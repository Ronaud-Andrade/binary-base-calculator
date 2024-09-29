from os import system
system('cls') #Clean the terminal on windows

print("PT-BR: Esse programa é um conversor de bases")
print("EN: This program is a base converter")
convert = input("Qual a base que vc quer converter? ex.: Bin; Dec; Oct; Hex.  ")
valor = input("Enter a value: ")
valor_characters = len(valor) #Number of characters
base = str(input("Enter the base you want to convert: Ex.: Bin; Dec; Oct; Hex.  "))
base = base.lower() #Transforming the string into lowercase
array = []
if(base == "bin"):
    if("2" in valor):
        print("Binario é somente '1' e '0'")
    else:
        #casting
            valor = int(valor)
            #loop
            while(valor > 0 or valor > 1):
                valor_inteiro = valor // 2 #4/2 = 2
                valor_resto = valor % 2 #4mod2 = 0
                #print(valor_resto, end="")
                array.append(valor_resto)
                #print(array)
                valor = valor_inteiro
        
            for i in range(len(array)):
                print(array[-1-i], end="")

elif(base == "oct" and convert == "bin"):
    if("2" in valor):
        print("Binario é somente '1' e '0'")
    else:
        valor_dec = 0
        #casting
            #Convertendo para decimal
        for i in range(valor_characters):
            valor_dec += (int(valor[-1-i]))*(2**i)
            
        if(i == valor_characters - 1):
            print(f"Converção para decimal: {valor_dec}", end="\n")
        else:
            print(f"Converção para decimal: {valor_dec}", end="")
                
        #Converter para octal       
        valor_dec = int(valor_dec)
        while((valor_dec) > 0 or (valor_dec) > 1):
            valor_inteiro = valor_dec // 8 
            valor_resto = valor_dec % 8
            #print(valor_resto, end="")
            array.append(valor_resto)
            #print(array)
            valor_dec = valor_inteiro
            
        for i in range(len(array)):
            print(array[-1-i], end="")

elif(base == "dec"): 
    valor_dec = 0
    #loop
    for i in range(valor_characters):
        valor_characters += -1
        #print(valor[int(valor_characters)])
        
        valor_dec += int(valor[valor_characters])*(2**i)
    print(valor_dec)
else: print("Unknown function")