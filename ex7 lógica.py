n1 = int(input())
n2 = int(input())
opcao = int(input('Escolha a opção 1,2,3 ou 4: '))

if opcao == 1:
    media = (n1+n2) /2
    print(media)
elif opcao == 2:
    diferenca = n1-n2
    print(diferenca)
elif opcao == 3:
    produto = n1*n2
    print(produto)
elif opcao == 4:
    divisao = n1/n2
    print(f'divisao = {divisao:.2f}')
else:
    print("Opção inválida")
