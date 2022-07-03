"""
cadCAD model State Update Block structure, composed of Policy and State Update Functions
"""


from model.policy_functions import p_network_capacity
import model.system_parameters
import model.policy_functions as policy
import model.state_update_functions as state

# from model.utils import update_from_signal


state_update_blocks = [
    {
        "description": """
            User Adoption
        """,
        "policies": {
            "client_adoption": policy.p_client_adoption,
            "host_adoption": policy.p_host_adoption,
        },
        "variables": {
            "clients": state.s_clients,
            "hosts": state.s_hosts,
            "potential_users": state.s_potential_users,
        },
    },
    {
        "description": """
            Network Demand & Allocation
        """,
        "policies": {
            "indicated_network_demand": policy.p_indicated_network_demand,
            "network_capacity": policy.p_network_capacity,
            "network_allocation": policy.p_network_allocation,
            "network_penetration": policy.p_network_penetration,
        },
        "variables": {
            "network_capacity": state.s_network_capacity,
            "indicated_network_demand": state.s_indicated_network_demand,
            "network_allocation": state.s_network_allocation,
            "network_penetration": state.s_network_penetration,
        },
    },
    {
        "description": """
            Price
        """,
        "policies": {"avg_price": policy.p_avg_price},
        "variables": {"avg_price": state.s_avg_price},
    },
    {
        "description": """
            Yields
        """,
        "policies": {
            "hosts_daily_revenue": policy.p_host_daily_yields,
            "hosts_daily_profit": policy.p_host_daily_yields,
            "platform_daily_revenue": policy.p_platform_daily_revenue,
        },
        "variables": {
            "hosts_daily_revenue": state.s_hosts_daily_revenue,
            "hosts_daily_profit": state.s_hosts_daily_profit,
            "platform_daily_revenue": state.s_platform_daily_revenue,
        },
    },
]
