GAME = 'doom'
STATE_DIM = 84
STATE_CHN = 4
ACTION_DIM = 6

BATCH_SIZE = 32  # the batch size of training
RANDOM_ACTION_PROBILITY = 1e-10  # the probilitf of randomly selecting action

LOCAL_T_MAX = 5  # repeat step size
RMSP_ALPHA = 0.99  # decay parameter for RMSProp
RMSP_EPSILON = 0.1  # epsilon parameter for RMSProp
GAMMA = 0.99
ENTROPY_BETA = 0.000001  # 0.01 for FFNet
MAX_TIME_STEP = 10 * 10**7

INITIAL_ALPHA_LOW = 1e-5    # log_uniform low limit for learning rate
INITIAL_ALPHA_HIGH = 1e-3   # log_uniform high limit for learning rate
INITIAL_ALPHA_LOG_RATE = 0.4226  # log_uniform interpolate rate for learning rate (around 7 * 10^-4)

PARALLEL_SIZE = 4  # how many actor threads
TRAIN_SIZE = 1  # how many training threads
USE_GPU = True
USE_LSTM = False  # currently cannot use lstm

REDIS_QUEUE_NAME = 'doom'
CHECKPOINT_DIR = 'tmp/checkpoints'
LOG_FILE = 'tmp/a3c_log'

