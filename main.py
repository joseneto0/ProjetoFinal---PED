from classes import *
from caminho import *

try:
    fake = Faker()
    pc1 = Computador(fake.ipv4(), fake.mac_address(), 'PC Zezin')
    pc2 = Computador(fake.ipv4(), fake.mac_address(), 'PC Matheus')
    pc3 = Computador(fake.ipv4(), fake.mac_address(), 'PC Joanderson')
    pc4 = Computador(fake.ipv4(), fake.mac_address(), 'PC Samuel')
    sw1 = Switch(fake.ipv4(), fake.mac_address(), 'SW01', 24)
    caminho = Grafo([], direcionado=False)
    caminho.adiciona_arestas({(sw1, pc1)})
    caminho.adiciona_arestas({(sw1, pc2)})
    caminho.adiciona_arestas({(sw1, pc3)})
    caminho.adiciona_arestas({(sw1, pc4)})
    pc1.adicionar_tabela_arp(hash(pc2.ip), pc2.mac)
    pc2.adicionar_tabela_arp(hash(pc1.ip), pc1.mac)
    sw1.adicionar_tabela_roteamento(pc1.mac)
    sw1.adicionar_tabela_roteamento(pc2.mac)
    sw1.adicionar_tabela_roteamento(pc3.mac)
    sw1.adicionar_tabela_roteamento(pc4.mac)
    r = pc1.getMac(hash(pc3.ip))
    if r == False:
        caminho.busca_ip(pc1, pc3.ip)
        print(pc1.tabela_arp)
    else:
        print(r)

except AssertionError as erro:
    print(erro)