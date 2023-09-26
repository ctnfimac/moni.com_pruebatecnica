from django.test import TestCase
from django.urls import reverse
import json
from web.models.genero import Genero
from web.models.prestamo import Prestamo
from web.models.usuario import Usuario


class PrestamoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.tipo1 = Genero.objects.create(tipo='Femenino')
        cls.tipo2 = Genero.objects.create(tipo='Masculino')

        cls.usuario_nuevo = Usuario(
            dni= '35669411', 
            email= 'test@gmail.com', 
            nombre= 'ramon', 
            apellido= 'valdez', 
            genero= cls.tipo2 
        )
        cls.usuario_nuevo.save()

        cls.prestamo_nuevo = Prestamo(
            monto= 8000,
            usuario=cls.usuario_nuevo
        )

        cls.prestamo_nuevo.save()


    def test_pedido_de_prestamo_correcto(self):
        url = reverse('web:solicitar_prestamo')

        datos = {
            'dni': '93667150', 
            'email': 'curly@gmail.com', 
            'nombre': 'Curly', 
            'apellido': 'Chiflado', 
            'genero': '1', 
            'monto': 4000,
        }

        response = self.client.post(url, datos)
        #response_data = json.loads(response.content)
        
        # me aseguro que la respuesta de la peticion es correcta
        self.assertEqual(response.status_code, 201)

        # verifico si se creo el prestamo
        self.assertEqual(Prestamo.objects.count(), 2)

        # verifico si el prestamo se guardo correctamente
        prestamo = Prestamo.objects.all()[1]
        self.assertEqual(prestamo.monto, 4000)
        self.assertEqual(prestamo.usuario.dni, '93667150')
        self.assertEqual(prestamo.usuario.nombre, 'Curly')
        self.assertEqual(prestamo.usuario.apellido, 'Chiflado')
        self.assertEqual(prestamo.usuario.email, 'curly@gmail.com')
        self.assertEqual(prestamo.usuario.genero.tipo, 'Femenino')


    def test_pedido_de_prestamo_monto_incorrecto(self):
        url = reverse('web:solicitar_prestamo')

        datos = {
            'dni': '93667150', 
            'email': 'curly@gmail.com', 
            'nombre': 'Curly', 
            'apellido': 'Chiflado', 
            'genero': '2', 
            'monto': 0,
        }

        response = self.client.post(url, datos)
        self.assertEqual(response.status_code, 400)

