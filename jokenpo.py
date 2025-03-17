# Criação das logicas para o Jokenpo
player_one = input('Digite o Nome do Player 1: ')
player_two = input('Agora o nome do player 2: ')

print('Hora do game!')
print('Primeiro o player um deve escolher entre pedra, papel ou tesoura')

play_one = input(f'Digite sua jogada {player_one}: ')
play_two = input(f'Agora é a vez do {player_two}: ')

print('Preparen-se o resultado já vai chegar!')

empate = (play_one == play_two)

player_one_winner = (play_one == 'pedra' and play_two == 'tesoura') or \
                    (play_one == 'tesoura' and play_two == 'papel') or \
                    (play_one == 'papel' and play_two == 'pedra')

player_two_winner = player_one_winner == False and empate == False

if empate:
    print('Opa, tivemos um empate!')
    print(f'{player_one} escolheu {play_one} e o {player_two} escolheu {play_two}')
    print('Isso resultou em um empate!')
elif player_one_winner:
    print(f'O {player_one} é o vencedor!')
    print(f'sua jogada foi: {play_one} enquanto a jogada de {player_two} foi {play_two}')
    print(f'isso resultou na vitória de {player_one}')
else:
    print(f'O {player_two} é o vencedor!')
    print(f'sua jogada foi: {play_two} enquanto a jogada de {player_one} foi {play_one}')
    print(f'isso resultou na vitória de {player_two}')