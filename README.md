# Prueba para Analista de Software
## Resumen
Este proyecto de forma visual permite listar, editar y crear roles. También hay endpoints para listar, crear, editar y eliminar permisos y usuarios

## Consideraciones del Proyecto
### Cambio en el Modelo de Usuario:
- Se eliminó el parámetro de permisos (many-to-many) del modelo User, ya que el modelo Role ya lo contenía, evitando así redundancias.

### Simplificación del Modelo Role:
- El modelo Role actualmente permite almacenar un solo permiso. La capacidad de almacenar varios permisos se implementará en una futura versión.

### Endpoint de Clonación:
- Dado que Role tiene un nombre único y solo un permiso, no fue necesario crear un endpoint de clonación.

### Asignación de Roles y Autenticación:
- En el modelo User existe un campo Role como many-to-many, lo que impide asignar autenticación directamente. Para crear un Role, se requiere un User, pero para crear un User se requiere que el campo Role no esté vacío.
- Se sugiere añadir un modelo llamado Employee (con campos como Role, name, etc.) y mantener el modelo User (con username, password) solo para autenticación.
  
## Requerimientos
Node.js 16 o superior
npm
python
pip

## Instalación
Front-End
Abrir una terminal en la carpeta del cliente (client) y ejecutar:`npm install`ejemplo
```
...\Prueba\client>npm install
```
Back-End
Abrir una terminal en la carpeta principal del proyecto y ejecutar `python -m pip install -r requirements.txt` ejemplo:
```
...\Prueba>python -m pip install -r requirements.txt
```

##Ejecución
1- Abrir una terminal en la carpeta principal del proyecto (Prueba) y ejecutar
```
python manage.py runserver
```
2- Abrir una nueva terminal (sin cerrar la anterior), dirigirse a la carpeta client y ejecutar
```
npm run dev
```
