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
    def __init__(self,nombre,institucion,categoria):
        super().__init__(nombre, institucion)
        self.__categoria = categoria
        self.__puntaje = 0
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
    def get_puntaje(self):
        return self.__puntaje

class concurso:
    def __init__(self):
        self.participantes = []
    def Agregar_Participante(self,banda):
       self.participantes.append(banda)
    def get_bands(self):
        return self.participantes

    def registrar_puntajes(self, sin, rit, mar, pres,name):
        # Sincronización,Ritmo,Marcha,Presentación
        for p in self.participantes:
            if p.get_nombre() == name:
                if isinstance(sin, int):
                    if sin >= 0 and sin <= 10:
                        if isinstance(rit, int):
                            if rit >= 0 and rit <= 10:
                                if isinstance(mar, int):
                                    if mar >= 0 and mar <= 10:
                                        if isinstance(pres, int):
                                            if pres >= 0 and pres <= 10:
                                                promedio = sin + rit + mar + pres
                                                promedio = promedio / 4
                                                p.set_puntaje = promedio
                                                print("Se a calificado exitosamente")
                                            else:
                                                print("La puntuación de presentación no es valida")
                                        else:
                                            print("La puntuación de presentación no es valida")
                                    else:
                                        print("La puntuación de Marcha no es valida")
                                else:
                                    print("La puntuación de Marcha no es valida")
                            else:
                                print("La puntuación de ritmo no es valida")
                        else:
                            print("La puntuación de ritmo no es valida")
                    else:
                        print("La puntuación de sincronización no es valida")
                else:
                    print("La puntuación de sincronización no es valida")
            else:
                print("No hay ninguna banda con ese nombre")
con = concurso()
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
        get_sinc.place(x=10, y=70)
        sinc = tk.Entry(evaluation, width=20)
        sinc.place(x=165, y=70)
        get_rit = tk.Label(evaluation, text="Ritmo:", font=("Arial", 11, "bold"))
        get_rit.place(x=10, y=100)
        rit = tk.Entry(evaluation, width=20)
        rit.place(x=165, y=100)
        get_mar = tk.Label(evaluation, text="Marcha:", font=("Arial", 11, "bold"))
        get_mar.place(x=10, y=130)
        mar = tk.Entry(evaluation, width=20)
        mar.place(x=165, y=130)
        get_pres = tk.Label(evaluation, text="Presentación:", font=("Arial", 11, "bold"))
        get_pres.place(x=10, y=160)
        pres = tk.Entry(evaluation, width=20)
        pres.place(x=165, y=160)
        get_name = tk.Label(evaluation, text ="Nombre de la banda: ",font=("Arial", 11, "bold"))
        get_name.place(x=10, y=190)
        name = tk.Entry(evaluation, width=20)
        name.place(x=165, y=190)
        grade = tk.Button(evaluation,text="Calificar banda",command = lambda:self.Puntuar(name.get(),sinc.get(),rit.get(),mar.get(),pres.get()))
        grade.place(x=50, y=240)
    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        listar = tk.Toplevel(self.ventana)
        listar.title("Listado de Bandas")
        listar.geometry("600x400")
        title3 = tk.Label(listar,text="Lista de las bandas participantes",font=("Arial", 16, "bold"))
        title3.place(x=110, y=20)
        part = tk.Listbox(listar,width=80,height=20)
        part.place(x=60, y=60)
        bandas = con.get_bands()
        for band in bandas:
            texto = (f"Nombre: {band.get_nombre()} | Institución: {band.get_institucion()} | "
                     f"Categoría: {band.get_categoria()} | Puntaje: {band.get_puntaje()}")
            part.insert("end",texto)
    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ranking = tk.Toplevel(self.ventana)
        ranking.title("Ranking Final")
        ranking.geometry("600x400")
    def Guardar(self,nombre,institucion,categoria):
        new_band = Banda_Escolar(nombre,institucion,categoria)
        con.Agregar_Participante(new_band)
        #tk.Label(band,text=f"
    def Puntuar(self,nombre,sin,rit,mar,pres):
        con.registrar_puntajes(sin,rit,mar,pres,nombre)
if __name__ == "__main__":
    ConcursoBandasApp()