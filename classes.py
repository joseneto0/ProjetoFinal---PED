from faker import Faker
import re

class Dispositivos:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

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
        assert self.Validar_MAC(mac) == True, 'MAC Inválido'
        self.__mac = mac

    def Validar_MAC(self, str):
        regex = ("^([0-9A-Fa-f]{2}[:-])" + "{5}([0-9A-Fa-f]{2})|" + "([0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4})$")
        p = re.compile(regex)
        if(re.search(p, str)):
            return True
        else:
            return False

class Computador(Dispositivos):
    def __init__(self, ip, mac, nome):
        super().__init__(ip, mac)
        self.nome = nome
        self.tabela_arp = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tabela_arp(self):
        return self.__tabela_arp

    @tabela_arp.setter
    def tabela_arp(self, tabela_arp):
        self.__tabela_arp = tabela_arp

    def adicionar_tabela_arp(self, lista):
        for i in lista:
            ip, mac = i.split('|')
            assert self.Validar_MAC(mac) == True, 'MAC Invalido na Inserção'
            macs = [i[(i.index('|')+1):] for i in self.tabela_arp]
            ips = [i[:((i.index('|')))] for i in self.tabela_arp]
            if mac not in macs and ip not in ips:
                self.tabela_arp.append(i)

class Switch(Dispositivos):
    def __init__(self, ip, mac, qtd_portas=4):
        super().__init__(ip, mac)
        self.qtd_portas = qtd_portas

    @property
    def tabela_roteamento(self):
        return self.__tabela_roteamento

    @tabela_roteamento.setter
    def tabela_roteamento(self, tabela_roteamento):
        self.__tabela_roteamento = tabela_roteamento

    @property
    def qtd_portas(self):
        return self.__qtd_portas

    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        assert qtd_portas in [4, 8, 16, 24], 'Porta Incorreta. Tente Novamente [4, 8, 16, 24]'
        self._qtd_portas = qtd_portas

if __name__ == '__main__':
    try:
        fake = Faker()
        pc1 = Computador(fake.ipv4(), fake.mac_address(), 'zezin')
        for i in range(2):
            pc1.adicionar_tabela_arp([f'{fake.ipv4()}|{fake.mac_address()}'])
        print(pc1.tabela_arp)
    except AssertionError as erro:
        print(erro)
