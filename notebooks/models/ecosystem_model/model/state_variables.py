from dataclasses import dataclass

import model.system_parameters as p
from model.types import Percentage


timeHorizon = int(365)  # (Days)


@dataclass
class StateVariables:

    """State Variables
    Each State Variable is defined as:
    state variable key: state variable type = default state variable value
    """

    clients: int = 10
    hosts: int = 1
    potential_users: int = 10_000  # p.Parameters["initial_population"][0]

    avg_price: float = 2  # (ZAR/Mbps/Day) The price hosts set for connectivity

    network_capacity: int = (
        1  # hosts * p.Parameters["avg_host_line"][0] # (Mbps) Total host capacity
    )
    indicated_network_demand: int = 0  # clients * p.Parameters["avg_client_allocation"][0] # (Mbps) Estimated total demand for connectivity
    network_allocation: int = 0  # (Mbps) Actual allocated demand
    network_penetration: Percentage = (
        0  # (%) Population servicable by hosts (a function of network coverage)
    )

    hosts_daily_revenue: float = 0  # (ZAR/Day)
    hosts_daily_profit: float = 0  # (ZAR/Day)
    platform_daily_revenue: float = 0  # (ZAR/Day)


# Initialize State Variables instance with default values
initial_state = StateVariables().__dict__
