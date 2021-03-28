import math
from typing import Any, Dict

from mqtt_utils.messages.mqtt_message import MQTTMessage

from hass_raspi_remote.mouse_controller import MouseController
from hass_raspi_remote.settings import settings


class MouseLeftClick(MQTTMessage):
    def __init__(self):
        super().__init__(settings.Messages.MOUSE_LEFT)
        self.mouse_controller = MouseController()

    def execute(self, payload: Dict[str, Any]):
        self.mouse_controller.left_click()
