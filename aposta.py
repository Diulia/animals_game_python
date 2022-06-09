from datetime import datetime
apostas = []

def registrar_aposta():
    numero_aposta = int(input('Informe o número: '))
    valor_aposta = float(input('Informe o valor da aposta: '))
    aposta = {
        "numero":numero_aposta, 
        "valor":valor_aposta
    }
    apostas.append(aposta)
    imprimir_comprovante(numero_aposta, valor_aposta)

def imprimir_comprovante(numero, valor):
    data = datetime.now()
    data_formatada = '{}/{}/{} {}:{}'.format(data.day, data.month, data.year, data.hour, data.minute)
    print("""
    ============={}=============== 
    | Número apostado: {} 
    | Valor apostado: {} 
    ======================================
    """.format(data_formatada, numero, valor))

def mostrar_apostas():
    print('Foram feitas {} apostas' .format(len(apostas)))

def obter_montante():
    # apostas [{"numero": 1, "valor": 2,50}, {"numero": 25, "valor": 14}]
    valor_obtido = 0
    for aposta in apostas:
        valor_obtido = valor_obtido + aposta["valor"]
    return valor_obtido    

def limpar_apostas():
    apostas.clear()