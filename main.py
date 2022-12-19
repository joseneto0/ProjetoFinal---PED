from classes import *
from caminho import *

try:
    fake = Faker()
    pc1 = Computador(fake.ipv4(), fake.mac_address(), 'PC Zezin')
    pc2 = Computador(fake.ipv4(), fake.mac_address(), 'PC Matheus')
    pc3 = Computador(fake.ipv4(), fake.mac_address(), 'PC Joanderson')
    pc4 = Computador(fake.ipv4(), fake.mac_address(), 'PC Samuel')
    sw1 = Switch(fake.ipv4(), fake.mac_address(), 'SW01', 24)
    sw2 = Switch(fake.ipv4(), fake.mac_address(), 'SW02', 24)
    caminho = Grafo([], direcionado=False)
    caminho.adiciona_arestas({(sw1, pc1)})
    caminho.adiciona_arestas({(sw1, pc2)})
    caminho.adiciona_arestas({(sw1, sw2)})
    caminho.adiciona_arestas({(sw2, pc3)})
    caminho.adiciona_arestas({(sw2, pc4)})
    pc1.adicionar_tabela_arp(hash(pc2.ip), pc2.mac)
    pc2.adicionar_tabela_arp(hash(pc1.ip), pc1.mac)
    pc1.getMac(hash(pc3.ip), caminho)
    pc2.getMac(hash(pc4.ip), caminho)
except AssertionError as erro:
    print(erro)