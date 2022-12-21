from familia.models import Familiar

Familiar(nombre="Cristina", direccion="Bacacay 123", numero_pasaporte=123123).save()
Familiar(nombre="Gustavo", direccion="Bacacay 123", numero_pasaporte=890890).save()
Familiar(nombre="Noelia", direccion="Santiago 123", numero_pasaporte=345345).save()
Familiar(nombre="Juan Manuel", direccion="Santiago 123", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")