def squareeverydigit(n):
    list = []
    list_2 = []
    for num in n:
        list.append(int(num))
    for i in list:
        list_2.append(str(i**2))
    list_2 = ''.join(list_2)
    return list_2
def run():
    n = input("Escribe un número entero: ")
    print (squareeverydigit(n))

if __name__ =="__main__":
    run()