def calnuevonum(n):
    numero = 1
    for num in n:
        numero=numero*int(num)
    return numero

def persiste(n):
    rondas = 0
    if len(n)>1:
        while len(n) >1:
            rondas +=1
            n = str(calnuevonum(n))
    return rondas

# import operator otra forma de hacerlo
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i

def run():
    n = input("Escribe un número entero: ")
    print(persiste(n))



if __name__ =="__main__":
    run()