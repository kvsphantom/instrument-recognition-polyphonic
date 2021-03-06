### FOR TRADITONAL MACHINE LEARNING METHOD ###
PATH_TO_DATASET='/homedtic/vshenoykadandale/dataset/MedleyDB'
PATH_TO_MATFILES='/homedtic/vshenoykadandale/instrument-recognition/data/mat_files'

PATH_TO_DATASET_SPLIT_FOLDERS='/homedtic/vshenoykadandale/instrument-recognition/data/dataset'
PATH_TO_ORIGINAL_WAV_FILES='/homedtic/vshenoykadandale/instrument-recognition/data/original/wavs'
PATH_TO_HARMONIC_WAV_FILES='/homedtic/vshenoykadandale/instrument-recognition/data/harmonic/wavs'
PATH_TO_RESIDUAL_WAV_FILES='/homedtic/vshenoykadandale/instrument-recognition/data/residual/wavs'

PATH_TO_ORIGINAL_FEATURES='/homedtic/vshenoykadandale/instrument-recognition/data/original/features'
PATH_TO_HARMONIC_FEATURES='/homedtic/vshenoykadandale/instrument-recognition/data/harmonic/features'
PATH_TO_RESIDUAL_FEATURES='/homedtic/vshenoykadandale/instrument-recognition/data/residual/features'

PATH_TO_ORIGINAL_TRAINSET='/homedtic/vshenoykadandale/instrument-recognition/data/original/train'
PATH_TO_HARMONIC_TRAINSET='/homedtic/vshenoykadandale/instrument-recognition/data/harmonic/train'
PATH_TO_RESIDUAL_TRAINSET='/homedtic/vshenoykadandale/instrument-recognition/data/residual/train'

PATH_TO_ORIGINAL_TESTSET='/homedtic/vshenoykadandale/instrument-recognition/data/original/test'
PATH_TO_HARMONIC_TESTSET='/homedtic/vshenoykadandale/instrument-recognition/data/harmonic/test'
PATH_TO_RESIDUAL_TESTSET='/homedtic/vshenoykadandale/instrument-recognition/data/residual/test'

PATH_TO_ORIGINAL_RESULTS='/homedtic/vshenoykadandale/instrument-recognition/data/original/results'
PATH_TO_HARMONIC_RESULTS='/homedtic/vshenoykadandale/instrument-recognition/data/harmonic/results'
PATH_TO_RESIDUAL_RESULTS='/homedtic/vshenoykadandale/instrument-recognition/data/residual/results'

MEDLEY_N_CLASSES=11

### FOR DEEP LEARNING METHOD ###
PATH_TO_WAV_FILES='/homedtic/vshenoykadandale/instrument-recognition/data/'
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
