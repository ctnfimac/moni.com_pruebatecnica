import requests


def aprobacion_del_prestamo(dni:str):
    """
    realiza una peticion a la api de moni.com.ar para verificar si el usuario
    que esta realizando un prestamo puede ser aceptado o no
    """
    try:
        url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
        parametros = {'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
        respuesta = requests.get(url, params=parametros)
        respuesta = respuesta.json()

        return respuesta
    except requests.exceptions.RequestException as e:
        print(e.__str__())
        return {'status':'Error'}