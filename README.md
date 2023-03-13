############################
# MANUAL DE USO TodoCLI.py #
############################

ES------------------------------------------------------------------------------------------------------------------------------------------

Consideraciones previas:
     - se entiendo un Todo como una cadena de texto en formato ASCII
     - para el uso de TodoCLI.py es necesaria la instalación de pymongo --> puede instalarse ejecutando el comando "pip install pymongo"

TodoCLI.py presenta 4 funciones diferentes las cuales se detallan a continuación:

1. POST 
    Esta función se encarga de introducir en la colección de nuestra base de datos MongoDB un nuevo TodoCLI,
    tras la ejecución es el propio programa el encargado de solicitar el Todo.
    El comando de ejecución podemos verlo acontinuación:

        > python TodoCLI.py -POST
    
2. GET
    Esta función se encarga de mostrar cada uno de los TodoS de la colección de nuestra base de datos MongoDB.
    Permite obtenerlo en formato txt, json y tabla, siendo esta ultima la opción por defecto.
    El comando de ejecución podemos verlo acontinuación:

        > python TodoCLI.py -GET [format]		[format]: txt | json | table 

3. DELETE 
    Esta función se encarga de mostrarnos cada uno de los TodoS de la colección de nuestra base de datos MongoDB,
    para posteriormente poder seleccionar uno mediante el "_id"  y eliminarlo.
    El comando de ejecución podemos verlo acontinuación:

        > python TodoCLI.py -DELETE

4. TEST
    Esta función se encarga de realizar el test de la aplicación y actua de la siguiente manera:

        - Crea un número aleatorio de Todos entre 10 y 100.
        - Consigue todos los TodoS en formato de texto.
	- Consigue todos los TodoS en formato json.
	- Consigue todos los TodoS en formato tabla.
        - Limpia todos los Todos almacenados.

    El comando de ejecución podemos verlo acontinuación:

        > python TodoCLI.py -TEST

EN------------------------------------------------------------------------------------------------------------------------------------------

Previous considerations:
     - a Todo is understood as a text string in ASCII format
     - for the use of TodoCLI.py ​​it is necessary to install pymongo --> it can be installed by executing the command "pip install pymongo"

TodoCLI.py ​​has 4 different functions which are detailed below:

1.POST
    This function is responsible for introducing a new TodoCLI into the collection of our MongoDB database,
    after execution, the program itself is in charge of requesting the All.
    The execution command can be seen below:

        > python TodoCLI.py -POST

2.GET
    This function is responsible for displaying each of the TodoS in the collection of our MongoDB database.
    It allows obtaining it in txt, json and table format, the latter being the default option.
    The execution command can be seen below:

         > python TodoCLI.py -GET [format]		[format]: txt | json | table 

3. DELETE
    This function is responsible for showing us each of the TodoS in the collection of our MongoDB database,
    to later be able to select one by means of the "_id" and delete it.
    The execution command can be seen below:

        > python TodoCLI.py -​​DELETE

4. TEST
    This function is responsible for testing the application and acts as follows:

        - Create a random number of All between 10 and 100.
        - Get all Todos in text format.
	- Get all TodoS in json format.
	- Get all the TodoS in table format.
        - Clears all stored Todos.

    The execution command can be seen below:

        > python TodoCLI.py -​​TEST
