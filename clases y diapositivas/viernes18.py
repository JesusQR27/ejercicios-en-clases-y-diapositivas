clase  para :
    def  usoFor ( self ):

        listasNotas = [( 30 , 40 , 10 , 20 ), ( 20 , 40 , 50 ), ( 50 , 40 , 10 ), ( 10 , 20 )]
        acum , cont = 0 , 0
        de  notas  en  listasNotas :
            imprimir ( notas )
            acump = 0
            contp = 0
            para  nota  en  notas :
                acump  + = nota
                acum = acum + nota
                cont = cont + 1
            imprimir ( acump / len ( notas ))
        imprimir ( acum / cont )
bucle  =  Para ()
bucle.usoFor ()
