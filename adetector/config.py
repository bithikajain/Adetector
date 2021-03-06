""" This is a configuration file """

"""Package paths - Please update before installation!"""
# a path to a folder in which trained weights are saved
WEIGHTS_FOLDER = \
     '/usr/src/Adetector/adetector/model_weights'
# a path to a folder in which data for unitests is stored
TEST_DATA_FOLDER = '/usr/src/Adetector/data'
# a path to a folder which conatains positive examples
AD_FOLDER = '/home/Data/audio_ads'
# a path to a folder which conatains negative music examples
MUSIC_FOLDER = '/home/Data/Music'
# a path to a folder which conatains negative music examples
PODCAST_FOLDER = '/home/Data/podcasts'

"""Model hyperparameters"""
SAMPLING_RATE = 22050  # the sampling rate of the audio file
CLIP_DURATION = 3  # length in seconds of the model's input
N_MFCC = 13  # number of mfc coefficients used when extracting features
N_TIMEBINS = 130  # number of timebins in the mfcc feature matrix.
                  # the shape of the mfcc feature matrix is (N_MFCC,N_TIMEBINS)
N_FEATURES = 1690  # used for NN model, where the input shape is (N_FEATURES,)

"""Data parameters"""
AD_FILE_DURATION = 30/60.0  # an average duration of an ad file in minutes
MUSIC_FILE_DURATION = 30/60.0  # music file duration in minutes
PODCAST_FILE_DURATION = 12/60.0  # podcast file duration in minutes
