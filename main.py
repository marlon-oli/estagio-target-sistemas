import json

def main():
    # RESPOSTA DA PERGUNTA 1:
    print("EX1:")
    ex1()

    # definindo o numero do parametro como numero a ser procurado
    print("\nEX2:")
    ex2(7)

    # arquivo fontedados.json utilizado como fonte de dados
    print("\nEX3:")
    ex3()

    # definindo a lista do exercicio 4
    print("\nEX4:")
    listaFaturamento = [("SP", 67836.43), ("RJ", 36678.66), ("MG", 29229.88), ("ES", 27165.48), ("Outros", 19849.53)]
    ex4(listaFaturamento)

    # definindo texto a ser invertido
    print("\nEX5:")
    texto = "Texto a ser invertido!"
    print(ex5(texto))

    return 0

#FUNCOES RESPOSTA DAS QUESTOES

# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

def ex1():
    indice = 13
    soma = 0
    k = 0

    while (k < indice):
        k = k + 1
        soma = soma + k

    print(soma)


# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

# usando o parametro x como o numero a ser buscado
def ex2(x):
    i = 0
    j = 1

    while (j <= x):
        i, j = j, i + j

    if (i == x):
        print(x, "pertence a sequencia de fibonacci.")
    else:
        print(x, "nao pertence a sequencia de fibonacci.")

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

def ex3():
    with open('fontedados.json', 'r') as file:
        dados = json.load(file)

    for mes in dados['meses']:
        resultados = calcular_faturamento(mes)
        print(f"Mes: {resultados['mes']}")
        print(f"Menor valor de faturamento: R${resultados['menor_faturamento']:.2f}")
        print(f"Maior valor de faturamento: R${resultados['maior_faturamento']:.2f}")
        print(f"Numero de dias com faturamento acima da media mensal: {resultados['dias_acima_da_media']}")

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

def ex4(lista):
    faturamentoTotal = 0

    for _,i in lista:
        faturamentoTotal += i

    print("Percentual de representacao de cada estado: \n")

    for est, fat in lista:
        percentual = (fat/faturamentoTotal)*100
        print(f'{est}: {percentual:.2f}%')

# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def ex5(texto):
    texto_invertido = texto[::-1]
    return texto_invertido

# FUNCAO AUXILIAR PARA CALCULAR FATURAMENTO
def calcular_faturamento(mes):
    faturamentos = [dia['faturamento'] for dia in mes['dias'] if dia['faturamento'] > 0.0]

    if faturamentos:
        menor_faturamento = min(faturamentos)
        maior_faturamento = max(faturamentos)
        media_mensal = sum(faturamentos) / len(faturamentos)
        dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

        return {
            "mes": mes["mes"],
            "menor_faturamento": menor_faturamento,
            "maior_faturamento": maior_faturamento,
            "dias_acima_da_media": dias_acima_da_media
        }
    else:
        return {
            "mes": mes["mes"],
            "menor_faturamento": None,
            "maior_faturamento": None,
            "dias_acima_da_media": 0
        }

if __name__ == '__main__':
    main()