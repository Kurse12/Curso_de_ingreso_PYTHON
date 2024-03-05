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
Enunciado: Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

-Nombre
-Edad (debe ser mayor a 12)
-Altura (no debe ser negativa)
-Días que asiste a la semana (1, 3, 5)
-Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
A) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
B) El porcentaje de clientes que asiste solo 1 día a la semana.
C) Nombre y edad del cliente con más altura.
D) Determinar si los clientes eligen más ir 1, 3 o 5 días
E) Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        seguir = True

        contador_1_dia = 0
        contador_3_dia = 0
        contador_5_dia = 0

        acumulador_kilos_3_dias = 0

        max_altura = 0
        flag_inic = True
        edad_mas_altura = 0
        nombre_mas_altura = None

        edad_min = 0
        flag_edad_min = True
        nombre_edad_min = 0
        kilos_edad_min = 0

        personas = 0
        
        dia_mas_elegido = 0

        while True:

            nombre = prompt("Nombre", "Ingrese su nombre")


            edad = prompt("Edad", "Ingrese su edad")
            edad = int(edad)

            while edad < 12:
                edad = prompt("Error", "Ingrese una edad valida")
                edad = int(edad)

            altura = prompt("Altura", "Ingrese su altura")
            altura = int(altura) 

            while altura < 0:
                altura = prompt("Error", "Ingrese una altura valida")
                altura = int(altura)

            dias_asistidos = prompt("Dias", "Ingrese la cantidad de dias que asiste a la semana (1, 3 o 5)")
            dias_asistidos = int(dias_asistidos)

            while dias_asistidos != 1 and dias_asistidos != 3 and dias_asistidos != 5:
                dias_asistidos = prompt("Error", "Ingrese una cantidad valida de dias")
                dias_asistidos = int(dias_asistidos)

            kilos_pm = prompt("Kilos", "Ingrese la cantidad de kilos que levanta en peso muerto")
            kilos_pm = int(kilos_pm)

            while kilos_pm < 1:
                kilos_pm = prompt("Error", "Ingrese un peso valido")



            match dias_asistidos:
                case 1:
                    contador_1_dia += 1
                case 3:
                    #A
                    contador_3_dia += 1
                    acumulador_kilos_3_dias = kilos_pm
                case 5:
                    if edad < edad_min or flag_edad_min == True:
                        edad_min = edad
                        nombre_edad_min = nombre
                        kilos_edad_min = kilos_pm

                    contador_5_dia += 1
            #C
            if altura > max_altura or flag_inic == True:
                max_altura = altura
                nombre_mas_altura = nombre
                edad_mas_altura = edad
                flag_inic = False

            

            personas += 1


            seguir = question("Seguir?", "Desea ingresar otra persona?")

            if seguir == False:
                break
        #A
        promedio_kilos_3_dias = acumulador_kilos_3_dias / contador_3_dia

        #B
        porcentaje_1_dia = (contador_1_dia * 100) / personas

        #D
        if contador_1_dia > contador_3_dia and contador_1_dia > contador_5_dia:
            dia_mas_elegido = "1 dia"
        elif contador_3_dia > contador_5_dia:
            dia_mas_elegido = "3 dias"
        else:
            dia_mas_elegido = "5 dias"

        print(f"Promedio de kilos que levantan las personas que solo asisten 3 dia por semana: {promedio_kilos_3_dias} \n Porcentaje de clientes que solo asiste 1 dia por semana: {porcentaje_1_dia} \n Nombre y edad del cliente con mas altura: {nombre_mas_altura} {edad_mas_altura} {max_altura} \n Los clientes eligen mas ir: {dia_mas_elegido} \n Nombre y cantidad de kilos que levanta el cliente mas joven que asista 5 dias: {nombre_edad_min} {kilos_edad_min} {edad_min}")
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()