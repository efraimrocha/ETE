
from ex01 import ObjAtividade01

print('Atividades 01 - Prof. Adjailson\n')

active = True

while active:
    print()
    print('=-'*29)
    print(' '*5,'ESCOLHA O NÚMERO DO EXERCÍCIO OU S PARA SAIR\n')
    print(' '*7,'[1] - Exercício 01 - Tarifa elétrica')
    print(' '*7,'[2] - Exercício 02 - Moto Voltz')
    print(' '*7,'[3] - Exercício 03 - Caixa eletrônico\n')
    print('-='*29)
    
    # Vê essa forma de usar o format
    
    print('=-'*22)
    print("{:<5}".format('ESCOLHA O NÚMERO DO EXERCÍCIO OU S PARA SAIR\n'))
    print("{:<7s}{:^15s}{:>22s}".format('[1]','- Exercício 01 -','Tarifa elétrica\n'))
    print("{:<7s}{:^15s}{:>22s}".format('[2]','- Exercício 02 -','Moto Voltz\n'))
    print("{:<7s}{:^15s}{:>22s}".format('[3]','- Exercício 03 -','Caixa eltrônico\n'))
          
    # sem o s o efeito é diferente. Esses símbolos < ^ > tem um signficado diferente.
    
    
    ex = input('DIGITE O NÚMERO DO EXERCÍCIO: ')
    if ex in "Ss":
        #print("FIM")
        active = False
    if ex == "1":
        ex = ObjAtividade01.Exe01()
    elif ex == "2":
        ex = ObjAtividade01.Exe02()
    elif ex == "3":
        ex = ObjAtividade01.Exe03()

