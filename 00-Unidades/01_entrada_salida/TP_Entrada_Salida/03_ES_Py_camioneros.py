import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino 

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Toneladas")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_toneladas = customtkinter.CTkEntry(master=self)
        self.txt_toneladas.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Kilómetros")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_kilometros = customtkinter.CTkEntry(master=self)
        self.txt_kilometros.grid(row=1, column=1)
       
        self.btn_cantidad_camiones = customtkinter.CTkButton(master=self, text="Calcular cantidad de camiones", command=self.btn_cantidad_camiones_on_click)
        self.btn_cantidad_camiones.grid(row=3, pady=10, padx=30 ,columnspan=2, sticky="nsew")
        
        self.btn_tiempo_llegada = customtkinter.CTkButton(master=self, text="Calcular tiempo de llegada", command=self.btn_tiempo_llegada_on_click)
        self.btn_tiempo_llegada.grid(row=4, pady=10, padx=30, columnspan=2, sticky="nsew")
    
    def btn_cantidad_camiones_on_click(self):
        votos_giovanni = 0
        votos_gianni = 0
        votos_esteban = 0

        votos = 0

        votante_mas_viejo = 0
        votante_mas_joven = 0

        contador_femeninos = 0

        porcentaje_giovanni = 0
        porcentaje_gianni = 0
        porcentaje_esteban = 0

        flag_edad = True

        max_edad = 0
        min_edad = 0

        mas_joven = None
        mas_viejo = None
        voto_mas_joven_gianni = None

        abandona_casa = None

        promedio_fem = 0

        promedio_edad_fem = 0


        while True:

            nombre = prompt("Nombre", "Ingrese su nombre")

            edad = prompt("Edad", "Ingrese su edad")
            edad = int(edad)
            print(nombre)
                
            while edad < 13:
                edad = prompt("Error", "Ingrese una edad valida")
                edad = int(edad)
                continue
            print(edad)

            genero = prompt("Genero", "Ingrese su genero (f, m u otro)")

            while genero != "f" and genero != "m" and genero != "otro":      
                genero = prompt("Error", "Ingrese un genero valido")
                continue
            print(genero)

            nombre_participante = prompt("Nombre participante", "Ingrese el nombre del participante que desea eliminar (Giovanni, Gianni o Esteban)")

            while nombre_participante != "Giovanni" and nombre_participante != "Gianni" and nombre_participante != "Esteban":
                nombre_participante = prompt("Error", "Ingrese un participante valido")
                continue

            print(nombre_participante)
            print(votos_esteban, votos_gianni, votos_giovanni)

            

            if edad < min_edad or flag_edad == True:
                min_edad = edad
                
            
            if edad > max_edad or flag_edad == True:
                max_edad = edad
                mas_viejo = nombre


            if genero == "f":
                contador_femeninos += 1
                promedio_edad_fem += edad

            if nombre_participante == "Giovanni":
                votos_giovanni += 1

            elif nombre_participante == "Gianni":
                votos_gianni += 1
                
            else:
                votos_esteban += 1

                
            votos += 1


            seguir = question("Seguir?", "continuar?")

            if seguir == False:
                break

        if votos_esteban == 0:
            votos_esteban = "No tuvo votos"

        if votos_gianni == 0:
            votos_gianni = "No tuvo votos"

        if votos_giovanni == 0:
            votos_giovanni = "No tuvo votos"

        print(votos_esteban, votos_gianni, votos_giovanni)
            #promedio edad femenino


        promedio_fem = promedio_edad_fem / contador_femeninos 

        promedio_gianni = votos_gianni * 100 / votos
        promedio_giovanni = votos_giovanni * 100 / votos
        promedio_esteban = votos_esteban  * 100/ votos

        print("promedio de edad:" f"{promedio_fem}")
        print("Votante mas viejo:" f"{mas_viejo}")
        print("Votante mas joven que votó a Gianni:" f"{voto_mas_joven_gianni}")
        print("Promedio giovanni:", f"{promedio_giovanni}")
        print("Promedio gianni:", f"{promedio_gianni}")
        print("Promedio esteban:", f"{promedio_esteban}")





            

           





        

    def btn_tiempo_llegada_on_click(self):
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()