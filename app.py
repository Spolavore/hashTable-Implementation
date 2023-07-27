import pandas as pd
import numpy as np

class NodoLista:
    def __init__(self, id, content, proximo_nodo=None):
        self.id = id
        self.content = content
        self.proximo = proximo_nodo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def insere_no_inicio(self, novo_id ,novo_content):
        novoNodo = NodoLista(novo_id, novo_content)
        novoNodo.proximo = self.inicio
        self.inicio = novoNodo

    def isIn(self, id):
        aux = self.inicio
        while(aux != None):
            if aux.id == id:
                return True
            else:
                aux = aux.proximo

    def getInfos(self, id):
        aux = self.inicio
        while aux != None:
            if aux.id == id:
                return aux.content
            else:
                aux = aux.proximo
        return 'Jogador não está na Tabela'

    def printa_lista(self):
        aux = self.inicio
        while aux != None:
            print(aux.id)
            aux = aux.proximo

class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash_table = [ListaEncadeada()] * self.tamanho
    
    def create_hash(self):
        Hash.hash_table *= self.tamanho


# Função de Hash para definir o local, retorna a key de onde o valor
# está ou deve ser inserido
    def get_position(self, id):
        if self.tamanho == 1000:
            key = (id % self.tamanho)
            return key
        
   

    def add(self, infos):
        id = int(infos[0])
        content = infos[1:]
        position = self.get_position(id)
        if not self.hash_table[position].isIn(id): # se o id não estiver na lista
            self.hash_table[position].insere_no_inicio(id, content)
        else:
            print('Dado já foi adicionado')
      
    def consulta(self, id):
        position = self.get_position(id)
        print(self.hash_table[position].getInfos(id))
        
    
if __name__ == '__main__':

    tabela_hash = Hash(1000)

    with open('players.csv', 'r') as file:
        txt = file.read().split('\n')
        for i in range(1, len(txt)):
            data = txt[i].split(',')
            tabela_hash.add(data)

    with open('consultas-fifa.txt', 'r') as consultas:
        searchs = consultas.readlines()
        for i in range(0, len(searchs)):
            tabela_hash.consulta(int(searchs[i][0:len(searchs[i])-1]))
       

