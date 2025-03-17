# Testando o código
valor = int(input("Digite o valor do saque: R$ "))

notas_disponiveis = [100, 50, 20, 10]  # Prioridade para as notas maiores
resultado = {}

for nota in notas_disponiveis:
    if valor >= nota:
        quantidade = valor // nota  # Calcula quantas notas desse valor podem ser usadas
        valor = valor - (quantidade * nota)  # Atualiza o valor restante
        resultado[nota] = quantidade  # Armazena a quantidade de cada nota usada

if valor == 0:
    print("\nNotas entregues:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de R$ {nota},00")
else:
    print("\nErro: Valor inválido para saque. Tente um múltiplo de 10.")
