from aposta import limpar_apostas, registrar_aposta, mostrar_apostas, apostas
from sorteio import sortear_numero, mostrar_ganhadores

def mostrar_menu():
    opcao = None
    while opcao != 3:
        print("""
        Bem vindo ao Jogo do Bicho

           9
     ,--.-'-,--.
     \  /-~-\  /
    / )' a a `( \\
   ( (  ,---.  ) )
    \ `(_o_o_)' /
     \   `-'   /
      | |---| |   
      [_]   [_]

        Selecione a opção desejada:
        1 - Fazer Aposta 
        2 - Gerar sorteio
        3 - Sair da aplicação
        """)

        opcao = int(input(''))

        if opcao == 1 : 
            registrar_aposta()
            
        elif opcao == 2: 
            mostrar_apostas()
            mostrar_ganhadores(apostas, sortear_numero(2))
            limpar_apostas()

        elif opcao == 3:
            pass
            #sai da aplicação
        else: 
            pass
            #mensagem de opção invalida
