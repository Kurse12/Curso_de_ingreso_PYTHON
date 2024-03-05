import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidato_mas_votado = None
        max_votos = 0
        candidato_menos_votado = None
        min_votos = 0

        total_edades = 0
        total_candidatos = 0
        total_votos = 0

        promedio_edades = 0

        flag_inic = True
        
        volver_a_ingresar = True


        while True:
            nombre = prompt("Nombre","Ingrese el nombre del candidato")
            if not nombre:
                break

            while True:
                edad = prompt("Edad", f"Ingrese la edad de {nombre}")

                while not edad:
                    break
                edad = int(edad)

                while edad <= 25:
                    alert("Error", "La edad del candidato debe ser mayor a 25")
                    continue
                while edad >= 100:
                    alert("Error", "Solo pueden postularse personas vivas")
                    continue

                while edad == None:
                    prompt("Mensaje", "Es necesario ingresara una edad")
                    continue
                
                else:
                    break

            while True:

                votos = prompt("Votos", f"Ingrese la cantidad de votos de {nombre}")
                if not votos:
                    votos = 0
                    break

                votos = int(votos)
                if votos < 0:
                    alert("Error", "La cantidad de votos debe ser mayor o igual a cero")
                    continue

                #cambiar candidato mas votado
                if votos > max_votos or flag_inic == True:
                    max_votos = votos
                    candidato_mas_votado = nombre

                #candidado menos votado
                if votos < min_votos or flag_inic == True:
                    min_votos = votos
                    flag_inic = False
                    candidato_menos_votado = nombre

                break

                #preguntar si quiere ingresar otro candidato
            volver_a_ingresar = question("Continuar?", "Desea ingresar otro candidato?")

            if volver_a_ingresar == False:
                break
                
                
                

            #cambiar maximo de votos
            print(votos)
            
            #actualizar totales
            total_edades += edad
            total_candidatos += 1
            total_votos += votos

            #promedio edades
            promedio_edades = total_edades / total_candidatos if total_candidatos > 0 else 0

            #resultados
        alert("Resultados", f"Candidato con mas votos:{candidato_mas_votado} votos, {max_votos}\n candidato menos votado:{candidato_menos_votado}, {min_votos} votos\n Promedio de edades: {promedio_edades}\n Total de votos emitidos: {total_votos}")
            

            



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
