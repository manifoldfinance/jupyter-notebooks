"""
# Policy functions return an Input/Signal (Python dictionary) which is used by State Update functions to update the state.
"""


import typing
from model.types import Percentage, Person, Mbps, ZAR_per_Mbps, ZAR_per_Day
import model.constants as constant


def p_client_adoption(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Person]:

    onboarding_coeff = params["onboarding_coefficient"]
    competitor_price = params["client_competitor_price"]
    registration_delay = params["client_registration_delay"]
    population = params["initial_population"]

    avg_price = previous_state["avg_price"]
    hosts = previous_state["hosts"]
    clients = previous_state["clients"]
    potential_users = previous_state["potential_users"]

    # WORD-OF-MOUTH
    # Calculate the probability that a
    probability_WOM = (clients + hosts) / (clients + hosts + potential_users)

    # Calculate price desirability (a percentage value where: 0 = no desirability, 1 = high desirability)
    price_desirability = 0
    if competitor_price - avg_price > 0:
        price_desirability = (competitor_price - avg_price) / competitor_price

    # Calculate the number of new clients who registered

    clientsRegistering = (
        onboarding_coeff
        * (potential_users * price_desirability * probability_WOM)
        / registration_delay
    )

    if clientsRegistering > potential_users:
        clientsRegistering = 0

    return {"clients": clientsRegistering}


def p_host_adoption(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Person]:

    onboarding_coeff = params["onboarding_coefficient"]
    setup_delay = params["host_setup_delay"]
    host_line_cost = params["host_line_cost"]
    avg_host_line = params["avg_host_line"]
    technical_difficulty = params["host_technical_difficulty"]
    MIN_expected_fulfillment = params["MIN_expected_fulfillment"]
    avg_client_allocation = params["avg_client_allocation"]
    population = params["initial_population"]

    avg_price = previous_state["avg_price"]
    hosts = previous_state["hosts"]
    clients = previous_state["clients"]
    potential_users = previous_state["potential_users"]
    network_penetration = previous_state["network_penetration"]

    # WORD-OF-MOUTH
    # Calculate the probability that
    probability_WOM = (clients + hosts) / (clients + hosts + potential_users)

    # Estimate the maximum number of clients a typical host can support
    max_clients = avg_host_line / avg_client_allocation  # (Person)

    # Adjust fulfillment expectation (%) based on actual network penetration
    host_expected_fulfillment = MIN_expected_fulfillment
    if MIN_expected_fulfillment < network_penetration:
        host_expected_fulfillment = network_penetration

    # Estimate the desire to become a host based on expected profit margins
    expected_revenue = (
        avg_price * max_clients * host_expected_fulfillment * avg_client_allocation
    )  # (ZAR/Day)
    operating_expenses = host_line_cost * avg_host_line  # (ZAR/Day)

    profit = expected_revenue - operating_expenses  # (ZAR/Day)

    if profit >= 0:
        expected_margin = profit / expected_revenue
    else:
        expected_margin = 0.01

    # Calculate the number of new hosts who registered

    hostsOnboarding = (
        onboarding_coeff
        * (
            expected_margin
            * potential_users
            * probability_WOM
            * (1 - technical_difficulty)
        )
        / setup_delay
    )

    if hostsOnboarding > potential_users:
        hostsOnboarding = 0

    return {"hosts": hostsOnboarding}


def p_network_capacity(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Mbps]:

    avg_host_line = params["avg_host_line"]
    hosts = previous_state["hosts"]
    network_inefficiencies = params["network_inefficiencies"]

    network_capacity = hosts * avg_host_line * (1 - network_inefficiencies)
    return {"network_capacity": network_capacity}


# Calculate the total demand for connectivity (note: this is the indicated demand from registered clients, and not the actual allocated demand. For allocated demand, see 'network_allocation')
def p_indicated_network_demand(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Mbps]:

    competitor_price = params["client_competitor_price"]
    avg_client_allocation = params["avg_client_allocation"]

    avg_price = previous_state["avg_price"]
    clients = previous_state["clients"]

    if avg_price > 0:
        price_attractiveness = competitor_price / avg_price
    else:
        price_attractiveness = 1

    indicated_network_demand = clients * avg_client_allocation * price_attractiveness

    return {"indicated_network_demand": indicated_network_demand}


def p_network_allocation(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Mbps]:

    avg_client_allocation = params["avg_client_allocation"]
    competitor_price = params["client_competitor_price"]

    clients = previous_state["clients"]
    avg_price = previous_state["avg_price"]
    network_penetration = previous_state["network_penetration"]

    if avg_price > 0:  # ensure never division by zero
        price_attractiveness = competitor_price / avg_price
    else:
        price_attractiveness = 1

    # To Do: what is the proper relationship between network penetration and access? Linear?
    access = network_penetration

    network_allocation = clients * avg_client_allocation * price_attractiveness * access

    return {"network_allocation": network_allocation}


def p_network_penetration(
    params, substep, state_history, previous_state
) -> typing.Dict[str, Percentage]:

    hosts = previous_state["hosts"]
    population = params["initial_population"]

    max_clients_servicable_by_host = constant.max_clients_servicable_by_host

    network_penetration = min(1, (hosts * max_clients_servicable_by_host / population))

    return {"network_penetration": network_penetration}


# Price is determined by supply and demand
def p_avg_price(
    params, substep, state_history, previous_state
) -> typing.Dict[str, ZAR_per_Mbps]:

    avg_reserve_capacity = params["avg_reserve_capacity"]
    price_change_delay = params["price_change_delay"]

    currentPrice = previous_state["avg_price"]
    indicated_network_demand = previous_state["indicated_network_demand"]
    network_capacity = previous_state["network_capacity"]

    if network_capacity > 0:
        supply_demand_ratio = indicated_network_demand / (
            network_capacity * (1 - avg_reserve_capacity)
        )
    else:
        supply_demand_ratio = 1

    # Determine price change based on supply-demand dynamics:
    desired_price = currentPrice * supply_demand_ratio
    newPrice = currentPrice + ((desired_price - currentPrice) / price_change_delay)

    if newPrice < 0:
        newPrice = 0

    return {"avg_price": newPrice}


def p_host_daily_yields(
    params, substep, state_history, previous_state
) -> typing.Dict[str, ZAR_per_Day]:

    host_line_cost = params["host_line_cost"]
    avg_host_line = params["avg_host_line"]

    avg_price = previous_state["avg_price"]
    hosts = previous_state["hosts"]
    network_allocation = previous_state["network_allocation"]

    total_daily_revenue = avg_price * network_allocation  # (ZAR/Day)
    total_daily_operating_expenses = hosts * host_line_cost * avg_host_line  # (ZAR/Day)
    total_daily_profit = (
        total_daily_revenue - total_daily_operating_expenses
    )  # (ZAR/Day)

    return {
        "hosts_daily_revenue": total_daily_revenue,
        "hosts_daily_profit": total_daily_profit,
    }


def p_platform_daily_revenue(
    params, substep, state_history, previous_state
) -> typing.Dict[str, ZAR_per_Day]:

    hosts_daily_revenue = previous_state["hosts_daily_revenue"]
    service_fee = params["service_fee"]

    platform_daily_revenue = hosts_daily_revenue * service_fee

    return {"platform_daily_revenue": platform_daily_revenue}
