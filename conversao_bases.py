#Recodificando o código

def menu():
    _ = "+" * 30

    print(
        f"{_} \n"
        "Bem-vindo \n"
        "Esse código é um conversor de bases númericas \n"
        f"{_} \n"
    )

def main():

    while(True):
        menu()
        base_principal = str(input("Digite a base númerica (Ex.: Dec, Bin, Oct, Hex) -> ")).capitalize()
        base_converter = str(input("D1igite a base númerica para qual quer converter -> ")).capitalize()
        print()
        valor_digitado = str(input("Digite o valor: "))
        #to_dec(valor_digitado)
        #print(valor_digitado[::-1])
        if(base_principal == "Dec"):
            if(base_converter == "Bin"):
                #Converter para Binario
                pass
            elif(base_converter == "Oct"):
                #Converter para Octal
                pass
            elif(base_converter == "Hex"):
                #Converter para Hexadecimal
                pass
            else: print("Operação desconhecida")
        elif(base_principal == "Bin"):
            if(base_converter == "Dec"):
                #Converter para Decimal
                print(f"Valor em decimal: {to_dec(valor_digitado)}")
                pass
            elif(base_converter == "Oct"):
                #Converter para Octal
                x = to_dec(valor_digitado)
                y = to_oct(x)

                print("Valor em octal: ", end="")
                for i in range(len(y)):
                    print(y[-1-i], end="")
                print()
                pass
            elif(base_converter == "Hex"):
                #Converter para Hexadecimal
                pass
            elif(base_principal == "Oct"):
                pass      
            else: print("Operação desconhecida")         
        elif(base_principal == "Oct"):
            if(base_converter == "Dec"):
                #Converter para Decimal
                pass
            elif(base_converter == "Hex"):
                #Converter para Hexadecimal
                pass
            elif(base_converter == "Bin"):
                #Converter para Binario
                pass
            else: print("Operação desconhecida")
        else: print("Operação desconhecida")

        esc = str(input("Caso queria encerrar, digite: [Y/N] -> "))

        if(esc == "Y"):
            print()
            print("OK! Adeus.")
            print()
            break
        elif(esc == "N"):
            print()
            print("OK!")
            print()

def to_dec(valor):

    

    count = 0
    valor_contrario = []
    for i in range(len(valor)):
        valor_contrario.append(valor[-1-i])

    for j in range(len(valor_contrario)):
        count += (int(valor_contrario[j]) * (2**j))
    
    return count

    

def to_bin(valor):
    numero_bin = []
    valor = int(valor)
    while(valor > 0):
        resto = valor % 2
        valor = valor // 2
        numero_bin.append(resto)


def to_oct(valor):
    numero_oct = []
    while(valor > 0):
        resto = valor%8
        valor = int(valor // 8)
        numero_oct.append(resto)
    
    return numero_oct

def to_hex(valor):
    pass


main()