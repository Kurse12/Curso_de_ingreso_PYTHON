import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Valentin
apellido:Corallo
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_negativo = 0
        contador_positivo = 0
        contador_ceros = 0

        while True:
            numero = prompt("Numero", "Ingrese un numero")
            if numero != None and numero != "":
                numero = int(numero)
            else:
                break

            if numero > 0:
                acumulador_positivos += numero
                contador_positivo += 1

            elif numero < 0:
                acumulador_negativos += numero
                contador_negativo += 1

            else:
                contador_ceros += 1

        diferencia = contador_positivo - contador_negativo

        mensaje = f"Resultado \n la suma acumulada de lo negatvios es: {acumulador_negativos} \n la suma acumulada de los positivos es: {acumulador_positivos} \n la diferencia es: {diferencia} \n la cantidad de positivos: {contador_positivo} \n la cantidad de negativos : {contador_negativo} \n cantidad de ceros: {contador_ceros}"

        alert("Mensaje", f"{mensaje}")




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
