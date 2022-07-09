continuar = True
fib = []
fib.append(0)
fib.append(1)

entrada = 10946 # MUDE AQUI O VALOR A SER PROCURADO

if( entrada in fib ):
    print(True)

else:
    while continuar:
        if(len(fib) == 2):
            fib.append(fib[0] + fib[1])
        
        else:
            fib[0] = fib[1]
            fib[1] = fib[2]
            fib[2] = fib[0] + fib[1]
            print(fib[2])
            if(fib[2] >= entrada):
                continuar = False

    if(entrada == fib[2]):
        print(True)
    else:
        print(False)