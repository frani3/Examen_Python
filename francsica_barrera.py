from os import system
from random import randint
from statistics import geometric_mean
system("cls")

menu="""
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas
4. Reporte de sueldos
5. Salir del programa
"""

trabajadores=["Juan Perez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_con_sueldo=[]
reporte_sueldos=[]
lista_sueldos=[]
cont_a=0
cont_b=0
cont_c=0
cont_d=0
prom=0
sueldo_a=0
sueldo_b=0
sueldo_c=0
sueldo_mayor=0
sueldo_menor=2500000


def asignar_sueldos(trabajadores, trabajadores_con_sueldo):
    for persona in trabajadores:
        sueldo=randint(300000,2500000)
        trabajador=[persona,sueldo]
        trabajadores_con_sueldo.append(trabajador)
    print("Sueldos Asignados!")

def clasificar_sueldos(trabajadores_con_sueldo, cont_a, cont_b, cont_c, sueldo_a, sueldo_b, sueldo_c):
    print(f"Sueldos menores a $800.000")
    print("Nombre empleado      Sueldo")
    for persona in trabajadores_con_sueldo:
        if persona[1]<=800000:
            cont_a+=1
            sueldo_a+=persona[1]
            print(f"{persona[0]}      ${persona[1]}")
    print(f"TOTAL: {cont_a}")
    print("-----------------------------------------------")
    print(f"Sueldos entre $800.000 y $2.000.000")
    print("Nombre empleado      Sueldo")
    for persona in trabajadores_con_sueldo:
        if persona[1]>=800000 and persona[1]<=2000000:
            cont_b+=1
            sueldo_b+=persona[1]
            print(f"{persona[0]}      ${persona[1]}")
    print(f"TOTAL: {cont_b}")
    print("-----------------------------------------------")
    print(f"Sueldos entre $800.000 y $2.000.000")
    print("Nombre empleado      Sueldo")
    for persona in trabajadores_con_sueldo:
        if persona[1]>2000000:
            cont_c+=1
            sueldo_b+=persona[1]
            print(f"{persona[0]}      ${persona[1]}")
    print(f"TOTAL: {cont_c}")
    print("-----------------------------------------------")
    print(f"TOTAL SUELDOS: ${sueldo_a+sueldo_b+sueldo_c}")

def estadisticas(trabajadores_con_sueldo, cont_d, prom, sueldo_mayor, sueldo_menor):
    for persona in trabajadores_con_sueldo:
        if persona[1]>sueldo_mayor:
            sueldo_mayor=persona[1]
        elif persona[1]<sueldo_menor:
            sueldo_menor=persona[1]
    for persona in trabajadores_con_sueldo:
        cont_d+=1
        prom+=persona[1]
    promedio=prom/cont_d
    for persona in trabajadores_con_sueldo:
        sueldos=persona[1]
        lista_sueldos.append(sueldos)
    print(f"Sueldo Mayor: {sueldo_mayor}")
    print(f"Sueldo Menor: {sueldo_menor}")
    print(f"Promedio de sueldos: {promedio}")
    print(f"Media geométrica: {geometric_mean(lista_sueldos)}")


def reporte_sueldos(trabajadores_con_sueldo, reporte_sueldos):
    reporte_sueldos=[]
    for persona in trabajadores_con_sueldo:
        desc_salud=float(persona[1])*0.07
        desc_afp=float(persona[1])*0.12
        liquido=float(persona[1])-desc_afp-desc_salud
        detalle=[persona[0],persona[1],desc_salud,desc_afp,liquido]
        reporte_sueldos.append(detalle)
    print("Nombre Empleado      Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Liquido")
    f=open("reporte_sueldos.csv","w")
    f.write("Nombre Empleado      Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Liquido\n")
    for persona in reporte_sueldos:
        print(f"{persona[0]}        ${persona[1]}        ${persona[2]}        ${persona[3]}        ${persona[4]}")
        f.write(f"{persona[0]}        ${persona[1]}        ${persona[2]}        ${persona[3]}        ${persona[4]}\n")
    f.close()

def fin_programa():
    print("Finalizando programa...")
    print("Desarrollando por Francisca Barrera")
    print("RUT 21.680.800-2")

while True:
    system("cls")
    print(menu)
    op=input("Seleccione una opción: ")
    if op=="1":
        asignar_sueldos(trabajadores, trabajadores_con_sueldo)
        input("Ingrese enter para continuar...")
    elif op=="2":
        clasificar_sueldos(trabajadores_con_sueldo, cont_a, cont_b, cont_c, sueldo_a, sueldo_b, sueldo_c)
        input("Ingrese enter para continuar...")                  
    elif op=="3":
        estadisticas(trabajadores_con_sueldo, cont_d, prom, sueldo_mayor, sueldo_menor)
        input("Ingrese enter para continuar...")
    elif op=="4":
        for persona in trabajadores_con_sueldo:
            if persona[0]=="":
                print("Debe utilizar seleccionar la opción 1 primero...")
                break
            else:
                continue
        reporte_sueldos(trabajadores_con_sueldo, reporte_sueldos)
        input("Ingrese enter para continuar...")
    elif op=="5":
        fin_programa()
        break
    else:
        print("Opción no válida...")
        input("Ingrese enter para continuar...")