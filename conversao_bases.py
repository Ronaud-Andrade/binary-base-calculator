print("Esse programa é um conversor de bases")
valor = input("Digite um valor: ")
valor_characters = len(valor)
base = str(input("Digite qual é a base que deseja converter: Ex.: Bin; Dec. (Sem acentos) "))
base = base.lower()

valor_dec = 0
if(base == "bin"):
    #casting
        valor = int(valor)
        while(valor > 0 or valor > 1):
            valor_inteiro = valor // 2 #4/2 = 2
            valor_resto = valor % 2 #4mod2 = 0
            print(valor_resto)
            valor = valor_inteiro
            
if(base == "dec"):
    
    for i in range(valor_characters):
        if(valor[i] == 1):
            valor_convertido = i*2
            valor_dec += valor_convertido
    print(valor_dec)


    