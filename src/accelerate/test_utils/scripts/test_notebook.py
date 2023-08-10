# Test file to ensure that in general certain situational setups for notebooks work.

import torch


assert not torch.cuda.is_initialized(), "CUDA was initialized before the test script."

from accelerate import Accelerator  # noqa

assert not torch.cuda.is_initialized(), "CUDA was initialized upon importing the `Accelerator` class."
