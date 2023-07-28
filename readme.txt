A função hash utilizada foi f(x) = key % m, onde key é o id de cada jogador e o m é igual o tamanho de entrada da hash-table.
O tratamento de colisões foi feito utilizando endereçamento fechado (encadeamento), então cada posição da tabela é uma lista encadeada,
e sempre que houver colisão, o algoritmo adiciona a chave ao início da lista encadeada