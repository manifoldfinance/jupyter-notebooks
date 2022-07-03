import sys
import pandas as pd
from IPython import get_ipython


ipython = get_ipython()

# Find performance bottlenecks by timing Python cell execution
ipython.magic(
    "load_ext autotime"
)  # ipython.magic("...") is equivalent to % in Jupyter cell

# Reload all modules (except those excluded by %aimport) every time before executing the Python code typed
# See https://ipython.org/ipython-doc/stable/config/extensions/autoreload.html
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")


sys.path.append("../..")
sys.path.append("../../..")

# pds raise in event of erroring in chaining assignment
pd.options.mode.chained_assignment = "raise"

# Set plotly as the default plotting backend for pandas. Banteg thinks this is a better default than matplotlib.
pd.options.plotting.backend = "plotly"
