from faker import Faker
import string
import random as rd

fake = Faker(['it_IT', 'en_US', 'es_ES', 'es_MX'])

def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(rd.choice(letters) for i in range(stringLength))

def firstName(size):
    return [fake.name()+randomString(6) for _ in range(size)]

def gameName(size):
    return [fake.license_plate() for _ in range(size)]

def companyName(size):
    return [fake.company()+randomString(6) for _ in range(size)]

def password(size):
    return [fake.swift() for _ in range(size)]

def email(size):
    return [fake.free_email()+randomString(6) for _ in range(size)]

def codigo(size):
    return [i for i in range(size)]

def formaDePago():
    return['Credit','Debito','Paypal','Yape','Toke','Tunqui']

def generos():
    return['Terror','Plataformas','RPG','Retro','Carreras','Espacio','Futbol', 'Peleas', 'Fantasía', 'Otome', 'Multijugador', 'Accion']

def recompensas():
    return['Skin','Dinero','Cofre Misterioso','Elixir','Vida','Habilidad','Mapa Desbloqueado', 'Gemas']

