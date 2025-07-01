from recbole.quick_start import run_recbole
run_recbole(
    model='CKE',
    dataset='amazon-book',
    config_file_list=['config/CKE.yaml'],
)