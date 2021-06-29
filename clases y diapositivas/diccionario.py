usuario = ('jquirumabyr','1234','jquirumbayr@gmail.com')
materias = ['Python','PHP','POO','Go']
alumno = {'nombre':'Jesus','edad':19,'fac':'faci'}
print(usuario[0],materias[1],alumno['nombre'])
print(usuario[0:2],alumno.keys(),alumno.values())
materias.append('Programa Movil')
alumno['sexo'], alumno['edad']='M', 20
print(materias,alumno)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in alumno.items(): print(c,':',v)