conda create -n recbole python=3.8
conda activate recbole

conda install -c aibox recbole

conda install -c dglteam dgl -y

pip install -U ipywidgets
pip install thop