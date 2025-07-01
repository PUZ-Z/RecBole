from recbole.quick_start import run_recbole
run_recbole(
    model='KGIN',
    dataset='amazon-book',
    config_file_list=['config/KGIN.yaml'],
)