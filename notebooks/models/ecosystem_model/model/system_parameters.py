"""
Definition of System Parameters, their types, and default values.

By using a dataclass to represent the System Parameters:
* We can use types for Python type hints
* Set default values
* Ensure that all System Parameters are initialized
"""

from dataclasses import dataclass

from model.utils import default
from model.types import List, Percentage


@dataclass
class Parameters:

    """System Parameters
    Each System Parameter is defined as:
    system parameter key: system parameter type = default system parameter value

    Because lists are mutable, we need to wrap each parameter list in the `default(...)` method.

    For default value assumptions, see the ASSUMPTIONS.md document.
    """

    # ECOSYSTEM PARAMETERS
    initial_population: List[int] = default([10000])
    onboarding_coefficient: List[float] = default(
        [0.75]
    )  # (%) adjust system-wide onboarding rate
    service_fee: List[Percentage] = default([0.05])  # (%) Fee charged on host earnings

    # CLIENT PARAMETERS
    client_competitor_price: List[float] = default(
        [2]
    )  # (ZAR/Mbps/Day) equivelent to AVG host service
    avg_client_allocation: List[int] = default([10])  # (Mbps) 'Bandwidth'
    client_registration_delay: List[int] = default([14])  # (Day)

    # HOST PARAMETERS
    host_line_cost: List[float] = default([0.05])  # (ZAR/Mbps/Day) ISP package
    avg_host_line: List[int] = default([1000])  # (Mbps) Backhaul capacity
    network_inefficiencies: List[float] = default(
        [0.2]
    )  # (%) losses due to hardware inefficiencies, downtime, environment, etc.
    host_setup_delay: List[int] = default([60])  # (Day)
    host_technical_difficulty: List[float] = default(
        [0.5]
    )  # (%) threshold for host onboarding
    MIN_expected_fulfillment: List[float] = default(
        [0.33]
    )  # (%) to what degree do hosts expect to fulfill their maximum capacity?
    avg_reserve_capacity: List[float] = default(
        [0.25]
    )  # (%) fraction of host capacity in reserve for temp client demand spikes
    price_change_delay: List[int] = default([14])


# Initialize Parameters instance with default values
parameters = Parameters().__dict__
