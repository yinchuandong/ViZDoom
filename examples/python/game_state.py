from vizdoom import *
from random import randint
import time
import itertools as it
from PIL import Image
import numpy as np


def preprocess(img):
    img = Image.fromarray(img).convert('L')
    img = img.resize((84, 84), Image.ANTIALIAS)
    img = np.array(img)
    return img


def initialize_vizdoom(config_file_path):
    print("Initializing doom...")
    game = DoomGame()
    game.load_config(config_file_path)
    # game.set_window_visible(False)
    game.set_mode(Mode.PLAYER)
    game.set_screen_format(ScreenFormat.RGB24)
    game.set_screen_resolution(ScreenResolution.RES_640X480)
    game.init()
    print("Doom initialized.")
    return game


class GameState():
    def __init__(self):
        # self.game = initialize_vizdoom("../config/basic.cfg")
        self.game = initialize_vizdoom("../config/simpler_basic.cfg")
        # self.game = initialize_vizdoom("../../examples/config/deadly_corridor.cfg")
        self.button_size = self.game.get_available_buttons_size()
        # self.actions = [
        #     [1, 0, 0, 0, 0, 0, 0],
        #     [0, 1, 0, 0, 0, 0, 0],
        #     [0, 0, 1, 0, 0, 0, 0],
        #     [0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 1, 0, 0, 1, 0],
        #     [0, 0, 1, 0, 0, 0, 1],
        # ]
        self.actions = [
            [1, 0, 1],
            [0, 1, 1],
            [0, 0, 1],
        ]
        self.skip_rate = 4
        self.reset()
        return

    def reset(self):
        self.game.new_episode()
        self.terminal = self.game.is_episode_finished()
        img = self.game.get_state().screen_buffer
        x_t = preprocess(img)
        # x_t = x_t / 255.0
        self.s_t = np.stack((x_t, x_t, x_t, x_t), axis=2)
        self.reward = 0.0
        return

    def process(self, action_id):
        self.reward = self.game.make_action(self.actions[action_id], self.skip_rate)
        self.terminal = self.game.is_episode_finished()
        if not self.terminal:
            img = self.game.get_state().screen_buffer
            x_t1 = preprocess(img)
            x_t1 = np.reshape(x_t1, (84, 84, 1))
            # x_t1 = x_t1 / 255.0
            self.s_t1 = np.append(self.s_t[:, :, 1:], x_t1, axis=2)
        return

    def update(self):
        self.s_t = self.s_t1
        return


def test():
    episodes = 10
    gamestate = GameState()
    print 'button_size', gamestate.button_size
    for i in range(episodes):
        gamestate.reset()
        while not gamestate.terminal:
            gamestate.process(randint(0, len(gamestate.actions) - 1))
            # gamestate.process(0)
            Image.fromarray(gamestate.s_t).save('img/s_t.png')
            Image.fromarray(gamestate.s_t1).save('img/s_t1.png')
            print 'reward:', gamestate.reward
            print 'terminal:', gamestate.terminal
            print 'action_size:', len(gamestate.actions)
            print 'game_vars:', gamestate.game.get_state().game_variables
            gamestate.update()
            time.sleep(0.02)
        print "Result:", gamestate.game.get_total_reward()
        time.sleep(2)
    return


if __name__ == '__main__':
    test()
