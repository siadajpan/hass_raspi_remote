import logging
import time
from typing import Tuple

from pynput import mouse, keyboard
from singleton_decorator import singleton

from hass_raspi_remote.settings import settings


@singleton
class MouseController:
    def __init__(self):
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.last_signal_time = time.time()
        self.last_xy_signal = (0, 0)
        self._logger = logging.getLogger(self.__class__.__name__)

    def update_signal(self, x, y, signal_time):
        self.last_xy_signal = (x, y)
        self.last_signal_time = signal_time

    def move_mouse_by_vector(self, vector_xy: Tuple[float, float]):
        self._logger.debug(f'Moving mouse by vector {vector_xy}')
        vector_xy = [value * settings.Mouse.POSITION_MULTIPLIER
                     for value in vector_xy]

        self.mouse.move(*vector_xy)

    def receive_position(self, x, y):
        curr_signal_time = time.time()

        latency = 1 / settings.Mqtt.MESSAGE_FREQUENCY
        if curr_signal_time - self.last_signal_time > latency + 0.1:
            self.update_signal(x, y, curr_signal_time)
            # received beginning of movement
            self._logger.debug(f'Received beginning of movement time: '
                               f'{self.last_signal_time}')
            return

        # received continuation of movement
        vector = (x - self.last_xy_signal[0], y - self.last_xy_signal[1])
        self.move_mouse_by_vector(vector)
        self.update_signal(x, y, curr_signal_time)

    def left_click(self):
        self.mouse.click(mouse.Button.left, 1)

    def double_click(self):
        self.mouse.click(mouse.Button.left, 2)

    def right_click(self):
        self.mouse.click(mouse.Button.right, 1)

    def press_space(self):
        self.keyboard.press(keyboard.Key.space)
        self.keyboard.release(keyboard.Key.space)
