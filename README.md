# Evaluacion_Modulo6_Python_Django
# Correr el programa
Tendras que crearte un ambiente virtual con el comando Python -m venv "nombre del anmbiente virtual" sin "" y con _ si es texto concadenado
luego tendras que inicializar el ambiente con el comando nombre_ambiente\Scripts\activate ,
una ves activado tendras que instalar django de la siguiente manera pip install django 
y una ves instalado podras correr el servidor posicionandote en la carpeta donde esta el manage.py y ejecutaras el comando python manage.py runserver ,
haces click en la url que te muestra en la consala y tendras el progrma corriendo 

# Views.py 
En el archivo view.py en la aplicacion de tareas estan las funcionalidades principales para renderizar las templates segun corresponda 
las cuales algunas no se pueden entrar antes sin estar auntentificado, como por ejemplo al index si no estas autentificado te redirige para que puedas iniciar 
session y por verlo, al estar auntentificado podras ver el index, agregar tareas, verlas y eliminarlas que de otra manera te mandarian esas vistas 
a iniciar session, tambien agregue funcionalidades para el error 403 y el 404 en caso que ocurran, como tambien las funcionalidades para agregar y elimninar tareas en memoria.

# urls.py 
Se configuraron todas las urls para que tenga un correcto funcionamiento el sistema y sepa donde ir en todo momento 

# Usuarios
Se hizo una migracion con el comando python manage.py makemigrations y python manege.py migrate , para hacer funcionar todo el sistema de 
usuarios, como la creacion de un CustomUsuario en el models.py para añadirle permisos custom.

#usuarios de prueba si no borras la db y no haces migraciones denuevo
username: prueba1
pass: asdfgh123456

susername: prueba2
pass: asdfgh123456

