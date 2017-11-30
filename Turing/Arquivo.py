class Arquivo(object):
    txt_mt = ''
    txt_in = ''
    e_inicial = '' #estado inicial
    e_final = []   #estado final
    simbol_branco = ''
    i_fita = ''
    entrada = []
    transicaol = [] #sequencia de instruções = estado atual, simbolo lido, simbolo escrito, mover para, próximo estado.

    def __init__(sell, txt1, txt2): #passando por parâmetro os arquivos criados de entrada.
        sell.txt_mt = txt1 #passando o método através do parametro sell
        sell.txt_in = txt2
        Arquivo.reading_mt(sell)
        Arquivo.reading_in(sell)

    def reading_mt(sell):
        arq = open(sell.txt_mt, 'r')
        arquivo = arq.readlines()
        i = 0
        while i != len(arquivo): #len = tamanho do arquivo
            if i == 0:
                sell.e_inicial = arquivo[i][:-1]
            elif i == 1:
                sell.e_final = arquivo[i][:-1].split(',')
            elif i == 2:
                sell.simbol_branco = arquivo[i][:-1]
            elif i == 3:
                sell. i_fita = arquivo[i]
            elif i >= 4:
                transicao = Transicao()
                linha = arquivo[i][:-1]
                list_auxiliar = linha.split(',')
                transicao.estado_atual = list_auxiliar[0]
                transicao.reading = list_auxiliar[1]
                transicao.escrita = list_auxiliar[2]
                transicao.sentido = list_auxiliar[3]
                transicao.proximo_estado = list_auxiliar[4]
                sell.transicaol.append(transicao) #append está adicionando um novo elemento
            i = i + 1

    def reading_in(sell):
        arq = open(sell.txt_in, 'r')
        arquivo = arq.readlines()
        i = 0
        while i != len(arquivo):
            sell.entrada.append(sell. i_fita[:-1] + arquivo[i][:-1])
            i+=1
           # i = i + 1


class Transicao():
    estado_atual = ''
    reading = ''
    escrita = ''
    sentido = ''
    proximo_estado = ''