class sintaxis:
    instancia=0
    #__init__ metodoconstructor que se ejecuta cuando se intancia la clase cuyo onjetivo es  
    # crear e instanciar los atributos de la clase. self es un objeto que representa la clase creada.

    def __init__(self,dato="llamando al constructor1" ):
        self.frase=dato   #-------> #atributos de instancia
        sintaxis.instancia=sintaxis.instancia+1


    def usovariables(self):
        edad,peso=20,70,5
        nombres:"JesusQuirumbay"
        tipo_de_sexo: "M"
        civil:True
        usuario=()
        usuario=("jquirumbayr1","1234","jquirumbayr1@gmail.com",True)
        #             0      1      2             3 
        x=usuario[0]
        materia=["programacion web","php","poo"]
        materia.append("go")

        estudiante={}
        estudiante={"nombre":"Jesus","edad":19,"fac":"faci",}
        estudiante["edad"]=19
        print("x,y")
        print(estudiante,estudiante["nombre"])
    def mostrar(self):
        print("mostrar")
        print(self.frase)



ejer1=sintaxis()
ejer1.usovariables()