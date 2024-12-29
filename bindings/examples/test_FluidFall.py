import os
import torch
import os
import subprocess

# Print CUDA details
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version via PyTorch: {torch.version.cuda}")
print(f"Is CUDA available: {torch.cuda.is_available()}")
print(f"CUDA devices count: {torch.cuda.device_count()}")

# Print CUDA environment variables
print(f"PATH: {os.environ.get('PATH')}")
print(f"LD_LIBRARY_PATH: {os.environ.get('LD_LIBRARY_PATH')}")

# Get and print the CUDA toolkit version using `nvcc`
try:
    nvcc_version = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    print(f"CUDA version via nvcc:\n{nvcc_version}")
except Exception as e:
    print(f"Failed to get CUDA version using nvcc: {e}")
import numpy as np
import pyflex
import time


time_step = 120
des_dir = 'test_FluidFall'
os.system('mkdir -p ' + des_dir)

pyflex.init()

scene_params = np.array([])
pyflex.set_scene(4, scene_params, 0)

for i in range(time_step):
    pyflex.step(capture=1, path=os.path.join(des_dir, 'render_%d.tga' % i))

pyflex.clean()
