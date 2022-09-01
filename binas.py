#binário só que sem o (bin) 

def dec_para_binario(decimal):
    binario = ""
    while decimal > 0:
        binario+=str(decimal%2)
        decimal=decimal//2
    return binario[::-1]
        
if __name__ == '__main__':
	num = int(input("Digite um número:"))
	print("O número em binário é: "+dec_para_binario(num))        


