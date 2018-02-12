# def login(request): #Se realiza el login a la plataforma, se valida que la password sea la misma que la obtenida en la consulta
#     if request.method == "POST":
#         m = Alumno.objects.get(no_control=request.POST['no_control']) #Consulta la informacion del usuario ingresado
#         if m.password == request.POST['password']:
#             request.session['no_control'] = m.no_control
#             request.session['semestre'] = m.semestre
#             request.session['status'] = m.status
#             request.session['nombre'] = m.nombre
#             return redirect('pick_view')
#         else:
#             return render(request,"login.html")
#
# #     if request.session['no_control']:
# #         return redirect('pick_view')
#     else:
#         return render(request,"login.html")
#
#
# def logout(request): # Elimina los datos de la sesion para salir de la misma.
#     request.session['no_control'] = 0
#     return render(request,"login.html")