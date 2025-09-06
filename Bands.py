import tkinter as tk
class Participantes:
    def __init__(self,nombre,institucion):
        self.__nombre = nombre
        self.__institucion = institucion
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nom):
        if nom.strip() != "":
            self.__nombre = nom
    def get_institucion(self):
        return self.__institucion
    def set_institucion(self,inst):
        if inst.strip() != "":
            self.__institucion = inst
    def Mostar(self):
        print(f"Nombre: {self.get_nombre()} -- Institucion: {self.get_institucion()}")
class Banda_Escolar(Participantes):
    def __init__(self,nombre,institucion,catogoria,puntaje):
        self.nombre = nombre
        self.institucion = institucion
        self.__categoria = catogoria
        self.__puntaje = puntaje
class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        band = tk.Toplevel(self.ventana)
        band.title("Inscribir Banda")
        band.geometry("600x400")
    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        evaluation = tk.Toplevel(self.ventana)
        evaluation.title("Registrar Evaluacion")
        evaluation.geometry("600x400")
    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        listar = tk.Toplevel(self.ventana)
        listar.title("Listado de Bandas")
        listar.geometry("600x400")
    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ranking = tk.Toplevel(self.ventana)
        ranking.title("Ranking Final")
        ranking.geometry("600x400")
if __name__ == "__main__":
    ConcursoBandasApp()