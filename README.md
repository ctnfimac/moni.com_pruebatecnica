# Prueba Técnica

Tecnologías utilizadas
- [Python](https://www.python.org/) 
- [Django](https://www.djangoproject.com/) 
- [Git](https://git-scm.com/) 
- [Docker](https://www.docker.com/) 
- [Docker compose](https://docs.docker.com/compose/) 

### Instalación
Siga los siguientes pasos:

1) clonar el proyecto:
```
git clone https://github.com/ctnfimac/moni.com_pruebatecnica.git
```

2) me muevo a la carpeta del proyecto
```
cd moni.com_pruebatecnica
```

3) duplicar el archivo ._env y nombrarlo .env, copiar las credenciales (esto no debería estar en el readme)
```
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=monidb
DATABASE_USER=moni
DATABASE_PASSWORD=moni.com
DATABASE_HOST=database
DATABASE_PORT=5432

SECRET_KEY=django-insecure-#qd+)k&ts&%l_d$w+*z^0mqkog$owc0%^+#7+q5nmlwc+jd1^3
```

4) ejecuto el docker-compose para instalar todo
```
docker-compose up
```

5) Cargo los géneros para las pruebas
```
docker exec moni.web python manage.py loaddata web/fixture/Genero.json
```

Para ejecutar las pruebas unitarias:
```
docker exec moni.web python manage.py test
```