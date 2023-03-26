print("*******************************************************************************************")
print("Você está no ambiente de análise de dados da área de marketing digital empresa Freeks Corp ")
print("*******************************************************************************************")
import src.dados_atuais
import src.dados_previsao

while True:
    escolha = int(input("Deseja analisar os dados atuais ou a previsão do mês seguinte?\
                    \nDADOS ATUAIS[1]  PREVISÃO[2]"))
    
    while escolha == 1 or escolha == 2:

        while True: 
            if (escolha == 1):
                src.dados_atuais.mostrar()
                break 
            elif (escolha == 2):
                src.dados_previsao.mostrar()
                break
        break
    else:
        print('Digite apenas 1 ou 2, por favor.')