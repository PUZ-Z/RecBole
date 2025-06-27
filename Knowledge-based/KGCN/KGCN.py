import sys
sys.path.append('.')
import custom_trainer

from recbole.quick_start import run_recbole
run_recbole(
    model='KGCN',
    dataset='amazon-book',
    config_file_list=['config/KGCN.yaml']
)