from classes import *
from caminho import *
import csv
from imports import *

try:
    fake = Faker()
    for i in range(5):
        a = i +1
        globals()['pc%s' % a] = Computador(computador[i]['ip'], computador[i]['mac'], computador[i]['nome'])
    
    for s in range(2):
        a = s + 1
        globals()['sw%s' % a] = Switch(switch[s]['ip'], switch[s]['mac'], 'SW0'+str(a), 24)

    caminho = Grafo([], direcionado=False)
    caminho.adiciona_arestas({(sw1, pc1)})
    caminho.adiciona_arestas({(sw1, pc2)})
    caminho.adiciona_arestas({(sw1, sw2)})
    caminho.adiciona_arestas({(sw2, pc3)})
    caminho.adiciona_arestas({(sw2, pc4)})
    pc1.adicionar_tabela_arp(hash(pc2.ip), pc2.mac)
    pc4.getMac(hash(pc3.ip), caminho)
except AssertionError as erro:
    print(erro)