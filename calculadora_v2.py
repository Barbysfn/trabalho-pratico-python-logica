saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    op = operacao.lower()
    if op == '+' or op == 'adicao' or op == 'adição' or op == 'soma' or op == 'mais':
        return adicao(num1, num2)
    elif op == '-' or op == 'subtracao' or op == 'subtração' or op == 'menos':
        return subtracao(num1, num2)
    elif op == '*' or op == 'multiplicacao' or op == 'multiplicação' or op == 'vezes':
        return multiplicacao(num1, num2)
    elif op == '/' or op == 'divisao' or op == 'divisão' or op == 'dividido':
        return divisao(num1, num2)
    else:
        return "Operação inválida"

while saida.lower() != 'n':
    try:
        primeiro = float(input("Digite o primeiro número: "))
    except Exception:
        print("Entrada inválida. Usando 0 como primeiro número.")
        primeiro = 0.0

    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")
    
    try:
        segundo = float(input("Digite o segundo número: "))
    except Exception:
        print("Entrada inválida. Usando 0 como segundo número.")
        segundo = 0.0

    resultado = calculadora(primeiro, segundo, operacao)

    print("Resultado da operação:", resultado)

    saida = input("Deseja continuar? (S/N): ")
    if saida.lower() == 'n':
        print("Encerrando a calculadora. Até mais!")
