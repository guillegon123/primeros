def num_primo(numero):
     # n-1! +1 %==0 si cumple esto es primo
    if numero != 1 :
        factorial= 1
        for i in range(2,numero):
            factorial = factorial *i
        factorial += 1
        if factorial% numero == 0:
            return True
        else:
            return False 
    else:
        return True        


def run():
    numero = int(input("Escriba un número: "))
    if num_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()