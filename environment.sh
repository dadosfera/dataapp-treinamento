#!/bin/bash
# Install Python 3.10 and get minimum set of dependencies
mamba create -y -n py38 python=3.8 future
mamba install -y -n py38 ipykernel jupyter_client ipython_genutils pycryptodomex future "pyarrow<8.0.0"
mamba run -n py38 pip install orchest

# Jupyter environment variable that specifies
# a path to search for kernels data files
# See https://jupyter-core.readthedocs.io/en/latest/paths.html
echo "export JUPYTER_PATH=/opt/conda/envs/py38/share/jupyter" >> /home/jovyan/.orchestrc
echo "export PATH='/opt/conda/envs/py38/bin/:$PATH'" >> /home/jovyan/.orchestrc

# Orchest related environment variable that can be set to specify
# the conda environment to use to start Jupyter kernels
echo "export CONDA_ENV=py38" >> /home/jovyan/.orchestrc
mamba run -n py38 pip install pandas snowflake-snowpark-python streamlit plotly
