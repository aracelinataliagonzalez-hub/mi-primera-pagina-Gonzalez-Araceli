#
Mi Primera Página – Proyecto Django
Descripción General

Este proyecto corresponde al Trabajo Práctico del curso Programación en Python dictado por Coderhouse.
El objetivo principal es desarrollar una aplicación web utilizando el framework Django, implementando sus conceptos fundamentales: estructura del proyecto, creación de aplicaciones, rutas, vistas, modelos, plantillas y base de datos.

La aplicación implementada incluye páginas de ejemplo y funcionalidades básicas que permiten comprender el flujo completo de trabajo dentro de un proyecto Django.

Características del Proyecto

Estructura de proyecto generada con django-admin startproject.

Aplicación interna denominada inicio.

Uso de vistas basadas en funciones (FBV).

Enrutamiento mediante el archivo urls.py principal y el de la aplicación.

Utilización de templates HTML para renderizar contenido dinámico.

Base de datos SQLite3, por defecto en Django.

Archivos separados para configuración, vistas, modelos y migraciones.

Estructura del Repositorio

El proyecto contiene los siguientes directorios principales:

mi-primera-pagina-Gonzalez-Araceli/
│
├── inicio/                  # Aplicación principal del proyecto
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/              # Archivos HTML del proyecto
│   ├── inicio.html
│   ├── listado_pizzas.html
│   └── pedido.html
│
├── seguimiento/            # Configuración general del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3              # Base de datos
├── manage.py               # Comando para gestionar el proyecto
└── requirements.txt        # Dependencias del proyecto

Requisitos Previos

Para ejecutar el proyecto es necesario contar con:

Python 3.10 o superior

Django 5.x

Entorno virtual recomendado (venv)

Instalación de dependencias:

pip install -r requirements.txt

Ejecución del Proyecto

Clonar el repositorio:

git clone https://github.com/aracelinataliagonzalez-hub/mi-primera-pagina-Gonzalez-Araceli.git


Acceder al directorio del proyecto:

cd mi-primera-pagina-Gonzalez-Araceli


Ejecutar el servidor de desarrollo:

python manage.py runserver


Acceder a la aplicación desde un navegador web:

http://127.0.0.1:8000/

video de la pagina: 

https://youtu.be/vKHuVgALcJw

Objetivo Educativo

Este trabajo práctico tiene como propósito:

Comprender la arquitectura MVC/MVT de Django.

Implementar una aplicación mínima funcional.

Practicar la gestión de rutas, vistas y plantillas.

Utilizar la base de datos por defecto y las migraciones.

Familiarizarse con el flujo general de desarrollo Django.

Autor

Araceli González
Proyecto presentado para el curso Programación en Python – Coderhouse.
#
