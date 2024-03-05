import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Valentin
apellido:Corallo
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = None
        edad = 0
        numero_legajo = 1000
        i = 0

        while i < 4:
            if i == 0:
                ingreso_apellido = prompt("Mensaje", "Ingresa el apellido")

                apellido = ingreso_apellido

                if ingreso_apellido == None or ingreso_apellido == "":
                    alert("Mensaje", "INGRESA ALGO")
                    continue
                            
            i+=1

            if i == 1:
                ingreso_edad = prompt("Mensaje", "Ingrese su edad")
                
                edad = ingreso_edad

                if ingreso_edad == None or ingreso_edad == "":
                    alert("Mensaje", "INGRESA ALGO")
                    continue
            i+=1

            if i == 2:
                ingreso_estado = prompt("Mensaje", "Ingrese su estado civil")

                estado = ingreso_estado

                if estado == "soltero" or estado == "Soltero" or estado == "soltera" or estado == "Soltera":
                    estado = self.combobox_tipo.set("Soltero/a")
                elif estado == "casado" or estado == "Casado" or estado == "casada" or estado == "Casada":
                    estado = self.combobox_tipo.set("Casado/a")
                elif estado == "divorciado" or estado == "Divorciado" or estado == "divorciada" or estado == "Divorciada":
                    estado = self.combobox_tipo.set("Divorciado/a")
                elif estado == "viudo" or estado == "Viudo" or estado == "Viuda" or estado == "viuda":
                    estado = self.combobox_tipo.set("Viudo/a")
                
                if ingreso_apellido == None:
                    continue
            i += 1

            if i == 3:
                legajo = 0
                ingreso_legajo = prompt("Mensaje", "Ingese su legajo")
                legajo = int(ingreso_legajo)

                if legajo <= 1000 or legajo >= 9999:
                    prompt("Mensaje", "El legajo es un numero de 4 cifras...")
                
                if ingreso_legajo == None:
                    
                    break

            i += 1



        self.txt_apellido.delete(0, "end")
        self.txt_apellido.insert(0, apellido)

        self.txt_edad.delete(0, "end")
        self.txt_edad.insert(0, edad)

        self.txt_legajo.delete(0, "end")
        self.txt_legajo.insert(0, legajo)

        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
