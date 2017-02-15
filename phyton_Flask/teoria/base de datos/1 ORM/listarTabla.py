# Crea el esquema de la base de datos
from User import db, User

print(User.query.all())
