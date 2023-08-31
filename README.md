# Proyecto Django-académico #14
Proyecto web creado utilizando el framework de desarrollo Django

## Integrantes
- Ulises Palazzo
- Lina Mendieta
- Julio Duhalde
- Timoteo Pregot
- Ramiro Burgos

## Indice
- [Instalación de entorno para desarrollo](#instalación-de-entorno-para-desarrollo)
    - [Pre-requisitos](#pre-requisitos)
    - [Pasos](#pasos)

# Instalación de entorno para desarrollo
El repositorio es publico y de finalidad académica, cualquiera que desee desarrollar sobre este proyecto debe seguir los siguientes pasos.

## Pre-requisitos
- Python3 (version utilizada 3.10)
- virtualenv (version utilizada 20.17.1) #opcional
- Git (version utilizada 2.34.1)
- 

## Pasos

#### Clonar el repositorio
~~~ git
git clone https://github.com/pala83/Django-cac.git
~~~

#### Crear un entorno virtual y activarlo
~~~ git
cd Django-cac
python3 -m venv venv
~~~
> activacion en windows
~~~ git
cd .\venv\Scripts
.\activate
cd ../..
~~~
> activacion en linux
~~~ git
source venv/bin/activate
~~~

#### instalar dependencias
~~~ git
pip install -r requirements.txt
~~~

#### Variables de entorno
necesarias para poder utilizar el proyecto
> Solicitar el archivo .env al dueño del repositorio
- Pegar el archivo **.env** dentro de la carpeta ecommerce/ecommerce/
