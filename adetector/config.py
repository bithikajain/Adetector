''' This is a configuration file '''
# a path to a folder with trained weights - Please update before installation
WEIGHTS_FOLDER = '/home/ohadmich/Documents/Github/Ad_Detector/adetector/models'

# model hyperparameters
SAMPLING_RATE = 22050 # the sampling rate of the audio file
CLIP_DURATION = 3 # length in seconds of the input clip to the classification model
N_MFCC = 13 # number of mfc coefficients used when extracting features
N_TIMEBINS = 130 # number of timebins in the  