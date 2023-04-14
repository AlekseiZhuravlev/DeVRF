_base_ = './default.py'

expname = 'exp_example'
basedir = '/itet-stor/azhuavlev/net_scratch/Projects/Results/DeVRF/'

data = dict(
    datadir='/itet-stor/azhuavlev/net_scratch/Projects/Data/DeVRF/lego/dynamic_4views/',
    dataset_type='blender',
    white_bkgd=True,
)

fine_train = dict(
    static_model_path = "/itet-stor/azhuavlev/net_scratch/Projects/Results/DeVRF/exp_example/fine_last.tar",
)



