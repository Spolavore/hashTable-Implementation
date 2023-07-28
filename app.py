# classe que representa o Nodo da Lista ou seja o jogador
class NodoLista:
    def __init__(self, id, content, proximo_nodo=None):
        self.id = id    # id da fifa
        self.content = content # contem o nome do jogador na posicao 0 e a sua posicao nos nodos seguintes
        self.proximo = proximo_nodo

class ListaEncadeada:
    lista_consultas = []

    def __init__(self):
        self.inicio = None  

    def insere_no_inicio(self, novo_id ,novo_content):
        novoNodo = NodoLista(novo_id, novo_content)
        novoNodo.proximo = self.inicio
        self.inicio = novoNodo
 
    def tamanho_lista(self):
        contador = 0
        aux = self.inicio
        while(aux != None): 
            contador+=1           
            aux = aux.proximo
        return contador

    def getInfos(self, id):
        qtd_consultas = 0
        aux = self.inicio
        while aux != None:
            if aux.id == id:
                ListaEncadeada.lista_consultas.append(qtd_consultas)                
                return (aux, qtd_consultas)
            else:
                aux = aux.proximo
                qtd_consultas+=1

    def printa_lista(self):
        aux = self.inicio
        while aux != None:
            print(aux.id)
            aux = aux.proximo

# Definicao da class hash,
# recebe na inicializacao o tamanho dela
class Hash:
    posicoes_usadas = []
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash_table = [ListaEncadeada() for i in range(self.tamanho)] # cria uma lista de listas encadeadas independentes
     
    

# Função de Hash para definir o local, retorna a key de onde o valor
# está ou deve ser inserido
    def get_position(self, id):
        key = (id % self.tamanho) # modulo do id pelo tamanho
        if key not in Hash.posicoes_usadas:
            Hash.posicoes_usadas.append(key)

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
    def consulta(self, id, arquivo):
        position = self.get_position(id)
        nodo_aux = self.hash_table[position].getInfos(id)
        nodo = nodo_aux[0] if nodo_aux else None
        if nodo: # se o nodo não for false
            arquivo.write(f'{nodo.id} {nodo.content[0]} {nodo_aux[1]}\n')
        else:
            arquivo.write(f'{id} MISS\n')
        
    
if __name__ == '__main__':

    tamanho = int(input("Informe o tamanho da tabela hash: 1000, 2000, 4000 ou 8000: ")) # definicao do tamanho da tabela hash para os valores pré-estabelecidos 1000,2000,4000,8000
    tamanho = tamanho if tamanho in [1000,2000,4000,8000] else 1000                      # se for algum valor diferente, usa o tamanho = 1000 como padrão
    tabela_hash = Hash(tamanho)                                     
                                

    with open('players.csv', 'r') as file: # lendo o players.csv e colocando no Hash
        next(file)                         #Ignora a primeira linha
        for linha in file:
            data = linha.split(',', 2)
            tabela_hash.add(data)
    
    entradas_usadas = len(Hash.posicoes_usadas)            #Qtd de entradas usadas
    entradas_vazias = tamanho - len(Hash.posicoes_usadas)  #Qtd de entradas vazias
    taxa_de_ocupacao = entradas_usadas/entradas_vazias if entradas_vazias != 0 else entradas_usadas
    min_tamanho_de_lista = float("inf")
    max_tamanho_de_lista = float("-inf")
    medio_tamanho_de_lista = 0
    for lista in tabela_hash.hash_table:                #Percorre todas as listas encadeadas da tabela hash e calcula qual a maior e a menor lista
        tamanho_da_lista_atual = lista.tamanho_lista()
        medio_tamanho_de_lista += tamanho_da_lista_atual/tamanho
        if tamanho_da_lista_atual > max_tamanho_de_lista:
            max_tamanho_de_lista = tamanho_da_lista_atual
        if tamanho_da_lista_atual < min_tamanho_de_lista:
            min_tamanho_de_lista = tamanho_da_lista_atual  
    

    with open('experimento' + str(tamanho)+'.txt', 'w') as arq:
        arq.write('PARTE 1: ESTATISTICAS DA TABELA HASH \n')
        arq.write('NUMERO DE ENTRADAS DA TABELA USADAS '+ str(entradas_usadas) + '\n')
        arq.write('NUMERO DE ENTRADAS DA TABELA VAZIAS '+ str(entradas_vazias) + '\n')
        arq.write('TAXA DE OCUPACAO ' + str(taxa_de_ocupacao) + '\n')
        arq.write('MINIMO TAMANHO DE LISTA ' + str(min_tamanho_de_lista) + '\n')
        arq.write('MAXIMO TAMANHO DE LISTA ' + str(max_tamanho_de_lista) + '\n')
        arq.write('MEDIO TAMANHO DE LISTA ' + str(medio_tamanho_de_lista) + '\n')

        arq.write('PARTE 2: ESTATISTICAS DAS CONSULTAS \n')

        with open('consultas-fifa.txt', 'r') as consultas:  # fazendo as consultas necessarias

            for linha in consultas:
                tabela_hash.consulta(int(linha), arq)

        lista_quantidade_consultas = ListaEncadeada.lista_consultas
        min_nro_testes = min(lista_quantidade_consultas)
        max_nro_testes = max(lista_quantidade_consultas)
        media_nro_testes = sum(lista_quantidade_consultas)/len(lista_quantidade_consultas)
        media_consultas = sum(set(lista_quantidade_consultas))/len(set(lista_quantidade_consultas))
        arq.write('MINIMO NUMERO DE TESTES POR NOME ENCONTRADO ' + str(min_nro_testes) + '\n')
        arq.write('MAXIMO NUMERO DE TESTES POR NOME ENCONTRADO ' + str(max_nro_testes) + '\n')
        arq.write('MEDIA NUMERO DE TESTES NOME ENCONTRADO ' + str(media_nro_testes) + '\n')
        arq.write('MEDIA DAS CONSULTAS ' + str(media_consultas))
