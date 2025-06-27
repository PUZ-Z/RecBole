from recbole.quick_start import run_recbole
run_recbole(
    model='KGAT',
    dataset='amazon-book',
    config_file_list=['config/KGAT.yaml'],
)