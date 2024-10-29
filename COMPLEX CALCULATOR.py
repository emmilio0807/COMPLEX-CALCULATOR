
#esta es una calculadora de operaciones basicas entre dos numeros complejos


print("\n ^_^ COMPLEX CALCULATOR ^_^ \n \n LAS ENTRADAS DEBEN SER ESCRITAS CON EL SIGUIENTE ORDEN: a+bj \n")

#declaracion de variables
A = complex(input("\n Ingresa el primer numero complejo: "))
B = complex(input("\n Ingresa el segundo numero complejo: "))

#la siguiente variable define el comportamiento del programa
operation = input("\n Indica la operacion que deseas realizar: suma(s)-resta(r)-multiplicacion(m)-division(d): ")

if operation == "s":
    def sum():                  #creacion de la funcion                 
        print(f"\n Resultado: {A+B}")
    sum()

elif operation == "r": 
    def rest():                 #creacion de la funcion resta
        print(f"\n Resultado: {A-B}")
    rest()

elif operation == "m":    
    def mult():                 #creacion de la funcion multiplicacion
        print(f"\n Resultado: {A*B}")
    mult()

elif operation == "d":
    def div():                  #creacion de la funcion division
        print(f"\n Resultado: {A/B}")
    div()
                            
else: 
    print("\n Operacion invalida o inexistente")    #esta condicion se ejecuta si se ingresa una entrada no esperada para este programa

input("\n \n Secuencia finalizada, presione enter para cerrar esta ventana")
