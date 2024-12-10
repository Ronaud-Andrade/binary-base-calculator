from os import system
system('cls') #Clean the terminal on windows

print("PT-BR: Esse programa é um conversor de bases")
print("EN: This program is a base converter")
valor = input("Enter a value: ")
valor_characters = len(valor) #Number of characters
base = str(input("Enter the base you want to convert: Ex.: Bin; Dec. "))
base = base.lower() #Transforming the string into lowercase
array = []
valor_dec = 0
if(base == "bin"):
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
                    
elif(base == "dec"): 
    #loop
    for i in range(valor_characters):
        valor_characters += -1
        #print(valor[int(valor_characters)])
        
        valor_dec += int(valor[valor_characters])*(2**i)
    print(valor_dec)
else: print("Unknown function")