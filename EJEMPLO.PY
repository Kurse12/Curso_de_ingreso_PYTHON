import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):

        flag_inic = True
        seguir = True

        num_min = 0
        num_max = 0

        while True:
            numero = input("ingrese un numero")
            numero = int(numero)
            

            

                
                
                
            #cambiar candidato mas votado
            if numero > num_max or flag_inic == True:
                num_max = numero
               

                #candidado menos votado
            if numero < num_min or flag_inic == True:
                num_min = numero
                flag_inic = False
                    

            print(num_max)
            print(num_min)


            seguir = question("Seguir?", "Desea ingresar otro numero?")

            if seguir == False:
                break

        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
                

            
