import TuringMachine
import os

if __name__ == '__main__':
    mt = TuringMachine.MaquinaTuring('C:\\Users\\laris\\Desktop\\turing\\duplobal.mt',
                                     'C:\\Users\\laris\\Desktop\\turing\\duplobal.in')
    mt.process_arquivo()
    os.system("Pause")