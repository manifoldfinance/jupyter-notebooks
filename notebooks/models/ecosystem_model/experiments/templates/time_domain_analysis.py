import copy

from experiments.default_experiment import experiment


# Prevent Mutating state
experiment = copy.deepcopy(experiment)

# 1 Average Yeear
TIMESTEPS = 365.2524


"""
parameter_overrides = {
    "name": [newValue],
    "name2": [newValue2],
}
"""


# Override default experiment Simulation and System Parameters related to timing
experiment.simulations[0].timesteps = TIMESTEPS


# Override default experiment System Parameters
# experiment.simulations[0].model.params.update(parameter_overrides)
