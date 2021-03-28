import logging
from datetime import datetime
import pathlib
from mqtt_utils.message_manager import MessageManager

from hass_raspi_remote.messages.mouse_double_click import MouseDoubleClick
from hass_raspi_remote.messages.mouse_left_click import MouseLeftClick
from hass_raspi_remote.messages.mouse_position import MousePosition
from hass_raspi_remote.messages.mouse_right_click import MouseRightClick
from hass_raspi_remote.settings import settings

if __name__ == '__main__':
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d__%H_%M_%S")
    curr_folder = pathlib.Path(__file__).parent.absolute()

    logging.basicConfig(
        filename=f'{curr_folder}/logs/{dt_string}.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)

    MESSAGES = [MousePosition(), MouseLeftClick(), MouseRightClick(),
                MouseDoubleClick()]
    message_manager = MessageManager(MESSAGES)
    message_manager.update_credentials(settings.Mqtt.USERNAME,
                                       settings.Mqtt.PASSWORD)
    message_manager.connect(settings.Mqtt.ADDRESS, settings.Mqtt.PORT)

    logging.info('Starting message manager')
    message_manager.start()

    try:
        message_manager.loop_forever()
    except KeyboardInterrupt:
        message_manager.stop()
