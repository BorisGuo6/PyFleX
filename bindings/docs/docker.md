# Using Docker for compiling PyFleX

We provide both Dockerfile and pre-built Docker container for compiling PyFleX. After compilation, you will be able to use PyFleX outside docker. We would like to give special thanks to [Yusufma03](https://github.com/Yusufma03) for providing this solution.

## Prerequisite

- Install [docker-ce](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker#quickstart)
- Install [Anaconda](https://www.anaconda.com/distribution/)
- Install Pybind11 using `conda install pybind11`
- Clone PyFleX `git clone https://github.com/YunzhuLi/PyFleX.git`

## Running pre-built Dockerfile

- Pull the pre-built docker file

```
docker pull yunzhuli/pyflex_16_04_cuda_9_1
```

- Assuming you are using Anaconda, using the following command to run docker, which will mount the python environment and PyFleX into the docker container. Make sure you have replaced `PATH_TO_PyFleX` and `PATH_TO_ANACONDA` with the corresponding paths.

```
docker run \
  -v PATH_TO_PyFleX:/workspace/PyFleX \
  -v PATH_TO_ANACONDA:/workspace/anaconda \
  -it yunzhuli/pyflex_16_04_cuda_9_1:latest
```
For example
```
docker run \
  -v /home/transfer/chenhn/PyFleX:/workspace/PyFleX \
  -v /home/transfer/anaconda3:/workspace/anaconda \
  -it yunzhuli/pyflex_16_04_cuda_9_1:latest
```

- Now you are in the Docker environment. Go to the code repo and compile PyFleX

```
export PATH="/workspace/anaconda/bin:$PATH"
cd /workspace/PyFleX
export PYFLEXROOT=${PWD}
export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH
export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH
cd bindings; mkdir build; cd build; cmake ..; make -j
```

- Now that PyFleX has properly compiled. You can move outside docker, export the environment variables and start playing with PyFleX.
```
cd /workspace/PyFleX
export PYFLEXROOT=${PWD}
export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH
export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH
cd ${PYFLEXROOT}/bindings/examples
python test_FluidFall.py
```

## Running with Dockerfile

We also posted the [Dockerfile](Dockerfile). To generate the pre-built file, download the Dockerfile in this directory and run
```
docker build -t pyflex_16_04_cuda_9_1 .
```
in the directory that contains the Dockerfile.
