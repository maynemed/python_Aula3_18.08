qtf= 0
qtm= 0

for i in range(3):
    nome = input("Digite o nome do cliente:")
    sexo = input("Digite o sexo do cliente (F PARA FEMININO OU M PARA MASCULINO):")

    if sexo == "F":
        qtf+= 1
    elif sexo == "M":
        qtm+= 1
    else:
        print ("DIGITE F PARA FEMININO OU M PARA MASCULINO!")

print (f"Quantidade de homens: {qtm} - Quantidade de mulheres: {qtf}")