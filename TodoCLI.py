#author Aaron Montoya Rodriguez

from pymongo import MongoClient
from bson.json_util import dumps
import sys
import random
import string


#MONGO_URL='mongodb://node:nodeuser@mongo:27017'
MONGO_URL= 'mongodb://localhost:27017'

client = MongoClient(MONGO_URL) #conexion a la Base de Datos --- "protocolo://enlace"

db = client['TodoDB'] #Base de Datos para la aplicacion, si existe la usa sino la crea
collection = db['TodoS']#coleccion dentro de la base de datos, si existe la usa sino la crea

#FUNCIONES-------------------------------------------------------------------------------------------------------------------------------

def  POST(content):# funcion para insertar el Todo 

    collection.insert_one({"content" : content}) # inserta el Todo

def GET(type):# devuelve los todos en funcion del tipo de entreega deseada txt,jason,table

    results = collection.find() # obtenemos documentos

    if type == "json":

        json_data = dumps(list(results), indent = 2, sort_keys=True) #obtenemos datos json de results para imprimir
        print (json_data)

    elif type == "txt":

        for doc in results: #recorremos results imprimiendo cada documento
            print(doc)
        
    else:

        if type!="table":
            print ("\nUnknown format, applying default format --> table\n\n")
        
        max_id=0 #maxima longitud del ID del documento
        max_content=0 #maxima longitud del content del documento

        for doc in results: # de esta manera recorremos results una vez y no dos para calcular cada maximo, vamos analizando cada documento de results
            max_id_temp = len(str(doc["_id"]))
            max_content_temp = len(str(doc["content"]))
            # funcion max() desglosada para solo necesitar recorrer una vez todo results
            if max_id_temp > max_id:
                max_id = max_id_temp

            if max_content_temp > max_content:
                max_content = max_content_temp

        print("_id".ljust(max_id)+" | "+"content".ljust(max_content))
        print("-".ljust(max_id,"-")+" | "+"-".ljust(max_content,"-"))

        results = collection.find() 

        for doc in results:
          print(str(doc["_id"]).ljust(max_id)+" | "+str(doc["content"]).ljust(max_content))

def DELETE(ID): # Elimina el Todo deseado
    collection.delete_one({'content' : ID}) # eliminar un Todo 


#OPCIONES DEL CLI (CONSULTA EL MANUAL)---------------------------------------------------------------------------------------------------

if len(sys.argv) < 2:# Filtro argumentos inesperados
    print("Function not covered\nConsult the manual")

elif sys.argv[1] == "-POST": # desencadenamos la opcion POST
     
    if len(sys.argv) != 2: # filtro de argumentos no admite ni mas ni menos argumentos de los necesarios
         print ("\nWrong number of arguments\nConsult the manual")

    else:
        newTodo = input("Give me the Todo you want to POST\n")
        POST(newTodo)  
       
elif sys.argv[1] == "-GET":# desencadena la opcion GET

    if len(sys.argv) == 3: # modo de seleccion de formato de la opcion GET
        GET(sys.argv[2])

    elif len(sys.argv) == 2:# modo por defecto de la opcion -GET

        GET("table")
   
    else: # filtro de argumentos no admite ni mas ni menos argumentos de los necesarios
        print ("\nWrong number of arguments\nConsult the manual")

elif sys.argv[1] == "-DELETE": # desencadena la opcion DELETE

    if len(sys.argv) != 2: # filtro de argumentos no admite ni mas ni menos argumentos de los necesarios
        print ("\nWrong number of arguments\nConsult the manual")
    else:

        GET("txt")
        
        deleteTodo = input("Give me the 'content' of the Todo you want to DELETE\n")
        results = collection.find() 
        DELETE(str(deleteTodo))

elif sys.argv[1] == "-TEST": # desencadena el modo TEST

    if len(sys.argv) != 2: # filtro de argumentos no admite ni mas ni menos argumentos de los necesarios
        print ("\nWrong number of arguments\nConsult the manual")

    else:
        rndTodos = random.randint(10,100) # determinamos el numero de TodoS que se generaran

        for i in range(rndTodos): # generamos los TodoS y realizamos POST con cada uno
            POST(str(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(4,10)))))

        GET("txt")
        GET("json")
        GET("table")

        collection.drop() # eliminamos hasta el ultimo Todo
        collection = db['TodoS'] #restablece la coleccion vacia

else: # Filtro argumentos inesperados
    print("Function not covered\nConsult the manual")


