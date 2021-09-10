#inicio_exe1.py
from exe1lpg import ObjEXE_LPG01
print('DIGITE O NÚMERO DA QUASTÃO QUE DESEJA ACESSAR')
print(' '*3,'QUESTÃO', ' '*8,'DIGITE')
print(' '*4,'EXE01', ' '*12,'1')
print(' '*4,'EXE02', ' '*12,'2')
print(' '*4,'EXE03', ' '*12,'3')
print(' '*4,'EXE04', ' '*12,'4')
print(' '*4,'EXE05', ' '*12,'5')
print(' '*4,'EXE06', ' '*12,'6')
print(' '*4,'EXE07', ' '*12,'7')
print(' '*4,'EXE08', ' '*12,'8')
print(' '*4,'EXE09', ' '*12,'9')
print(' '*4,'EXE10', ' '*12,'10')
print(' '*4,'EXE10.1', ' '*10,'10.1')

while True:
    ex = input('DIGITE O CÓDIGO OU S PARA SAIR: ')
    if ex in "Ss":
        print('FIM!')
        break
    if ex == "1":
        ex = ObjEXE_LPG01.exe01()
        continue
    elif ex == "2":
        ex = ObjEXE_LPG01.exe02()
        continue
    elif ex == "3":
        ex = ObjEXE_LPG01.exe03()
        continue
    elif ex == "4":
        ex = ObjEXE_LPG01.exe04()
        continue
    elif ex == "5":
        ex = ObjEXE_LPG01.exe05()
        continue
    elif ex == "6":
        ex = ObjEXE_LPG01.exe06()
        continue
    elif ex == "7":
        ex = ObjEXE_LPG01.exe07()
        continue
    elif ex == "8":
        ex = ObjEXE_LPG01.exe08()
        continue
    elif ex == "9":
        ex = ObjEXE_LPG01.exe09()
        continue
    elif ex == "10":
        ex = ObjEXE_LPG01.exe10_1()
        continue
    elif ex == "10.1":
        ex = ObjEXE_LPG01.exe10_2()
        continue
