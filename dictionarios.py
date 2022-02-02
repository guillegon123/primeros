def run():
    mi_diccionario ={
        "llave_1": 1,
        "llave_2": 2,
        "llave_3": 3,    
    }
    # print(mi_diccionario["llave_1"])
    # print(mi_diccionario["llave_2"])
    # print(mi_diccionario["llave_3"])

    poblacion_paises = {
        "Argentina": 44938712,
        "Brazil": 21047125,
        "Colombia": 50372424
    }
    # print(poblacion_paises["Argentina"])
    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #      print(pais)
    for pais,poblacion in poblacion_paises.items():
        print("El país "+ pais + " tiene " + str(poblacion) + " de habitantes")

if __name__ == "__main__":
    run()