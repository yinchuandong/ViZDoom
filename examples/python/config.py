GAME = 'doom'
STATE_DIM = 84
STATE_CHN = 4
ACTION_DIM = 3

LOCAL_T_MAX = 5  # repeat step size
RMSP_ALPHA = 0.99  # decay parameter for RMSProp
RMSP_EPSILON = 0.1  # epsilon parameter for RMSProp
GAMMA = 0.99
ENTROPY_BETA = 0.01  # 0.01 for FFNet
MAX_TIME_STEP = 10 * 10**7

INITIAL_ALPHA_LOW = 1e-4    # log_uniform low limit for learning rate
INITIAL_ALPHA_HIGH = 1e-2   # log_uniform high limit for learning rate
INITIAL_ALPHA_LOG_RATE = 0.4226  # log_uniform interpolate rate for learning rate (around 7 * 10^-4)

GREEDY_EPSILON_START = [1.0, 1.0, 1.0]  # initial epsilon greedy
GREEDY_EPSILON_END = [0.1, 0.01, 0.5]  # final epsilon greedy
GREEDY_DISTRIBUTION = [0.4, 0.3, 0.3]  # the probility of choosing
GREEDY_MAX_STEP = 4 * 10**6  # the first 4 million frames


PARALLEL_SIZE = 8  # parallel thread size, please start game_server first
USE_GPU = True
USE_LSTM = True

CHECKPOINT_DIR = 'tmp/checkpoints'
LOG_FILE = 'tmp/a3c_log'
