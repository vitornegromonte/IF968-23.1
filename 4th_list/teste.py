def notacao_posFixada(expressao):
    pilha = []
    
    for caractere in expressao: # percorre todos os caracteres do input
        
        if caractere.isdigit(): # verifica se o caractere é numérico, se for, transforma em inteiro e adiciona na lista
            pilha.append(int(caractere))
        else:
            operando_1 = pilha.pop()
            operando_2 = pilha.pop()
            
            # como o caractere não é numérico, testamos a qual operação ele corresponde
            if caractere == '+':
                pilha.append(operando_1 + operando_2)
                
            elif caractere == '-':
                pilha.append(operando_1 - operando_2)
                
            elif caractere == '*':
                pilha.append(operando_1 * operando_2)
                
            elif caractere == '/':
                pilha.append(operando_1 / operando_2)
    
    return pilha[0] # retornando o valor que está no topo da pilha

def numero_perfeito(n):
    if n <= 0: # se o número é negativo ele não é um número perfeito
        return False
    else:
        # percorre todos os números no intervalo entre 1 e n - 1
        # testa se o resto da divisão de n pelo número é 0, se for, adiciona na soma e confirma se a soma é igual ao valor de n
        soma_divisores = sum( i for i in range(1,n) if n % i == 0) 
        return soma_divisores == n

def ascii_decoder():
    palavra_decodificada = ''

    while True:
        expressao = []
        while True:
            entrada = input()
            if entrada == '':
                break
            elif entrada == 'Todas as expressoes foram enviadas!':
                return palavra_decodificada

            # Mova a chamada strip().split() para dentro do loop
            expressao += entrada.strip().split()

        binario = ''
        for caractere in expressao:
            resultado = notacao_posFixada(caractere)

            if resultado is not None and numero_perfeito(int(resultado)):  # Remove o "resultado is"
                binario += '1'
            else:
                binario += '0'

        expressao_ascii = chr(int(binario, 2))  # Move a conversão para int() para dentro de chr()
        palavra_decodificada += expressao_ascii

palavra_decodificada = ascii_decoder()
print(palavra_decodificada)