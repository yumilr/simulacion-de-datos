import os

from random import randint
from random import randrange
from datetime import timedelta
from datetime import datetime
from data import *
import random as rd

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return datetime.strftime(start + timedelta(seconds=random_second), '%Y/%m/%d')   # formato normal ; o ;

# d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')




def checkFolders(schema, dataSize):
    if os.path.isdir(f'{schema}') == False: os.mkdir(f'{schema}')
    if os.path.isdir(f'{schema}/scripts') == False: os.mkdir(f'{schema}/scripts')
    if os.path.isdir(f'{schema}/textFiles') == False: os.mkdir(f'{schema}/textFiles')
    if os.path.isdir(f'{schema}/scripts/{dataSize}') == False: os.mkdir(f'{schema}/scripts/{dataSize}')
    if os.path.isdir(f'{schema}/textFiles/{dataSize}') == False: os.mkdir(f'{schema}/textFiles/{dataSize}')

fNU = None
fNE = None
fNV = None
fC = None

def generateUsers(schema, dataSize):
    checkFolders(schema, dataSize)
    global fNU
    fNU = firstName(dataSize)

    fP = password(dataSize)
    global fC
    fC = email(dataSize)


    file1 = open(f"{schema}/textFiles/{dataSize}/usuarios{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_usuarios{dataSize}.sql","a")
    print("a\n")
    for i in range(dataSize):
        str1 = f"'{fNU[i]}', '{fP[i]}', '{fC[i]}'\n"
        str2 = f"INSERT INTO {schema}.usuario (Nombre, Contrasenia, Correo) VALUES ('{fNU[i]}', '{fP[i]}', '{fC[i]}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateEmpresas(schema, dataSize):
    global fNE
    fNE = companyName(dataSize)
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/empresas{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_empresas{dataSize}.sql","a")
    d1 = datetime.strptime('1/1/1980', '%m/%d/%Y')
    d2 = datetime.strptime('11/1/2016', '%m/%d/%Y')
    for i in range(dataSize):
        fecha = random_date(d1,d2)
        str1 = f"'{fNE[i]}', '{fecha}'\n"
        str2 = f"INSERT INTO {schema}.empresa (Nombre, FechaFundacion) VALUES ('{fNE[i]}', '{fecha}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()
# d1 = datetime.strftime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')

def generateDesarrolladores(schema, dataSize):
    file1 = open(f"{schema}/textFiles/{dataSize}/desarrolladores{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_desarrolladores{dataSize}.sql","a")
    print("a\n")
    global fNE
    rd.shuffle(fNE)
    for i in range(dataSize):
        str1 = f"'{fNE[i]}'\n"
        str2 = f"INSERT INTO {schema}.desarrollador (Nombre) VALUES ('{fNE[i]}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateEditores(schema, dataSize):
    file1 = open(f"{schema}/textFiles/{dataSize}/editores{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_editores{dataSize}.sql","a")
    print("a\n")
    global fNE
    rd.shuffle(fNE)
    for i in range(dataSize):
        str1 = f"'{fNE[i]}'\n"
        str2 = f"INSERT INTO {schema}.editor (Nombre) VALUES ('{fNE[i]}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()


def generateGameName(schema, dataSize):
    global fNV, fNE
    fNV = gameName(dataSize)
    fG = generos()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/games{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_games{dataSize}.sql","a")
    rd.shuffle(fNE)
    d1 = datetime.strptime('1/1/1981', '%m/%d/%Y')
    d2 = datetime.strptime('11/1/2020', '%m/%d/%Y')
    for i in range(dataSize):
        en = fNE[rd.randint(0,dataSize-1)]
        dn = fNE[rd.randint(0,dataSize-1)]
        precio = rd.uniform(5.99,499.99)
        genero = fG[rd.randint(0,len(fG)-1)]
        descargas = rd.randint(0,5000000)
        calific = rd.uniform(0,5)
        fecha = random_date(d1,d2)
        str1 = f"'{en}', '{dn}','{fNV[i]}', {precio}, '{genero}', {descargas}, {calific}, '{fecha}'\n"
        str2 = f"INSERT INTO {schema}.videojuego (ENombre, DNombre, Nombre, Precio, Genero, Descargas, Calificacion, Fecha) VALUES ('{en}', '{dn}','{fNV[i]}', {precio}, '{genero}', {descargas}, {calific}, '{fecha}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateEdicionNormal(schema, dataSize):
    file1 = open(f"{schema}/textFiles/{dataSize}/edicionesNormales{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_edicionesNormales{dataSize}.sql","a")
    print("a\n")
    global fNE,fNV
    rd.shuffle(fNE)
    rd.shuffle(fNV)
    for i in range(dataSize):
        en = fNE[rd.randint(0, dataSize - 1)]
        dn = fNE[rd.randint(0, dataSize - 1)]
        vn = fNV[rd.randint(0, dataSize - 1)]
        str1 = f"'{en}', '{dn}', '{vn}'\n"
        str2 = f"INSERT INTO {schema}.edicionNormal (ENombre, DNombre, Nombre) VALUES ('{en}', '{dn}', '{vn}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateEdicionEspecial(schema, dataSize):
    file1 = open(f"{schema}/textFiles/{dataSize}/edicionesEspeciales{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_edicionesEspeciales{dataSize}.sql","a")
    print("a\n")
    global fNE,fNV
    rd.shuffle(fNE)
    rd.shuffle(fNV)
    fR = recompensas()
    for i in range(dataSize):
        en = fNE[rd.randint(0, dataSize - 1)]
        dn = fNE[rd.randint(0, dataSize - 1)]
        vn = fNV[rd.randint(0, dataSize - 1)]
        recompensa = fR[rd.randint(0, len(fR) - 1)]
        str1 = f"'{en}', '{dn}', '{vn}', '{recompensa}'\n"
        str2 = f"INSERT INTO {schema}.edicionNormal (ENombre, DNombre, Nombre, Recompensa) VALUES ('{en}', '{dn}', '{vn}', '{recompensa}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateCupon(schema, dataSize):
    global fNV, fNE, fC
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/cupones{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_cupones{dataSize}.sql","a")

    d1 = datetime.strptime('1/1/2002', '%m/%d/%Y')
    d2 = datetime.strptime('11/1/2020', '%m/%d/%Y')

    for i in range(dataSize):
        en = fNE[rd.randint(0,dataSize-1)]
        dn = fNE[rd.randint(0,dataSize-1)]
        vn = fNV[rd.randint(0,dataSize-1)]
        correo = fC[rd.randint(0,dataSize-1)]
        descnt = rd.randint(1,99)
        codigo = i+1
        fecha_ini = random_date(d1,d2)
        fecha_fin = random_date(datetime.strptime(fecha_ini, '%Y/%m/%d'),d2)
        str1 = f"{codigo}, '{correo}','{en}', '{dn}', '{vn}', {descnt}, '{fecha_ini}', '{fecha_fin}'\n"
        str2 = f"INSERT INTO {schema}.cupon (Codigo, Correo, ENombre, DNombre, Nombre, PorcentajeDesc, Inicio, Fin) VALUES ({codigo}, '{correo}','{en}', '{dn}', '{vn}', {descnt}, '{fecha_ini}', '{fecha_fin}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateCompra(schema, dataSize):
    global fNV, fNE, fC
    fP = formaDePago()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/compras{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_compras{dataSize}.sql","a")

    d1 = datetime.strptime('1/1/2002', '%m/%d/%Y')
    d2 = datetime.strptime('11/1/2020', '%m/%d/%Y')

    for i in range(dataSize):
        en = fNE[rd.randint(0,dataSize-1)]
        dn = fNE[rd.randint(0,dataSize-1)]
        vn = fNV[rd.randint(0,dataSize-1)]
        correo = fC[rd.randint(0,dataSize-1)]
        formap = fP[rd.randint(0,len(fP)-1)]
        fecha= random_date(d1,d2)
        str1 = f"'{correo}','{en}', '{dn}', '{vn}', '{fecha}', '{formap}'\n"
        str2 = f"INSERT INTO {schema}.compra (Correo, ENombre, DNombre, Nombre, Fecha, FormaDePago) VALUES ('{correo}','{en}', '{dn}', '{vn}', '{fecha}', '{formap}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()


    # MAL ESTRUCTURADO LOS JUEGOS CREACION Y FECHA DE COMPRA!! FALTA CONSTRAINT, TAMBIÉN ESTÁ MAL CUPONES