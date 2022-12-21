from classes import *
from caminho import *
import csv
from imports import *

try:
    caminho = Grafo([], direcionado=False)
    for i, palavra in enumerate(lista_computadores):
        globals()['pc' + str(i)] = palavra
    for i, palavra in enumerate(lista_switches):
        globals()['sw' + str(i)] = palavra

    caminho.adiciona_arestas({((sw0, pc0))})
    caminho.adiciona_arestas({((sw0, pc1))})
    caminho.adiciona_arestas({((sw0, pc2))})
    caminho.adiciona_arestas({((sw0, pc3))})
    caminho.adiciona_arestas({((sw0, sw1))})
    caminho.adiciona_arestas({((sw1, pc4))})
    caminho.adiciona_arestas({((sw1, pc5))})
    caminho.adiciona_arestas({((sw1, pc6))})
    caminho.adiciona_arestas({((sw1, pc7))})

    pc6.getMac(hash(pc2.ip), caminho)
    pc0.getMac(hash(pc3.ip), caminho)
except AssertionError as erro:
    print(erro)