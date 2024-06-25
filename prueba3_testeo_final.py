cargos = ["ceo", "desarrollador", "analista de datos"]
empleados = []
list_analista = []
list_desarolla= []
list_ceo= []

def numeros(a):
    return "{:,}".format(a).replace(",", ".")
    
def menu_principal():    
    while True:
        print("="*20, "Menú Principal", "="*20)
        print("1. Registrar trabajador")
        print("2. Listar los todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("0. Salir del Programa")
        try:
            op_menu_p = int(input("Elija una opción ->"))
            if op_menu_p == 1:
                registro_user()
            elif op_menu_p == 2:    
                if empleados == []:
                    print("No hay trabajadores registrados aún.")        
                else:
                    lista_trabajadores()
            elif op_menu_p == 3:
                if empleados == []:
                    print("No hay trabajadores registrados aún.")
                else:                              
                    planilla_sueldos()
            elif op_menu_p == 0:
                print("Gracias por usar nuestro sistema.")
                break
            else:
                print("Opción no válida")
        except:
            print("Ingrese un valor valido")

def planilla_sueldos():    
    while True:
        print("==========Plantilla de sueldos==========")
        print("1. Imprimir todos los trabajadores")
        print("2. Imprimir todos los CEO")
        print("3. Imprimir todos los Desarrolladores")
        print("4. Imprimir todos los Analistas de Datos")
        print("0. Salir")
        try:
            op_planilla = int(input("Indique la opción deseada -> "))
            if op_planilla == 0:
                break
            elif op_planilla == 1:                
                imprimir(empleados)  
                break

            elif op_planilla == 2:
                imprimir(list_ceo) 
                break

            elif op_planilla == 3:
                imprimir(list_desarolla)  
                break

            elif op_planilla == 4:
                imprimir(list_analista)                 
                break

            else:
                print("Opción no válida")  
        except:
            print("Ingrese un valor valido")

def imprimir (a):
    if a == []:
        print("No hay trabajadores registrados en ese cargo")
    else:
        print("Lista impresa correctamente, volviendo al menu principal")
        with open("planilla.txt", "w") as archivo:
            archivo.write("Nombre, Cargo, Sueldo Bruto, Desc. Salud, Desc. AFP, Sueldo Liquido"+ '\n' )
            for i in a:
                archivo.write(f"{i[0].title()}, {i[1].title()}, ${numeros(i[2])}, ${numeros(i[3])}, ${numeros(i[4])}, ${numeros(i[5])}\n")

def registro_user():        
    while True:
        nombre= input("Ingrese nombre del trabajador-> ").lower()
        if nombre == "":
            print("Es necesario ingresar un nombre")
            break
        cargo = input("Ingrese el cargo del trabajador\n (CEO, Desarrollador o Analista de Datos) -> ").lower()
        if cargo not in cargos:
            print("El cargo debe corresponder a una de la opciones indicadas")  
            break                                              
        try:
            sueldo_bruto=int(input("Ingrese sueldo bruto del trabajador ->$"))
            if sueldo_bruto < 459999:
                print("El valor debe ser sobre el minimo legal")  
                break
        except:
            print("El valor debe ser númerico")
            break 

        salud = int(0.07 * sueldo_bruto)
        afp = int(0.12 * sueldo_bruto)
        liquido = sueldo_bruto - salud - afp
        empleados.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))   
        if cargo == "ceo":
            list_ceo.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))  
        elif cargo == "desarrollador":
            list_desarolla.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))   
        elif cargo == "analista de datos":
            list_analista.append((nombre, cargo, sueldo_bruto, salud, afp, liquido))
        print("Trabajador registrado Correctamente")       
        break

def lista_trabajadores ():
    for i in empleados:
        print(f"Nombre: {i[0].title()} // Cargo: {i[1].title()} // Sueldo Bruto: ${numeros(i[2])}")

menu_principal()  