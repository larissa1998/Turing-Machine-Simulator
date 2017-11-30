import Arquivo
from enum import Enum

#Se não houver entrada alguma na tabela de transição para a combinação atual de símbolo e estado, a máquina para de funcionar
class Move(Enum):
    Stay = 0
    Right = 1
    Left = -1


class MaquinaTuring(object):
    e_inicial = ''
    e_final = []
    simbolo_branco = ''
    i_fita = ''
    transicaol = [] #listar transições
    reading_files = None
    entrada = []
    fita_out = []


    def __init__(sell, txt1, txt2):
        reading_files = Arquivo.Arquivo(txt1, txt2)
        sell.e_inicial = reading_files.e_inicial
        sell.e_final = reading_files.e_final
        sell.simbolo_branco = reading_files.simbol_branco
        sell.i_fita = reading_files.i_fita
        sell.transicaol = reading_files.transicaol
        sell.entrada = reading_files.entrada

    def proximo_estado(sell, estado_atual, reading):
        retorno = []

        for transicao in sell.transicaol:
            if (transicao.estado_atual == estado_atual and transicao.reading == reading):
                retorno.append(transicao.sentido)
                retorno.append(transicao.escrita)
                retorno.append(transicao.proximo_estado)
                return retorno
        return retorno

    def process_fita(sell, fita_str):
        fita = list(fita_str)
        reading = 0
        estado_atual = sell.e_inicial
        resultado = -1
        while resultado == -1:

            if (sell.verifica_e_final(estado_atual)):
                sell.fita_out = fita
                stop = 1
                break
            auxiliar = sell.proximo_estado(estado_atual, fita[reading])
            if (len(auxiliar) == 0):
                sell.fita_out = fita
                stop = 0
                break
            fita[reading] = auxiliar[1]
            if (auxiliar[0] == 'D'):
                reading = reading + 1;
                if (reading == len(fita) - 1):
                    fita.append(sell.simbolo_branco)
                estado_atual = auxiliar[2]
            elif (auxiliar[0] == 'E'):
                if (fita[reading] == sell.i_fita):
                    stop = 0
                    break
                    reading = reading - 1
                estado_atual = auxiliar[2]
        return stop

    def process_arquivo(sell):
        arquivo = open('saida.out', 'r')
        texto = arquivo.readlines()

        for fita in sell.entrada:
            resultado = sell.process_fita(fita)
            if resultado == 1:
                print(sell.fita_out)
                print('Aceito\n')
                texto.append(fita + ';1')
            elif resultado == 0:
                print(sell.fita_out)
                print('Rejeitado\n')
                texto.append(fita + ';0')
            arquivo = open('saida.out', 'w')
            arquivo.writelines(texto)
            arquivo.close()

    def verifica_e_final(self, estado):
        for x in self.e_final:
            if (x == estado):
                return True
        return False


if __name__ == '__main__':

    instructions = {
        (0, '0'): ('1', Move.Right, 0),
        (0, '1'): ('0', Move.Right, 0),
        (0, None): ('', Move.Right, 1),
        (1, None): ('1', Move.Stay, 2)
    }

    m = MaquinaTuring(list('0110100'), instructions)
    for x in m:
        print(x)






