class Television:
    """
    Class for television
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Constructor - how a tv object should look like at first
        """
        self.__channel = Television.MIN_CHANNEL
        self.__vol = Television.MIN_VOLUME
        self.__status = 'off'

    def power(self):
        """
        Function (method) to turn tv on or off when it is called on a tv object
        """
        if self.__status == 'off':
            self.__status = 'on'
        elif self.__status == 'on':
            self.__status = 'off'

    def channel_up(self):
        """
        Function (method) to increase tv channel value when it is called on a tv object
        """
        if self.__status == 'on' and self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status == 'off' or self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Function (method) to decrease tv channel value when it is called on a tv object
        """
        if self.__status == 'on' and self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__status == 'off' or self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Function (method) to change increase tv volume value when it is called on a tv object
        """
        if self.__status == 'on' and self.__vol < Television.MAX_VOLUME:
            self.__vol += 1
        elif self.__status == 'off' or self.__vol == Television.MAX_VOLUME:
            self.__vol = Television.MAX_VOLUME

    def volume_down(self):
        """
        Function (method) to change decrease tv volume value when it is called on a tv object
        """
        if self.__status == 'on' and self.__vol > Television.MIN_VOLUME:
            self.__vol -= 1
        elif self.__status == 'off' or self.__vol == Television.MIN_VOLUME:
            self.__vol = Television.MIN_VOLUME

    def __str__(self):
        """
        Function (method) to return a string to let the user print the status (on or off), channel and volume of a tv object.
        """
        if self.__status == 'on':
            return f'TV status: Is on = True, Channel = {self.__channel}, Volume = {self.__vol}'
        else:
            return f'TV status: Is on = False, Channel = {self.__channel}, Volume = {self.__vol}'

