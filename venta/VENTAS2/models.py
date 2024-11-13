from django.db import models

# Cliente Model
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Categoria Model
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Producto Model
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.RESTRICT)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Factura Model
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='facturas', on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)  # 1% discount

    def calcular_total_con_descuento(self):
        return self.total * (1 - (self.descuento / 100))

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"


