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
        else:
            print("No se permite dejar el nombre en blanco")
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
        self.__puntaje = 0
        self.bandas = []
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,cat):
        if cat != "":
            check = cat.lower()
            if check == "primaria" or check == "básico" or check == "basico" or check == "diversificado":
                self.__categoria = cat
            else:
                print("La categoría ingresada no es valida")
        else:
            print("No puede dejar el espacio vacío")
    def guardar(self):
        pass
    def get_puntaje(self):
        return self.__puntaje
    def registrar_puntajes(self,sin,rit,mar,pres):
        #Sincronización,Ritmo,Marcha,Presentación
        if isinstance(sin, int):
            pass
        else:
            print("La puntuación de sincronización no es valida")
    def guardar_bandas(self,band):
        self.bandas.append(band)
    def Mostrar(self):
        for b in self.bandas:
            if b.puntaje == 0:
                print(f"Nombre: {b.nombre} -- Institucion: {b.institucion} -- Categoria: {b.categoria}")
            else:
                print(f"Nombre: {b.nombre} -- Institucion: {b.institucion} -- Categoria: {b.categoria} -- Puntaje: {b.puntaje}")
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
        title1 =tk.Label(band, text="Porfavor ingrese todos los datos de su banda",font=("Arial", 16, "bold"))
        title1.place(x = 60, y = 20)
        get_nombre = tk.Label(band, text="Nombre:",font=("Arial", 11, "bold"))
        get_nombre.place(x = 20, y = 70)
        nombre = tk.Entry(band, width=20)
        nombre.place(x = 105, y = 70)
        get_inst = tk.Label(band, text="Institucion:", font=("Arial", 11, "bold"))
        get_inst.place(x=20, y=100)
        inst = tk.Entry(band, width=20)
        inst.place(x=105, y=100)
        get_cat = tk.Label(band,text="Categoría:",font=("Arial", 11, "bold"))
        get_cat.place(x=20, y=130)
        cat = tk.Entry(band, width=20)
        cat.place(x=105, y=130)
        save =tk.Button(band,text="Guardar Banda",
                  command =lambda:self.Guardar(nombre.get(),inst.get(),cat.get()))
        save.place(x = 70, y = 200)
        #tk.Button(band, text="Guardar Banda", command=Banda_Escolar.guardar()).pack()
    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        evaluation = tk.Toplevel(self.ventana)
        evaluation.title("Registrar Evaluacion")
        evaluation.geometry("600x400")
        title2 = tk.Label(evaluation, text="Califique cada criterio de la banda del 0 al 10",font=("Arial", 16, "bold"))
        title2.place(x=70, y=20)
        get_sinc = tk.Label(evaluation, text="Sincronización:", font=("Arial", 11, "bold"))
        get_sinc.place(x=20, y=70)
        sinc = tk.Entry(evaluation, width=20)
        sinc.place(x=125, y=70)
        get_rit = tk.Label(evaluation, text="Ritmo:", font=("Arial", 11, "bold"))
        get_rit.place(x=20, y=100)
        rit = tk.Entry(evaluation, width=20)
        rit.place(x=125, y=100)
        get_mar = tk.Label(evaluation, text="Marcha:", font=("Arial", 11, "bold"))
        get_mar.place(x=20, y=130)
        mar = tk.Entry(evaluation, width=20)
        mar.place(x=125, y=130)
        get_pres = tk.Label(evaluation, text="Presentación:", font=("Arial", 11, "bold"))
        get_pres.place(x=20, y=150)
        pres = tk.Entry(evaluation, width=20)
        pres.place(x=125, y=150)
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
    def Guardar(self,nombre,institucion,catogoria):
        new_band = Banda_Escolar(nombre,institucion,catogoria,0)
        new_band.guardar()
        new_band.Mostrar()
        #tk.Label(band,text=f"
if __name__ == "__main__":
    ConcursoBandasApp()