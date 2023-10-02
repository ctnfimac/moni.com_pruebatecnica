from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import User
from web.models.genero import Genero
from web.models.prestamo import Prestamo
from web.models.usuario import Usuario
from web.forms.prestamoEditarForm import PrestamoEditarForm


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

        # creo un usuario administrador para las prueba del 
        # administrador de prestamos
        cls.administrador = User.objects.create_user(
            username='christian',
            password='christian1234',
            is_staff=True,
            is_superuser=True
        )


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


    def test_administrador_listar_prestamos(self):
        # simulo que inicie sesion
        self.client.login(username='christian',password='christian1234')

        url = reverse('web:administrador')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        elementos = response.context['object_list']
        self.assertEqual(len(elementos), 1)


    def test_administrador_editar_prestamo(self):
        # simulo que inicie sesion
        self.client.login(username='christian',password='christian1234')
        
        # simulo cuando elijo el registro para editar
        url = reverse('web:editar_prestamo', args=[self.prestamo_nuevo.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
        # corroboro que al elegir el registro se utilice el form correcto
        self.assertIsInstance(response.context['form'], PrestamoEditarForm)
        data = {'monto': 66000}
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('web:administrador'))

        # actualizo el prestamo en la base de datos y corroboro que se haya realizado el cambio
        self.prestamo_nuevo.refresh_from_db()
        self.assertEqual(self.prestamo_nuevo.monto, 66000)



    def test_administrador_eliminar_prestamo(self):
        self.client.login(username='christian',password='christian1234')
        url = reverse('web:eliminar_prestamo', args=[self.prestamo_nuevo.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # simula que acepte la elimincación
        response = self.client.post(url, follow=True)
        # redirijo a la vista exitosa
        self.assertRedirects(response, reverse('web:administrador'))
        # verifico que ya no exista el prestamo eliminado
        self.assertFalse(Prestamo.objects.filter(pk=self.prestamo_nuevo.pk).exists())

