import math
from typing import Any, Dict

from mqtt_utils.messages.mqtt_message import MQTTMessage

from hass_raspi_remote.mouse_controller import MouseController
from hass_raspi_remote.settings import settings


class MousePosition(MQTTMessage):
    def __init__(self):
        super().__init__(settings.Messages.MOUSE_POSITION)
        self.mouse_controller = MouseController()

    def execute(self, payload: Dict[str, Any]):
        self._logger.debug(f'Executing Mouse Position message with payload '
                           f'{payload}')
        color = payload.get('color', None)
        if color is None:
            return
        angle = color.get('h', None)
        r = color.get('s', None)
        if not angle or not color:
            return

        angle = (360 - angle) * math.pi/180
        x = r * math.cos(angle)
        y = - r * math.sin(angle)
        self.mouse_controller.receive_position(x, y)
