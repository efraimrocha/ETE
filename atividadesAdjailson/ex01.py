
class Atividade01():
    def Exe01(self):
        consumo = float(input("Digite seu consumo em kw/h: "))
        tarifa_verde = 0.9
        tarifa_amarela = 1.874
        tarifa_vermelha = 3.971
        ad_kw = consumo - 100.0

        if consumo > 100:
            consumo_amarelo = (ad_kw * tarifa_amarela) + 90
            consumo_vermelho = (ad_kw * tarifa_vermelha) + 90
            print(f'O valor do consumo será:\nBandeira AMARELA - R$ {consumo_amarelo}\nBandeira VERMELHA - R$ {consumo_vermelho} ')
        elif 0 <= consumo <= 100:
            consumo_verde = consumo * tarifa_verde
            print(f'O valor do consumo será: R$ {consumo_verde}')
        else:
            print("Informe um valor real. ")
        return

    #2 

    def Exe02(self):
        valor_gasolina = float(input('Digite o valor da gasolina: '))
        kml = float(input('Quantos km seu por litro? '))
        km_viagem = float(input('Informe quantos km irá pecorrer: '))

        consumo_carga_totalVoltz = (5 * 2.4) * 0.9
        km_carga_totalVoltz = 120
        vm_mediaVoltz = 35


        def consumo_gasolina():
            qt_litros = km_viagem/kml
            total_gasolina = qt_litros*valor_gasolina
            round_total_gasolina = round(total_gasolina, 2)
            return round_total_gasolina


        def consumo_voltz():
            custo_cagacompleta = (5 * 2.4) * 0.9
            custo_km = custo_cagacompleta / km_carga_totalVoltz
            consumo_voltz = km_viagem * custo_km
            round_consumo_voltz = round(consumo_voltz, 2)
            return round_consumo_voltz

        print("R$", consumo_gasolina() ,'será o valor da viagem usando gasolina.','\nR$', consumo_voltz() ,'será o valor da viagem usano a Voltz.')

    #3 
    def Exe03(self):
            print('Cédulas disponíveis: 100, 50, 20 e 10')
            saque = int(input('Digite o valor do saque: '))
            total = saque
            cedula = 100
            total_cedula = 0

            while True:
                if total >= cedula:
                    total -= cedula
                    total_cedula += 1
                else:
                    if total_cedula > 0:
                        print(f'{total_cedula} de R$ {cedula}')
                    if cedula == 100:
                        cedula = 50
                    elif cedula == 50:
                        cedula = 20
                    elif cedula == 20:
                        cedula = 10
                    elif cedula == 10:
                        cedula = 5
                    total_cedula = 0
                    if total == 0:
                        return saque


ObjAtividade01 = Atividade01()
