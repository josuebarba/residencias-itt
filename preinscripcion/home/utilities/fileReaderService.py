# def ReadXls(request): # Recorre el archivo Excel que contiene todos los alumnos y los guarda en la base de datos.
#     # file_loc = "ISC.xls"
#     # df = pd.read_excel(file_loc, index_col = 0, na_values=['NA'], usecols = "A,C:AA")
#     # # xlsx = pd.ExcelFile("ISC.xls")
#     # print df
#     xls = pd.ExcelFile("ISC2.xls")
#     print(xls.sheet_names)
#     df=xls.parse('x34300')
#     print(df.index)
#
#     for index, item in enumerate(df.index):
#         p = Alumno(no_control=df.cc_ctr[index],password="123",semestre=df.cc_npe[index],nombre=df.cc_nom[index],status=0)
#         p.save()
#     return HttpResponse('200')
#
# def addMaterias(requiest): #Recorre el archivo que contiene todas las materias y los guarda en la base de datos.
#     xls = pd.ExcelFile("ISC2.xls")
#     df= xls.parse("Sheet2")
#
#     for index, item in enumerate(df.index):
#         p = Materia(clave=df.Clave[index], semestre=df.Semestre[index], nombre=df.Nombre[index],creditos=df.Creditos[index],horas_teoricas=df.Teoria[index],horas_practicas=df.Practica[index],previous=df.Previous[index],next=df.Next[index])
#         p.save()
#     return HttpResponse('200')