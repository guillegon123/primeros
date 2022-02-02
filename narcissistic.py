def narcissistic(n):
    digits = len(n)
    acum = 0
    for num in n:
        acum = int(num)**digits + acum
    if acum == int(n):
        return True
    else:
        return False

def run():
    n = input("Escribe un número entero: ")
    print(narcissistic(n))



if __name__ =="__main__":
    run()