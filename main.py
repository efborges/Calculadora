print ("Para utilizar a calculadora escolha a opção de cálculo desejada utilizando o número correspondente.")

print()

versão = 1.0
status = 1

print("Versão do projeto: ", versão)

print()

while status == 1:
    print("(1) Soma")
    print("(2) Subtração")
    print("(3) Multiplicação")
    print("(4) Divisão")

    print()

    resp_cru = input ("Digite a opção desejada: ")

    def trata_resp(resp_cru):
        respostas_validas = ["1", "2", "3", "4"]
    
        if resp_cru in respostas_validas:   
            resp_tratada = int(resp_cru)
            return resp_tratada
        else:
            print("Opção Desconhecida")

    trata_resp(resp_cru)