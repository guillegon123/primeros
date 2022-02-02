def get_count(sentence):
    return sum(1 for letra in sentence if letra in "aeiouAEIOU") # Una forma de hacerlo mucho mas facil
    # contador = 0
    # for letra in sentence:
    #     if letra == 'a':
    #         contador += 1
    #     elif letra == 'e':
    #         contador += 1
    #     elif letra == 'i':
    #         contador += 1
    #     elif letra == 'o':
    #         contador += 1
    #     elif letra == 'u':
    #         contador += 1
    # return contador

def run():
    sentence = input("Escriba una frase: ")
    print(get_count(sentence))

if __name__ == "__main__":
    run()
