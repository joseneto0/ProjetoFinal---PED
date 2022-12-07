class Dispositivos:
    def __init__(self, ip, mac):
        self.__ip = ip
        self.__mac = mac

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, mac):
        self.__mac = mac