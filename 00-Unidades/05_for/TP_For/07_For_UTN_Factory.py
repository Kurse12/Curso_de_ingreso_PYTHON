import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        participantes = 10

        contador_nb_ssr_js_net  = 0

        contador_f = 0
        contador_m = 0
        contador_nb = 0

        min_edad = 0
        flag_edad = True
        nombre_menor_jr = None

        acumulador_edad_f = 0
        acumulador_edad_m = 0
        acumulador_edad_nb = 0

        contador_py = 0
        contador_asp = 0
        contador_js = 0

        tecnologia_mas_postulada = None




        for i in range(1, participantes +1):
            nombre = prompt("Mensaje", "Ingrese su nombre")
            print(nombre)

            edad = prompt("Mensaje", "Ingrese su edad")
            print(edad)
            edad = int(edad)

            genero = prompt("Mensaje", "Ingrese el genero(F,M, NB)")
            print(genero)

            tecnologia = prompt("Mensaje", "Ingrese la tecnologia(PYTHON - JS - ASP.NET)")
            print(tecnologia)

            puesto = prompt("Mensaje", "Selecciones su puesto (JR, SSR, Sr)")
            print(puesto)


            match genero:
        #a
                case "nb":
                    if (tecnologia == "asp.net" or tecnologia == "js") and edad >= 25 and edad <= 40 and puesto == "ssr":
                        contador_nb_ssr_js_net += 1
                    acumulador_edad_nb += edad
                    contador_nb += 1
        #e
                case "f":
                    contador_f += 1
                    acumulador_edad_f += edad
                case "m":
                    contador_m += 1
                    acumulador_edad_m += edad

        #b   
            match puesto:
                case "jr":
                    if edad < min_edad or flag_edad ==  True:
                        min_edad = edad
                        nombre_menor_jr = nombre
                        flag_edad = False
                case _: 
                    pass
        #d
            match tecnologia:
                case "python":
                    contador_py += 1
                case "js":
                    contador_js += 1
                case "asp.net":
                    contador_asp += 1
                    

        

        #c
        promedio_edad_f = acumulador_edad_f / contador_f
        promedio_edad_m = acumulador_edad_m / contador_m
        promedio_edad_nb = acumulador_edad_nb / contador_nb 

        #d
        if contador_py > contador_js and contador_py > contador_asp:
            tecnologia_mas_postulada = "python"
        elif contador_js > contador_asp:
            tecnologia_mas_postulada = "js"
        else:
            tecnologia_mas_postulada = "asp.net"

        #e
        porcentaje_genero_m = (contador_m * 100) / participantes
        porcentaje_genero_f = (contador_f * 100) / participantes
        porcentaje_genero_nb = (contador_nb * 100) / participantes

        print(f"La cantidad de postulantes de genero no binario que programe en JS o ASP.NET y que tengan entre 25 y 40 es: {contador_nb_ssr_js_net}\n El nombre del postulante de menor edad es: {nombre_menor_jr}\n promedio de edades por genero: Femeninos: {promedio_edad_f}\n Masculinos {promedio_edad_m}\n No binario: {promedio_edad_nb}\n Tecnologia con mas postulantes: {tecnologia_mas_postulada}\n Porcentaje de postulantes por genero:\n Masculino: {porcentaje_genero_m}\n Femenino: { porcentaje_genero_f}\n No binario: {porcentaje_genero_nb}")

        






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
