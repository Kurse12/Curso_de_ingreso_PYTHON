import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

C-

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)





'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #inicializaciones fuera del while
         
        i = 0
        contador_masc = 0
        contador_fem = 0
        contador_nb = 0

        acumulador_masc = 0
        acumulador_fem = 0
        acumulador_nb = 0

        con_fiebre = 0
        sin_fiebre = 0

        mayores_de_edad = 0
        suma_edades = 0

        

        menor_temp = 0
        flag_nombre_menor_temp = True

        sexo_mas_ingresado = 0
        
        
        #Validaciones adentro del while
        while i < 5:
            
            nombre = prompt("Mensaje", "Ingrese el nombre")
            print(nombre)

            edad = prompt("Mensaje", "Ingrese la edad")
            edad = int(edad)
            print(edad)

            while edad < 0:
                edad = prompt("La edad debe ser mayor a cero")
                edad = int(edad)


            sexo = prompt("Mensaje", "Ingrese el sexo (f, m, nb)")

            while sexo != "m" and sexo != "f" and sexo != "nb":
                sexo = prompt("Mensaje", "Ingrese un sexo valido")
                continue

            print(sexo)


            temperatura = prompt("Mensaje", "Ingrese la temperatura")
            temperatura = int(temperatura)

            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("Mensaje", "Ingrese una temperatura valida...")
                temperatura = int(temperatura)

            print(temperatura)

            #incremento de variables dentro del while mayor

            match sexo:
                case "m":
                    contador_masc += 1
                case "f":
                    contador_fem += 1
                case "nb":
                    contador_nb += 1

            if temperatura < 38:
                con_fiebre += 1
            else:
                sin_fiebre += 1

            if edad >= 18:
                mayores_de_edad += 1
                suma_edades = suma_edades + edad

            match sexo:
                case "m":
                    if temperatura < menor_temp or flag_nombre_menor_temp == True:
                        menor_temp = temperatura
                        masculino_menor_temp = (nombre)
                        flag_nombre_menor_temp = False
                case _:
                        masculino_menor_temp = ("No hay")

                
            

            i += 1



        #resoluciones matematicas fuera del while mayor
        #A            
        if contador_masc > contador_fem and contador_masc > contador_nb:
            acumulador_masc += 1
        elif contador_fem > contador_nb:
            acumulador_fem += 1
        else:
            acumulador_nb += 1

        if acumulador_fem > acumulador_masc and acumulador_fem > acumulador_nb:
            sexo_mas_ingresado = "Femenino"
        elif acumulador_masc > acumulador_nb:
            sexo_mas_ingresado = "Masculino"
        else:
            sexo_mas_ingresado = "No binario"

        #B
        porcentaje_fiebre = (con_fiebre * 100) / 5
        porcentaje_sin_fiebre = (sin_fiebre * 100) / 5

        
        #C 3
        edad_promedio_mayores = suma_edades / mayores_de_edad 

        print(f"A) Sexo mas ingresado:{sexo_mas_ingresado}\n B) porcentaje con fiebre: {porcentaje_fiebre}\n porcentaje sin fiebre: {porcentaje_sin_fiebre}\n C) 1- Mayores de edad: {mayores_de_edad}\n 2- Promedio de edad de los mayores: {edad_promedio_mayores}\n 3- Nombre del masculino de temperatura mas baja: {masculino_menor_temp}")
            




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()