import src.dados_atuais
import src.dados_previsao
import sys

print("*******************************************************************************************")
print("Você está no ambiente de análise de dados da área de marketing digital empresa Freeks Corp ")
print("*******************************************************************************************")

while True:
    escolha = int(input("Deseja analisar os dados atuais ou a previsão do mês seguinte?\
                         \nDADOS ATUAIS[1]  PREVISÃO[2]  SAIR[3]\n"))

    while escolha == 1 or escolha == 2:
        if escolha == 1:
            src.dados_atuais.mostrar()
        elif escolha == 2:
            src.dados_previsao.mostrar()

        opcao = input("Ainda deseja analisar os dados?\nOpções: [S] Sim [N] Não\n").lower()
        while opcao != "s" and opcao != "n":
            opcao = input("Opção inválida. Por favor, digite 'S' para continuar ou 'N' para sair.\n").lower()

        if opcao == "n":
            print("Obrigado por utilizar o programa. Até a próxima!")
            sys.exit(0)
            
        while True:
            escolha = int(input("Deseja analisar os dados atuais ou a previsão do mês seguinte?\
                                \nDADOS ATUAIS[1]  PREVISÃO[2]  SAIR[3]\n"))
            if escolha == 1 or escolha == 2 or escolha == 3:
                escolha = int(escolha)
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

    if escolha == 3:
        print("Obrigado por utilizar o programa. Até a próxima!")
        sys.exit(0)

    print("Opção inválida. Por favor, digite '1', '2' ou '3'.\n")
