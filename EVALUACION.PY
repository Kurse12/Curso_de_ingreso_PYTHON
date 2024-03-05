import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Valentin
apellido:Corallo
---
Ejercicio: entrada_salida_02
---
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        seguir = True

        contador_f = 0
        contador_m = 0

        sexo_menos_ingresado = None

        contador_perro = 0
        contador_gato = 0
        contador_exotico = 0

        flag_peso = True
        menos_peso = 0
        nombre_menos_peso = 0
        tipo_menos_peso = 0

        flag_perro = True
        perro_joven = 0

        acumulador_peso = 0
       

        while True:
            nombre = prompt("Nombre", "Ingrese el nombre de la mascota")
            print(nombre)

            tipo = prompt("Tipo", "Ingrese el tipo de mascota (gato, perro o exotico)")
            print(tipo)

            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("Error", "Ingrese un tipo valido de mascota")

            peso = prompt("Peso", "Ingrese el peso de la mascota")
            peso = int(peso)

            while peso < 11 or peso > 80:
                peso = prompt("Error", "Ingrese un peso valido")
                peso = int(peso)
            print(peso)

            sexo = prompt("Sexo", "Ingrese el sexo de la mascota(f o m)")
            
            while sexo != "f" and sexo != "m":
                sexo = prompt("Error", "Ingrese un sexo valido")
            print(sexo)

            edad = prompt("Edad", "Ingrese la edad de la mascota(mayor a 0)")
            edad = int(edad)

            while edad < 1:
                edad = prompt("Error", "Ingrese una edad valida")
                edad = int(edad)
            print(edad)


            match sexo:
                case "f":
                    contador_f += 1
                case "m":
                    contador_m += 1
            
            match tipo:
                case "perro":
                    contador_perro += 1
                    acumulador_peso += peso
                    if edad < perro_joven or flag_perro == True:
                        perro_joven = nombre, "con", edad
                        #nombre_perro_joven = nombre
                        flag_perro = False
                case "gato":
                    contador_gato += 1
                    acumulador_peso += peso
                case "exotico":
                    contador_exotico += 1
                    acumulador_peso += peso

            if peso < menos_peso or flag_peso == True:
                menos_peso = peso
                nombre_menos_peso = nombre
                tipo_menos_peso = tipo
                flag_peso = False            

            seguir = question("Seguir?", "Desea seguir?")

            if seguir == False:
                break
        
        #A
        if contador_m < contador_f:
            sexo_menos_ingresado = "Masculino"
        else:
            sexo_menos_ingresado = "Femenino"

        #B
        total_mascotas = contador_exotico + contador_gato + contador_perro

        porcentaje_perros = (contador_perro * 100) / total_mascotas
        porcentaje_gatos = (contador_gato * 100) / total_mascotas
        porcentaje_exoticos = (contador_exotico * 100) / total_mascotas

        promedio_peso = acumulador_peso / total_mascotas

        if perro_joven == 0:
            perro_joven = "No hay perros"
            #nombre_perro_joven = "No hay perros"

        print(f"El sexo menos ingresado fue: {sexo_menos_ingresado}\n El porcentaje de mascotas es: {porcentaje_perros}% de perros \n {porcentaje_gatos}% de gatos \n {porcentaje_exoticos}% de exoticos \n la mascota menos pesada es: {nombre_menos_peso}, {tipo_menos_peso}, con {menos_peso}kg \n El perro mas joven es: {perro_joven} \n El promedio de peso de las mascotas es: {promedio_peso}")



        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()