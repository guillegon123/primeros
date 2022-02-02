def run():
    contador=15000
    while contador >0:
        contador -= 1
        if contador%5 != 0:
            continue
        elif contador == 500:
            break
        print(contador)
        


if __name__ =="__main__":
    run()