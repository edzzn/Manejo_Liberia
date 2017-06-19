from CoreData import loadD


registros = loadD('r')
dic_reg_reservas = registros.reg_reservas

print(dic_reg_reservas)
#
# for estudiante in dic_reg_reservas:
#     print(estudiante.name)
#     print(dic_reg_reservas[estudiante][0][0].name)


registro_estudiantes = loadD('e')
est = registro_estudiantes[1]
print(registro_estudiantes)

for estudiante  in dic_reg_reservas:
    print(estudiante)
    print(dic_reg_reservas[estudiante])
    if est.id == estudiante.id:
        print('ES IGUAL')
        print(est)
        print(dic_reg_reservas[est])

# estu_reservas = dic_reg_reservas[est]


# print(estu_reservas)