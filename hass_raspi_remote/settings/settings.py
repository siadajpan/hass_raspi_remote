class Mqtt:
    ADDRESS = '192.168.0.164'
    PORT = 1883
    USERNAME = 'karol'
    PASSWORD = 'klapeczki'
    TOPIC = 'mouse/master_bedroom/tv/'
    ERROR_TOPIC = 'errors/raspi_tv/master_bedroom/main/'
    MESSAGE_FREQUENCY = 2  # this is constant on the light picker


class Messages:
    MOUSE_POSITION = Mqtt.TOPIC + "position"
    MOUSE_LEFT = Mqtt.TOPIC + "left_click"
    MOUSE_DOUBLE = Mqtt.TOPIC + "double_click"
    MOUSE_RIGHT = Mqtt.TOPIC + "right_click"
    PRESS_SPACE = Mqtt.TOPIC + "press_space"


class Mouse:
    POSITION_MULTIPLIER = 5
