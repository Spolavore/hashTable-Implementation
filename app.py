# classe que representa o Nodo da Lista ou seja o jogador
class NodoLista:
    def __init__(self, id, content, proximo_nodo=None):
        self.id = id    # id da fifa
        self.content = content # contem o nome do jogador na posicao 0 e a sua posicao nos nodos seguintes
        self.proximo = proximo_nodo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None  

    def insere_no_inicio(self, novo_id ,novo_content):
        novoNodo = NodoLista(novo_id, novo_content)
        novoNodo.proximo = self.inicio
        self.inicio = novoNodo

    # Função que verifica se um jogador já está na lista com base no seu id
    # -> não está sendo utilizada pois não há jogadores repetidos
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
                return aux
            else:
                aux = aux.proximo
        return False # caso não haja o jogador

    def printa_lista(self):
        aux = self.inicio
        while aux != None:
            print(aux.id)
            aux = aux.proximo

# Definicao da class hash,
# recebe na inicializacao o tamanho dela
class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash_table = [ListaEncadeada()] * self.tamanho # lista de listas encadeadas
     


# Função de Hash para definir o local, retorna a key de onde o valor
# está ou deve ser inserido
    def get_position(self, id):
        key = (id % self.tamanho) # modulo do id pelo tamanho
        return key
        
   

    def add(self, infos):
        id = int(infos[0])
        content = infos[1:]
        position = self.get_position(id) # pega a posicao que o dado deve ser inserido com base na funcao hash

        # verificacao caso quisessemos garantir que jogadores duplicados nao a
        # aparecessem na lista
        # if not self.hash_table[position].isIn(id): 
        #     self.hash_table[position].insere_no_inicio(id, content)
        # else:
        #     print('Dado já foi adicionado')

        self.hash_table[position].insere_no_inicio(id, content)
      
    # Com base no id vai para o posicao do array especifico
    # E Posteriormente chama uma funcao da propria classe da lista Encadeada 
    # para consultar se o elemento esta naquela lista
    def consulta(self, id):
        position = self.get_position(id)
        nodo = self.hash_table[position].getInfos(id)
        if nodo: # se o nodo não for false
            print(f'{nodo.id} {nodo.content[0]}')
        
    
if __name__ == '__main__':

    tabela_hash = Hash(1000) # definicao do tamanho da tabela hash

    with open('players.csv', 'r') as file: # lendo o players.csv e colocando no Hash
        txt = file.read().split('\n')
        for i in range(1, len(txt)):
            data = txt[i].split(',')
            tabela_hash.add(data)

    with open('consultas-fifa.txt', 'r') as consultas:  # fazendo as consultas necessarias
        searchs = consultas.readlines()
        for i in range(0, len(searchs)):
            tabela_hash.consulta(int(searchs[i][0:len(searchs[i])-1]))