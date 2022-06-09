from random import choice, random
from aposta import obter_montante

def sortear_numero(quantidade_digito)-> int:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultado = []
    for i in range(quantidade_digito):
        numero_escolhido = str(choice(numeros))
        resultado.append(numero_escolhido)
    return int(''.join(resultado))

def mostrar_ganhadores(apostas, resultado):
    ganhadores = 0
    for aposta in apostas:
        if aposta["numero"] == resultado : 
            ganhadores = ganhadores + 1
    valor_apostas = obter_montante()
    print("""
    O valor total do concurso foi de {}.
    O número sorteado foi {} e houveram {} ganhadores.
    """.format(valor_apostas, resultado, ganhadores))
