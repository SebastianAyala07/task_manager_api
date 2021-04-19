# Task Manager API

_Api para gestionar las tareas por usuario y su estado._

## Comenzando 🚀

_Luego de clonado el repositorio sera necesario crear un ambiente de desarrollo con python 3_
_Y se deberan instalar los requerimientos que estan contemplados en el archivo requirements.txt con el siguiente comando dentro del directorio donde esta el manage.py_

```
$ python -m pip install -r requirements.txt
```


### Levantar el servidor 📋

_Requiere realizar los siguientes pasos_

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Ejecucion de Tests 🔧

_Para ejecutar los tests debe ejecutar el siguiente comando_

```
$ python manage.py test
```

## Rutas de api


_Estas rutas tienen el prefijo en la url 'api'_

```
127.0.0.1:8000/api/
```

_Las rutas son las siguientes_

```
127.0.0.1:8000/api/tasks/
127.0.0.1:8000/api/tasks/list/
```

*La primera ruta acepta lo metodos POST, PUT, PATCH Y DELETE*

*La segunda ruta acepta el metodo GET*

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Django Rest Framework](https://www.django-rest-framework.org/) - El framework web usado
* [Swagger](https://drf-yasg.readthedocs.io/en/stable/index.html) - Auto Documentación del API


## Autor ✒️


* **Sebastian Ayala Gonzalez** - *Backend Developer* - [LinkedIn](https://www.linkedin.com/in/sebastianayala7/)

---
_Sebastian Ayala Gonzalez - Backend Developer_