import os
PATH_TO_DATA_DIRECTORY='/media/venkatesh/slave/dataset/iid'
SAMPLING_RATE=44100

### FOR TRADITONAL MACHINE LEARNING METHOD ###
#PATH_TO_DATASET='/homedtic/vshenoykadandale/dataset/MedleyDB'
PATH_TO_DATASET=os.path.join(PATH_TO_DATA_DIRECTORY,'MedleyDB')
PATH_TO_MATFILES=os.path.join(PATH_TO_DATA_DIRECTORY,'mat')
PATH_TO_DATASET_SPLIT_FOLDERS=os.path.join(PATH_TO_DATA_DIRECTORY,'splits')

PATH_TO_WAV_FILES=os.path.join(PATH_TO_DATA_DIRECTORY,'wavs')
PATH_TO_ORIGINAL_WAV_FILES=os.path.join(PATH_TO_WAV_FILES,'original')
PATH_TO_HARMONIC_WAV_FILES=os.path.join(PATH_TO_WAV_FILES,'harmonic')
PATH_TO_RESIDUAL_WAV_FILES=os.path.join(PATH_TO_WAV_FILES,'residual')

PATH_TO_FEATURES=os.path.join(PATH_TO_DATA_DIRECTORY,'features')
PATH_TO_ORIGINAL_FEATURES=os.path.join(PATH_TO_FEATURES,'original')
PATH_TO_HARMONIC_FEATURES=os.path.join(PATH_TO_FEATURES,'harmonic')
PATH_TO_RESIDUAL_FEATURES=os.path.join(PATH_TO_FEATURES,'residual')

PATH_TO_TRAINSET=os.path.join(PATH_TO_DATA_DIRECTORY,'train')
PATH_TO_ORIGINAL_TRAINSET=os.path.join(PATH_TO_TRAINSET,'original')
PATH_TO_HARMONIC_TRAINSET=os.path.join(PATH_TO_TRAINSET,'harmonic')
PATH_TO_RESIDUAL_TRAINSET=os.path.join(PATH_TO_TRAINSET,'residual')

PATH_TO_TESTSET=os.path.join(PATH_TO_DATA_DIRECTORY,'test')
PATH_TO_ORIGINAL_TESTSET=os.path.join(PATH_TO_TESTSET,'original')
PATH_TO_HARMONIC_TESTSET=os.path.join(PATH_TO_TESTSET,'harmonic')
PATH_TO_RESIDUAL_TESTSET=os.path.join(PATH_TO_TESTSET,'residual')

PATH_TO_RESULTS=os.path.join(PATH_TO_DATA_DIRECTORY,'results')
PATH_TO_ORIGINAL_RESULTS=os.path.join(PATH_TO_RESULTS,'original')
PATH_TO_HARMONIC_RESULTS=os.path.join(PATH_TO_RESULTS,'harmonic')
PATH_TO_RESIDUAL_RESULTS=os.path.join(PATH_TO_RESULTS,'residual')

MEDLEY_N_CLASSES=11

### FOR DEEP LEARNING METHOD ###
#PATH_TO_WAV_FILES='/homedtic/vshenoykadandale/instrument-recognition/data/'
PATH_TO_LABELS='/homedtic/vshenoykadandale/instrument-recognition/data/dataset_'
PATH_TO_METADATA='/homedtic/vshenoykadandale/DeepLearning/metadata/'
PATH_TO_RESULTS='/homedtic/vshenoykadandale/DeepLearning/results/'
MODEL_MEANS_BASEPATH = './means/'
MODEL_HISTORY_BASEPATH = './history/'
MODEL_WEIGHT_BASEPATH = './weights/'
MEDLEY_TRAIN_FEATURE_BASEPATH = '/homedtic/vshenoykadandale/DeepLearning/data/'
MEDLEY_TEST_FEATURE_BASEPATH = '/homedtic/vshenoykadandale/DeepLearning/test_data/'

TRAIN_SPLIT = 0.85
VALIDATION_SPLIT = 0.15
N_TRAINING_SET = 6705
MAX_EPOCH_NUM = 400
EARLY_STOPPING_EPOCH = 20
SGD_LR_REDUCE = 5
BATCH_SIZE = 16
ALLOWED_MODELS = ['han16', 'singlelayer', 'multilayer']
