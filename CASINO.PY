import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_02
---
Enunciado:
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
Nombre
-Importe ganado (mayor o igual $1000)
-Género (“Femenino”, “Masculino”, “Otro”)
-Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:
A) Nombre y género de la persona que más ganó.
B) Promedio de dinero ganado en Ruleta.
C) Porcentaje de personas que jugaron en el Tragamonedas.
D) Cuál es el juego menos elegido por los ganadores.
E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
F) Porcentaje de dinero en función de cada juego.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        seguir = True

        mayor_importe = 0
        nombre_mayor_importe = None
        genero_mayor_importe = None

        flag_mayor_ganador = True

        contador_ruleta = 0
        acumulador_ruleta = 0
        contador_ruleta = 0

        acumulador_tragamonedas = 0
        contador_tragamonedas = 0

        acumulador_poker = 0
        contador_poker = 0

        acumulador_no_poker = 0
        contador_no_poker = 0

        gente = 0

        


        while True:

            nombre = prompt("Nombre", "Ingrese su nombre")
            print(nombre)

            importe = prompt("Importe", " Ingrese su importe ganado")
            importe = int(importe)
            print(importe)

            while importe < 1000:
                importe = prompt("Error", "Debe ser un numero mayor a 1000 (MIL)")
                importe = int(importe)
            
            genero = prompt("Genero", "Ingrese su genero (f, m u otro)")
            print(genero)

            while genero != "f" and genero != "m" and genero != "otro":
                genero = prompt("Error", "Ingrese un genero valido")

            juego = prompt("Juego", "Ingrese su juego (ruleta, poker, tragamonedas)")
            print(juego)
            
            while juego != "ruleta" and juego != "poker" and juego != "tragamonedas":
                juego = prompt("Error", "Ingrese un juego valido")
                
            #A
            if importe > mayor_importe or flag_mayor_ganador == True:
                mayor_importe = importe
                nombre_mayor_importe = nombre
                genero_mayor_importe = genero
                flag_mayor_ganador = False

            #B
            match juego:
                case "ruleta":
                    acumulador_ruleta += importe
                    contador_ruleta += 1
                case "tragamonedas":
                    contador_tragamonedas += 1
                    acumulador_tragamonedas += importe
                case "poker":
                    contador_poker += 1
                    acumulador_poker += importe

            if juego != "poker" and importe > 15000:
                acumulador_no_poker += importe
                contador_no_poker += 1

            gente += 1

            seguir = question("Seguir?", "Desea seguir ingresando datos de otra persona?")

            if seguir == False:
                break

        #B
        if contador_ruleta != 0:

            promedio_ruleta = acumulador_ruleta / contador_ruleta
        else:
            promedio_ruleta = prompt("Error", "No se ingreso ninguna ruleta")

        #C
        total_juegos = contador_poker + contador_ruleta + contador_tragamonedas
        
        porcentaje_tragamonedas = (contador_tragamonedas * 100 ) / total_juegos

        #D
        if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
            juego_menos_jugado = "poker"
        elif contador_ruleta < contador_tragamonedas:
            juego_menos_jugado = "ruleta"
        else:
            juego_menos_jugado = "tragamonedas"


        #E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
        porcentaje_no_poker_mayor_15k = acumulador_no_poker / contador_no_poker

        #F) Porcentaje de dinero en función de cada juego.
        total_importe = acumulador_poker + acumulador_ruleta + acumulador_tragamonedas

        porcentaje_dinero_poker = (acumulador_poker * 100) / total_importe
        porcentaje_dinero_tragamonedas = (acumulador_tragamonedas * 100) / total_importe
        porcentaje_dinero_ruleta = (acumulador_ruleta * 100) / total_importe

        print(f"nombre y genero de la persona que mas ganó:{nombre_mayor_importe}, {genero_mayor_importe}\n Promedio ganado en la ruleta: {promedio_ruleta}\n Porcentaje personas que jugaron al tragamonedas: {porcentaje_tragamonedas}%\n Juego menos elegido: {juego_menos_jugado}\n Promedio ganado de personas que no jugaron al poker y ganaron mas de 15K: {porcentaje_no_poker_mayor_15k}\n Porcentaje poker: {porcentaje_dinero_poker}%\n porcentaje ruleta: {porcentaje_dinero_ruleta}%\n porcentaje tragamonedas {porcentaje_dinero_tragamonedas}%")


        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()