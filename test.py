# from pprint import pprint as pp
# from CoreData import loadD, saveD
#
# reg_r = loadD('r')
# for persona in reg_r.reg_reservas:
#     pp(persona)
#     pp(reg_r.reg_reservas[persona])
#     for reserva in reg_r.reg_reservas[persona]:
#         pp(reserva)
#         if pp =
#     pp('')

# from CoreData import loadD, saveD
#
# reg_reservas = loadD('r')
# reg_estudiantes = loadD('e')
# cedula = '001'
# isbn = '001'
#
#
# estudiante = reg_estudiantes.encontrar_estudiante(cedula)
#
# for estud in reg_reservas.reg_reservas:
#     # print(type(estud))
#     # print(type(estudiante))
#     if estud.id ==  estudiante.id:
#         print(reg_reservas.reg_reservas[estud])
#         list_reservas_estudiante = reg_reservas.reg_reservas[estud]
#         for reserva in list_reservas_estudiante:
#             print(reserva)
#             if reserva[0].isbn == isbn:
#                 print(isbn)
#                 list_reservas_estudiante.remove(reserva)
#         print(list_reservas_estudiante)
#         print(reg_reservas.reg_reservas)
# saveD('r', reg_reservas)

#
# from CoreData import loadD, saveD, Estudiante
#
# reg_reservas = loadD('r')
# print(reg_reservas.reg_reservas)
#
# for persona in reg_reservas.reg_reservas:
#     print(persona)
#     print(reg_reservas.reg_reservas[persona])
#



# from CoreData import loadD, saveD, Estudiante
#
# reg_libros = loadD('l').reg_libro
# reg_estudiantes = loadD('e').reg_estudiante
#
# print(reg_libros)
# for libro in reg_libros:
#     print(libro.isbn)
#
#
# print('')
# print(reg_estudiantes)
# for estudiante in reg_estudiantes:
#     print(estudiante)
#
# print('')
#
#
# reg_estudiantes = loadD('e')
# estudiante4 = Estudiante('007', 'AEWR', 'BBB')
# reg_estudiantes.add(estudiante4)
#
# # saveD('e', reg_estudiantes)
#
# reg_reservas = loadD('r').reg_reservas
#
# print("Reservas")
# for persona in reg_reservas:
#     # print(reserva)
#     print(reg_reservas[persona][0][0].isbn)
#     print(persona.id)
#     print('--')


# saveD('r', 'hola')

    #
# id_estudiante = '001'
# libro_isbn = '01'
# fch_a_reservar = '0001'
# fch_reserva = '0002'
# hora_reserva = '15.10'
#
#
# # def agregarReserva():
# #     reg_reservas = loadD('r')
# #     print(reg_reservas)
# #
# #     reg_reservas.add(estudiante, libro, fechaAReservar, fechaReserva, Hora)
# #
# #
# #
# #     saveD('r', reg_reservas)
# #
# #
# # # agregarReserva(id_estudiante, )
#
#
#
# from CoreData import loadD, saveD
#
# isbn = 'a1123'
#
# def validateLibro(isbn):
#     reg_libros = loadD('l')
#
#     for libro in reg_libros.reg_libro:
#
#         if libro.isbn == isbn:
#             return True
#     else:
#         return False
#
# print(validateLibro('005'))
#
#
# def validateEstudiante(cedula):
#     reg_estudiantes = loadD('e')
#     for estudiante in reg_estudiantes.reg_estudiante:
#         if estudiante.id == cedula:
#             return True
#     else:
#         return False
#
# print(validateEstudiante('002'))
#
#
#         #
# def validateLibro(isbn):
#     """
#     Valida que un libro exista en el registro de libros
#     :param isbn:
#     :return: Boolean
#     """
#     reg_libros = loadD('l')
#
#     for libro in reg_libros:
#
#         if libro.isbn == isbn:
#             return True
#     else:
#         return False
#
# def validateEstudiante(cedula):
#     """
#     Valida que un usuario se encuentre en el registro de usuarios
#     :param cedula:
#     :return: Boolean
#     """
#     reg_estudiantes = loadD('e')
#     for estudiante in reg_estudiantes:
#         if estudiante.id == cedula:
#             return True
#     else:
#         return False
#
# # from CoreData import loadD
# #
# #
# # registros = loadD('r')
# # dic_reg_reservas = registros.reg_reservas
# #
# # print(dic_reg_reservas)
# # #
# # # for estudiante in dic_reg_reservas:
# # #     print(estudiante.name)
# # #     print(dic_reg_reservas[estudiante][0][0].name)
# #
# #
# # registro_estudiantes = loadD('e')
# # est = registro_estudiantes[1]
# # print(registro_estudiantes)
# #
# # for estudiante  in dic_reg_reservas:
# #     print(estudiante)
# #     print(dic_reg_reservas[estudiante])
# #     if est.id == estudiante.id:
# #         print('ES IGUAL')
# #         print(est)
# #         print(dic_reg_reservas[est])
# #
# # # estu_reservas = dic_reg_reservas[est]
# #
# #
# # # print(estu_reservas)