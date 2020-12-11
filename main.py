from process.generators import *

sizes = [1000, 10000, 100000, 1000000]
#sizes = [1000]
schema = 'nitrom-e'

for dataSize in sizes:
    generateUsers(schema, dataSize)
    generateEmpresas(schema, dataSize)
    generateDesarrolladores(schema, dataSize)
    generateEditores(schema, dataSize)
    generateGameName(schema, dataSize)
    generateEdicionNormal(schema, dataSize)
    generateEdicionEspecial(schema, dataSize)
    generateCupon(schema, dataSize)
    generateCompra(schema, dataSize)