Proyecto Prueba Analista de Software

Resumen:
se entrega un proyecto que permite listar, editar y crear roles

Consideraciones entrega del proyecto:
1- Se cambio el modelo de User, eliminando el parametro de Permission(many-to-may), debido a que Role ya lo contenia, entonces seria redundante

2- Para simplificar el proyecto, el modelo Role, solo permite almacenar 1 solo permiso. El almacenamiento de varios permisos quedo para una futura entrega

3- Debido a que el Role tiene nombre único y que sólo tiene 1 permiso, no se vio la necesidad de crear un endpoint de clonacion

4- Debido a que el modelo de Usuario tiene el campo Role tipo many-tomany , no se puede asignar una autenticación, ya para crear un Role, se requiere un usuario, pero para crear un usuario se requiere que el campo Role no esté vacio, se sugiere que se añada otro modelo llamado Employe (con Role, name, etc.) y que también se tenga el modelo usuario (username, password) solo para la autenticación.

Requerimientos:
1-Node 16 o superior
2-npm
Instalación

1-Front-End
Abrir una terminal ubicada en la carpeta del Front (client) y ejecutar npm install, aqui un ejemplo
...\Prueba\client>npm install

2-Back-End
Abrir una terminal ubicada en la carpeta principal del proyecto ejecutar el siguiente comando
...\Prueba>python -m pip install -r requirements.txt

Ejecución
ejecutar el Backend: abrir una terminal ubicada en la carpeta principal del proyecto (Prueba) y ejecutar el comando python manage.py runserver

Ejecutar el front: abrir una nueva terminal(y sin cerrar la anterior) dirigirse la carpeta client y ejecurtar el comando npm run dev