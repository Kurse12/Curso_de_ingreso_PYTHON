import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #que va antes del while
        continuar = True
        contador_masculino_tecnologia_edad = 0

        contador_iot = 0
        contador_ia = 0
        contador_rv_ra = 0

        tecnologia_mas_votada = None

        contador_masc = 0
        contador_fem = 0
        contador_otro = 0

        contador_iot_edad = 0

        contador_fem_ia = 0
        acumulador_fem_edad = 0

        flag_min = False
        minima_edad = 0

        nombre_minimo = None
        genero_minimo = None

        #que va adentro del while
        while continuar == True:
            nombre = prompt("Nombre", "Ingrese nombre")

            edad = prompt("Edad", "Ingrese edad")
            edad = int(edad)

            while edad < 18:

                edad = prompt("Error", "Ingrese una edad valida")
                edad = int(edad)

            genero = prompt("Genero", "Ingrese genero")

            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":

                genero = prompt("Error", "Ingrese un genero")

            tecnologia = prompt("Tecnologia", "Ingrese la tecnologia")

            while tecnologia != "I" and tecnologia != "RV/RA" and tecnologia != "IOT":

                tecnologia = prompt("Error", "Reingrese la tecnologia")

            #1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
            if genero == "Masculino" and (tecnologia == "IOT" or "IA") and edad >= 25 and edad <= 50:
                contador_masculino_tecnologia_edad += 1

            #!X 2) - Tecnología que mas se votó.
            if tecnologia == "IA":
                contador_ia += 1
            elif tecnologia == "IOT":
                contador_iot += 1
                if edad >= 18 and edad <=35 or edad >= 33 and edad <= 42:
                    contador_iot_edad += 1
            else:
                contador_rv_ra += 1
                #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                if flag_min == False or edad < minima_edad:
                    minima_edad = edad
                    nombre_minimo = nombre
                    genero_minimo = genero
                    flag_min = True

            #!X 3) - Porcentaje de empleados por cada genero

            match genero:
                case "Masculino":
                    contador_masc += 1
                case "Femenino":
                    contador_fem += 1
                    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if tecnologia == "IA":
                        contador_fem_ia += 1
                        acumulador_fem_edad += 1
                case "Otro":
                    contador_otro += 1

                


            continuar = question("Seguir?", "Desea continuar?")


        #que va afuera del while
            
        if contador_ia > contador_iot and contador_ia > contador_rv_ra:
            tecnologia_mas_votada = "IA"
        elif contador_iot > contador_rv_ra:
            tecnologia_mas_votada = "IOT"
        else:
            tecnologia_mas_votada = "RV_RA"

        #!X 3) - Porcentaje de empleados por cada genero
            total_empleados = contador_fem + contador_masc + contador_otro

            porcentaje_masc = (contador_masc * 100) / total_empleados
            porcentaje_fem = (contador_fem * 100) / total_empleados
            porcentaje_otro = (contador_otro * 100) / total_empleados

        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
            porcentaje_edad = (contador_iot_edad * 100) / total_empleados

        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
            if contador_fem_ia != 0:
                promedio_edad = (acumulador_fem_edad * 100) / contador_fem_ia
            else:
                promedio_edad = "No se ingresó ningun femenino que cumpla el requisito"
        


        print(f"1. Cantidad  masculinos que votaron iot o ia en rango de edad 25/50:{contador_masculino_tecnologia_edad}")
        print(f"2. La tecnologia mas votada es: {tecnologia_mas_votada}")
        print(f"3. Porcentajes: \n \t{porcentaje_fem}%\n \t{porcentaje_masc}%\n \t{porcentaje_otro}%")
        if contador_rv_ra != 0:
            print(f"3.{minima_edad}{genero_minimo}{nombre_minimo}")
        else:
            print("No se ingresó votos para RV")
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


    '''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

