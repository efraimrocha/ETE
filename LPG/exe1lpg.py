#exe01lpg.py
#1
class EXE_LPG01:
    def exe01(self):
        nome = str(input('Qual é o seu nome? \n'))
        anonasc = int(input('Digite o ano em que você nasceu? '))
        anoatual = int(input('Informe o ano atual: \n'))
        idade = anoatual - anonasc
        if (idade >= 18):
            return print(f'{nome}, sua entrada foi permitida.')
        else:
            return print(f'{nome}, sua entrada não foi permitida.')
#2
    def exe02(self):
        n = int(input('Digite um número:\n '))
        if (n % 2) == 0:
            return print(f'{n} é par.')
        else:
            return print(f'{n} é ímpar.')
#3
    def exe03(self):
        salario = float(input('Digite o valor do salário: '))
        prestacao = float(input('Digite um valor para a prestação: '))
        porcento = (salario * 20) / 100
        if prestacao <= porcento:
            return print('Empréstimo poderá ser concedido')
        else:
            return print('Empréstimo não poderá ser concedido')
#4
    def exe04(self):
        n = float(input('Digite um número: '))
        if (n == 20):
            return print(f'O número digitado {n} é igual a 20.')
        elif (n > 20):
            return print(f'O valor digitado {n} é maior que 20.')
        elif (n < 20):
            return print(f'O valor digitado é menor que 20.')
        else:
            return print('Digite um número válido')
#5
    def exe05(self):
        a = int(input('Digite um número: '))
        b = int(input('Digite um segundo número: '))
        c = int(input('Digite um terceiro número: '))
        n = ()
        if (a >= b):
            n = a
        else:
            n = b
        #print(n)
        if (n >= c):
            return print(f'{n} é o maior dos números digitados')
        else:
            return print(f'{c} é o maior dos númeors digitados')
#6
    def exe06(self):
        na = int(input('Digite um valor para NumA: '))
        nb = int(input('Digite um valor para NumB: '))
        nc = na
        return print(f'NumA = {nb} e NumB = {nc}')
#7
    def exe07(self):
        n1 = float(input('Digite um número: \n'))
        n2 = float(input('Digite outro número: \n'))
        if (n1 == n2):
            return print('Os números digitados são iguais!')
        else:
            return print('Os números digitados são diferentes!')
#8
    def exe08(self):
        valor = float(input('Dgite o valor da velocidade que deseja converter: \n'))
        tipo = str(input('\n   [k] Converter para km/h\n   [m] Coverter para m/s\n'))
        tipo = tipo.upper()
        if (tipo == 'K'):
            return print('{:.1f} Km/h'.format(valor*3.6))
        elif (tipo == 'M'):
            return print('{:.1f} m/s'.format(valor/3.6))
        else:
            return print('Digite uam opção válida')
#9
    def exe09(self):
        salario = float(input('Digite o valor do salário: \n'))
        sm = salario // 1100 # reotna apenas a parte interia da divião
        return print('{} = {} SM.'.format(salario, sm))
        #print('{} = {:.1f} SM.'.format(salario, sm))
#10 v1.0
    def exe10_1(self):
        produto = str(input('Nome do produto 1: '))
        valor = float(input('Valor do produto 1: '))
        qt = int(input('Digite a quantidade: '))
        produto2 = str(input('Nome do produto 2: '))
        valor2 = float(input('Valor do produto 2: '))
        qt2 = int(input('Digite a quantidade: '))
        produto3 = str(input('Nome do produto 3: '))
        valor3 = float(input('Valor do produto 3: '))
        qt3 = int(input('Digite a quantidade: '))
        list1 = [produto, valor, qt]
        list2= [produto2, valor2, qt2]
        list3 = [produto3, valor3, qt3]
        total = (valor*qt) + (valor2*qt2) + (valor3*qt3)
        print(f'{list1}\n{list2}\n{list3}\n Toal = R$ {total}')
        pagamento = float(input('Informe quanto em valor irá pagar: \n'))
        troco = pagamento - total
        if not (troco == 0):
            return print(f'Seu troco será R$ {troco}')
        else:
            return print('Obrigado pela prefereência')
#10 v2.0 - Correção da anterior, usando a função while 
    def exe10_2(self):
        total = 0
        iten = 0
        while True:
            print('[s] para sair ou [t] para total')
            produto = input('NOME DO PRODUTO OU S PARA SAIR: ')
            if produto in "Ss":
                print('FIM!')
                break
            qt = float(input('QUANTIDADE: '))
            valor = float(input('VALOR UNITÁRIO: '))    
            lista = [produto, qt, valor]

            if produto in "Tt":        
                total_produto = qt * valor
                total = total + total_produto
                print(f'{iten}, {lista}\nR$ {total}')
            else:
                total_produto = qt * valor
                total = total + total_produto
                iten += 1
                print(f'ITEM {iten}, {lista}\nR$ {total}')
                continue
        pago = float(input("PAGAMENTO: "))
        ativo = True
        while ativo:
            if pago < total:
                pago = float(input("PAGAMENTO: "))
                continue
            elif pago >= total:
                if pago == total:
                    return print('MUITO OBIGADO - VOLTE SEMPRE')
                    break
                else:
                    troco = pago - total
                    return print(f'TROCO R$ {troco}')
                    break
ObjEXE_LPG01 = EXE_LPG01()
