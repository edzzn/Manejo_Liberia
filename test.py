from CoreData import loadD


registros = loadD('r')
dic_reg_reservas = registros.reg_reservas

print(dic_reg_reservas)

for estudiante in dic_reg_reservas:
    print(estudiante.name)
    print(dic_reg_reservas[estudiante][0][0].name)
