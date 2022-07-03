"""
Various Python types used in the model
"""

import numpy as np
import sys


# See https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field

# If Python version is greater than equal to 3.8, import from typing module
# Else also import from typing_extensions module
if sys.version_info >= (3, 8):
    from typing import TypedDict, List, Callable, NamedTuple
else:
    from typing import List, NamedTuple
    from typing_extensions import TypedDict, Callable


# Generic types
Uninitialized = np.nan
Percentage = float
Person = int

# Network
Mbps = int
ZAR_per_Mbps = float

# Currents ecosystem
Currents = int
ZAR = float
ZAR_per_Day = float

# Simulation types
Run = int
Timestep = int
