numero = 0 #MUDE AQUI O NUMERO A SER PROCURADO
fib = 0
fib_atual = 1


while(numero > fib_atual):
    holder = fib_atual
    fib_atual = fib+fib_atual
    fib = holder

print(str(numero) + " pertence a sequência") if (numero == fib_atual or numero == 0) else print(str(numero) + " não pertence a sequência")
