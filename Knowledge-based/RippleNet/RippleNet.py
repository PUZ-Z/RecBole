from recbole.quick_start import run_recbole
run_recbole(
    model='RippleNet',
    dataset='amazon-book',
    config_file_list=['config/RippleNet.yaml'],
)