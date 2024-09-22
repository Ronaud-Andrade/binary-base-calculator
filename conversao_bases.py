from os import system
system('cls') #Clean the terminal

print("PT-BR: Esse programa é um conversor de bases")
print("EN: This program is a base converter")
valor = input("Enter a value: ")
valor_characters = len(valor) #Number of characters
base = str(input("Enter the base you want to convert: Ex.: Bin; Dec. "))
base = base.lower() #Transforming the string into lowercase

valor_dec = 0
if(base == "bin"):
    #casting
        valor = int(valor)
        
        #loop
        while(valor > 0 or valor > 1):
            valor_inteiro = valor // 2 #4//2 = 2
            valor_resto = valor % 2 #4%2 = 0
            print(valor_resto)
            valor = valor_inteiro
print("The displayed value is inverted. Example: 001 -> 100 (Binary) = 4 (Decimal)")
            
if(base == "dec"):
    
    #loop
    for i in range(valor_characters):
        if(valor[i] == 1):
            valor_convertido = i*2
            valor_dec += valor_convertido
    print(valor_dec)


    