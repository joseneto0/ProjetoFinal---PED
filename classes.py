from faker import Faker
import re
from tabela import *
from time import sleep
from caminho import *

class Dispositivos:
    def __init__(self, ip, mac, identificador):
        self.ip = ip
        self.mac = mac
        self.identificador = identificador

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

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    def Validar_MAC(self, str):
        regex = ("^([0-9A-Fa-f]{2}[:-])" + "{5}([0-9A-Fa-f]{2})|" + "([0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4})$")
        p = re.compile(regex)
        if(re.search(p, str)):
            return True
        else:
            return False

    def __str__(self):
        return str(self.identificador)

    def __repr__(self):
        return str(self)

class Computador(Dispositivos):
    def __init__(self, ip, mac, identificador):
        super().__init__(ip, mac, identificador)
        self.tabela_arp = TabelaHash(30)

    @property
    def tabela_arp(self):
        return self.__tabela_arp

    @tabela_arp.setter
    def tabela_arp(self, tabela_arp):
        self.__tabela_arp = tabela_arp
    
    def adicionar_tabela_arp(self, ip, mac):
        assert self.Validar_MAC(mac) == True, 'MAC Inválido'
        assert self.tabela_arp.contains(ip) == False, 'IP já vinculado a um endereço MAC'
        return self.tabela_arp.put(ip, mac)
    
    def getMac(self, ip):
        if self.tabela_arp.contains(ip) == True:
            return self.tabela_arp.get(ip)
        else:
            return False

    def __hash__(self):
        return hash(self.ip)

class Switch(Dispositivos):
    def __init__(self, ip, mac, identificador, qtd_portas=24):
        super().__init__(ip, mac, identificador)
        self.qtd_portas = qtd_portas
        self.tabela_roteamento = TabelaHash(60)

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
        self.__qtd_portas = qtd_portas

    def adicionar_tabela_roteamento(self, porta, mac):
        assert self.tabela_roteamento.contains(porta) == False, f'Porta {porta} já referenciada ao MAC: {self.tabela_roteamento.get(porta)}'
        assert len(self.tabela_roteamento) < self.qtd_portas, 'Portas do Switch Lotadas'
        if self.tabela_roteamento.verifica_mac_repetido(mac) == False:
            return self.tabela_roteamento.put(porta, mac)