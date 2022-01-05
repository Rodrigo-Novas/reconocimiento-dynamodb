# Dynamo DB

Dynamo db es un motor NOsql, de datos semistructurados como yaml y json. Usa clave-valor

## Estructura

DynamoDB utiliza una variacion de JSON para lamacener los datos:

<ul>
    <li>Table: DynaoDB no es una base de datos cada tabla es independiente y no pueden ser unidas mediante joins</li>
    <li>Items: Cada registro se considera un item</li>
    <li>Items: Cada columna de cada registro es un atributo</li>
</ul>


## USOS DE DynamoDB

<ul>
    <li>MicroServicios</li>
    <li>IOT</li>
    <li>Event Driven  Arichitecture<li>
</ul>

## USOS NO optimos

<ul>
    <li>Data Analytics</li>
    <li>Data Science</li>
</ul>

# Leyendo y escribiendo datos

Dynamo tiene un limite de 400 kb por item (sucede porque dynamo esta diseñado para trabajar con registros chicos y asi asegurar rapidez), sin embargo lee y escribe en pedazos distribuidos de la siguiente manera.
DynamoDB cobra por lectura y escritura.
<ul>
    <li>Escribe en pedazos de 1kb</li>
    <li>Lee en pedazos de 4kb</li>
</ul>

# Consistencia

Hay que ser cuidadoso con cual usar porque dependiendo la consistencia se utilizara mas o menos read capacity units.
Strong consistency es el doble de costoso que eventualmente consistente y consistencia transaccional es el doble que strong consinstence. Dependiendo el tipo de consistencia va a salir mas caro. 

Eventualmente consistente es lo recomendable en el mundo de microservercios.

<https://docs.informatica.com/integration-cloud/cloud-data-integration-connectors/current-version/amazon-dynamodb-connector/synchronization-tasks-with-amazon-dynamodb-connector/amazon-dynamodb-sources-in-synchronization-task/read-capacity-unit.html#:~:text=For%20Amazon%20DynamoDB%20Connector%2C%20the,8%20KB%20for%20that%20table.>

DynamoDB tiene 3 niveles de consistencia:

Eventualmente consistente: Dynamo tiene una copia maestra que es donde los datos llegan y se depositan y hay 5 replicas dentro de esas 5 replicas puede ser que la lectura venga de una replica donde el cambio no ha llegado por eso se le llama eventualmente consistente. EVENTUALMENTE SE VA A OBTENER EL ULTIMO REGISTRO PUEDE SER QUE NO SEA AHORA O PUEDE SER EN 5 MINUTOS, EL TIEMPO ES VARIABLE.

Fuertemente consistente: Si se necesita encontrar exactamente el ultimo registro se debe especificar que se necesita una query strongly consistent.

Transaccion consistente: DynamoDB asegura que la transaccion no se va a marcar como completada hasta que los datos no sean correctamente completadas en todas las replicas.


# COSTOS

<table>
    <thead>
        <th>
        Consistencia
        </th>
        <th>
        Escritura
        </th>
        <th>
        Lectura
        </th>
    </thead>
    <tbody>
    <tr>
        <td>
        Eventual consistency
        </td>
        <td>
        1kb=1wcu
        </td>
        <td>
        4kb = 1 rcu
        </td>
        </tr>
    <tr>
        <td>
        Strong Consistency
        </td>
        <td>
        1kb=2wcu
        </td>
        <td>
        4kb = 2 rcu
        </td>
        </tr>
        <tr>
        <td>
        Transactional Consistency
        </td>
        <td>
        1kb=4wcu
        </td>
        <td>
        4kb = 4 rcu
        </td>
        </tr>
    <tbody>
</table>


# Trabajando con DynamoDB localmente

## Requisistos:

Docker o JRE

DynamoDB-ADMIN 
Python
Boto3 - Libreria de AWS para Python

# AWS DYNAMO

Crear tabla

Nombre de tabla: sin espacios con snake case


# CLAVE PRIMARIA

BUENA PRACTICA = CLAVE PRIMARIA COMPUESTA POR PARTICION Y ORDENACION

Hay dos tipos de claves primarias. Una clave primaria simple usa un solo atributo para identificar un elemento, como un nombre de usuario o un Id. De pedido. Usar una tabla de DynamoDB con una clave primaria simple es similar a usar la mayoría de los almacenes de clave-valor simples, como Memcached.

Una clave primaria compuesta usa una combinación de dos atributos para identificar un artículo en particular. El primer atributo es una clave de partición (también conocida como "clave hash") que se utiliza para segmentar y distribuir elementos entre fragmentos. El segundo atributo es una clave de clasificación/ordenacion (también conocida como "clave de rango") que se utiliza para ordenar artículos con la misma clave de partición. Una tabla de DynamoDB con una clave primaria compuesta puede utilizar patrones de consulta interesantes más allá de las simples operaciones de obtención / configuración.

Clave de partición: Sin mayusculas y con snake case. Tiene que ser una llave de particion relacionada con el nombre de la tabla.

Clave de ordenación: Sin mayusculas y con snake case. Puede ser un string un numero o un booleano.

# ATRIBUTOS

ATRIBUTOS = COLUMNAS EN SQL RELACIONAL

Un artículo se compone de atributos , que son diferentes elementos de datos sobre un artículo en particular. Por ejemplo, un elemento de la tabla Usuario puede tener un atributo de Nombre, un atributo de Edad, un atributo de Dirección y más. Son comparables a las columnas de una base de datos relacional.

La mayoría de los atributos de una tabla de DynamoDB no son obligatorios para todos los elementos. DynamoDB es una base de datos NoSQL que permite un modelo de datos más flexible que las bases de datos relacionales estándar. Puede almacenar tipos de objetos completamente diferentes en una sola tabla de DynamoDB, como un objeto Coche con atributos Marca, Modelo y Año, y un objeto Mascota con atributos Tipo, Raza, Edad y Color. Esta es una práctica común, ya que a menudo tendrá varios tipos de entidades diferentes en una sola tabla.

EJ:
{
    "Name": { "S": "Alex DeBrie" },
    "Age": { "N": "29" },
    "Roles": { "L": [{ "S": "Admin" }, { "S": "User" }] }
}

# CREAR ELEMENTOS

Un elemento en DynamoDB es un documento en mongodb, es decir un registro en una tabla relacional.

En DynamoDB para crear un elemento se debe dirigir a la tabla - ver elementos - crear elementos.

Al dar click se abrira una consola donde podremos modificar el DynamoJson.

El dynamoJson tiene algunas caracteristicas especiales:

Su sintaxys es casi identica a la de mongo pero al ser semistructurado s ele puede indicar el tipo de dato: Bynario numerico o cadena.

EJ: En este caso "S" es el tipo de dato string y "B" es el tipo de dato binario.

{
  "score_tag": {
    "S": "gamer123"
  },
  "win": {
    "B": "dHJ1ZQ=="
  }
}

### Generar atributos cadena:
Identificador: "S"
El tipo de cadena es el tipo de datos más básico y representa una cadena Unicode con codificación UTF-8.

"Name": { "S": "Alex DeBrie" }

### Para generar un atributo booleano:

Identificador: "BOOL"

"IsActive": { "BOOL": "false" }

Para generar un binario:

### Los atributos Binarios:

Identificador: "B"

<https://magic-flask.herokuapp.com/Conversor>

Se puede utilizar DynamoDB para almacenar datos binarios directamente, como una imagen o datos comprimidos. Generalmente, los blobs binarios más grandes deben almacenarse en algo como Amazon S3 en lugar de DynamoDB para permitir un mayor rendimiento, pero puede usar DynamoDB si lo desea.

" BLOB son las siglas de Binary Large Object o, en español, objeto binario grande. Es un término que se usa para almacenar un elemento grande de datos en una base de datos que está en código binario "


"SecretMessage": { "B": "bXkgc3VwZXIgc2VjcmV0IHRleHQh" }

### TIPO NULL

Identificador: "NULL"

ES ALTAMENTE RECOMENDABLE NO USARLO. almacena un bool con identificador especial.

"OrderId": { "NULL": "true" }


### TIPO LISTA

Identificador: "L"

"Roles": { "L": [ "Admin", "User" ] }


### TIPO MAPA

Identificador: "M"

Son diccionarios en python.

"FamilyMembers": {
    "M": {
        "Bill Murray": {
            "Relationship": "Spouse",
            "Age": 65
        },
        "Tina Turner": {
            "Relationship": "Daughter",
            "Age": 78,
            "Occupation": "Singer"
        }
    }
}


### TIPO ARRAY DE STRINGS

Identificador: "SS"

"Roles": { "SS": [ "Admin", "User" ] }



### TIPO ARRAY DE NUMEROS

Identificador: "NS"

"Roles": { "NS": [ 23, 50 ] }


### TIPO ARRAY DE BINARIOS

Identificador: "BS"

"SecretCodes": { "BS": [ 
	"c2VjcmV0IG1lc3NhZ2UgMQ==", 
	"YW5vdGhlciBzZWNyZXQ=", 
	"dGhpcmQgc2VjcmV0" 
] }



# INDICES

DynamoDB posee índices secundarios . Los índices secundarios le permiten especificar estructuras de claves alternativas que se pueden utilizar en operaciones de consulta o exploración (pero no en operaciones de GetItem).

La ventaja que da es que te permite realizar busquedas mas rapidas, ya que en lugar de hacer una consulta a un conjunto de datos entero lo haces para el indice (que previamente va a tener solo las columnas que seleccionaste)

## TIPOS DE INDICES


Hay dos tipos de índices secundarios: índices secundarios locales e índices secundarios globales .

Los índices secundarios locales se pueden usar en una tabla con una clave primaria compuesta para especificar un índice con la misma clave HASH pero una clave RANGE diferente para una tabla. Esto es útil si por ej queremos dividir nuestros datos por nombre de usuario, pero queremos recuperar elementos por un atributo diferente (Cantidad).

Los índices secundarios globales se pueden utilizar para especificar una estructura de claves completamente diferente para una tabla. Si tuviera una tabla con una clave primaria compuesta, podría tener un índice secundario global con una clave simple. O bien, puede agregar un índice secundario global con una clave HASH y una clave RANGE completamente diferentes. Si su tabla tiene una clave primaria simple, puede agregar un índice secundario global con una estructura de clave compuesta.

Los índices secundarios son muy poderosos y permiten una estructura de consulta mucho más flexible.


Para crear un indice global debemos dirigirnos a la tabla y luego a indices - crear indices

Una vez hecho esto se coloca una clave de particion y de ordenacion para el indice


## CARACTERISTICAS DE LOS TIPOS
LSI - Local Secondary Index

<ul>
    <li>Requiere la llave de particion tiene que ser identica a la tabla</li>
    <li>La clave de ordenacion puede ser diferente</li>
    <li>Creacion solo durante la creacion de la tabla</li>
    <li>Maximo 5 por tabla</li>
    <li>Hace campos mandatorios</li>
</ul>


GSI - Global Secondary Index

<ul>
    <li>Pueden contener una estructura totalmente distinta a la tabla</li>
    <li>La clave de particion puede ser diferente</li>
    <li>La clave de ordenacion puede ser diferente</li>
    <li>Maximo 2 por tabla</li>
    <li>Pueden crearse independientemente</li>
</ul>



# CORRER DYNAMODB LOCAL

Se haran las consultas localmente pero aws no va a cobrarlas ya que no hay interfaz de por medio

# EJECUTAR DOCKER COMPOSE
antes hay que crear la ruta .\docker\dynamodb
docker-compose up -d



# COMANDOS CLI

## CRUD


### CREATE TABLE

Al crear una tabla, deberá proporcionar **AttributeDefinitions** para cada atributo que necesite definir. Una definición de atributo incluye el nombre y el tipo del atributo. Para nosotros, esto significa que tenemos un atributo con el nombre "Username" y de tipo "S", para String. Solo necesita definir los atributos que se usan en su clave principal o que se usan en índices secundarios.

Luego deberá proporcionar el **KeySchema** de su tabla. Aca es donde define su clave principal, incluida una clave HASH y una clave RANGE opcional. En este ejemplo, estamos usando una clave primaria simple, por lo que solo usamos el nombre de usuario como una clave HASH.

Finalmente, deberá especificar un **TableName** y **ProvisionedThroughput** para su tabla. Mantendremos las unidades de capacidad de lectura y escritura en 1.

Comando:

aws dynamodb create-table \
  --table-name UsersTable \
  --attribute-definitions '[
    {
        "AttributeName": "Username",
        "AttributeType": "S"
    }
  ]' \
  --key-schema '[
    {
        "AttributeName": "Username",
        "KeyType": "HASH"
    }
  ]' \
  --provisioned-throughput '{
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }' \
  $LOCAL

### INSERTAR ELEMENTO

Se utiliza el comando put-item

Con la llamada PutItem, proporciona un elemento completo para colocarlo en su tabla de DynamoDB. Esta acción creará un nuevo elemento si no existe ningún elemento con la clave principal dada, o sobrescribirá un elemento existente si ya existe un elemento con esa clave principal.

En este caso estamos agregando un elemento para el atributo clave principal Username

aws dynamodb put-item \
    --table-name UsersTable \
    --item '{
      "Username": {"S": "alexdebrie"}
    }' \
    $LOCAL

aws dynamodb put-item \
    --table-name UsersTable \
    --item '{
      "Username": {"S": "Rodrigo"}
    }' \
    $LOCAL

Agreguemos mas atributos (campos/columnas)

aws dynamodb put-item \
    --table-name UsersTable \
    --item '{
      "Username": {"S": "JulianPal"},
      "Name": {"S": "Julian"},
      "Age": {"N": "31"}
    }' \
    $LOCAL

### READ

Se utiliza el comando get-item

Vamos a leer los elementos del atributo primary key UserName que sea JulianPal

aws dynamodb get-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "JulianPal"}
    }' \
    $LOCAL

Use la **--projection-expression** opción para devolver solo elementos particulares de un artículo

aws dynamodb get-item \
    --table-name UsersTable \
    --projection-expression "Age, Username" \
    --key '{
      "Username": {"S": "JulianPal"}
    }' \
    $LOCAL

PARA LEER TODA LA TABLA (SELECT * FROM NOMBRETABLA) SE UTILIZA EL COMANDO SCAN

aws dynamodb scan --table-name UsersTable

### UPDATE

La cláusula de actualización más común es "SET", que se utiliza para agregar un atributo a un artículo si el atributo no existe o para sobrescribir el valor del atributo existente si existe.

Volviendo a nuestros ejemplos iniciales de PutItem, quizás queramos tener un atributo DateOfBirth para nuestros usuarios. Sin la acción UpdateItem, necesitaríamos recuperar el Item con una llamada GetItem y luego reinsertar el Item con un atributo DateOfBirth a través de una llamada PutItem. Con la llamada UpdateItem, podemos simplemente insertar el DateOfBirth directamente:

aws dynamodb update-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "JulianPal"}
    }' \
    --update-expression 'SET #dob = :dob' \
    --expression-attribute-names '{
      "#dob": "DateOfBirth"
    }' \
    --expression-attribute-values '{
      ":dob": {"S": "1937-04-17"}
    }' \
    $LOCAL


## REMOVE ATRIBUTO

La cláusula REMOVE es lo opuesto a la cláusula SET: elimina un atributo de un elemento si existe.

Usémoslo aquí para eliminar el atributo "DateOfBirth" que acabamos de agregar. También vamos a agregar una --return-valuesopción para que DynamoDB nos devuelva el elemento después de la actualización para que no tengamos que hacer una llamada GetItem por separado. La --return-valuesopción tiene diferentes opciones, que incluyen devolver el artículo antiguo antes de los cambios o devolver solo los atributos actualizados antes de que se cambiaran. Aquí, solo usaremos la opción "ALL_NEW" para mostrar el elemento tal como existe después de la operación:

aws dynamodb update-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "JulianPal"}
    }' \
    --update-expression 'REMOVE #dob' \
    --expression-attribute-names '{
      "#dob": "DateOfBirth"
    }' \
    --return-values 'ALL_NEW' \
    $LOCAL


## DELETE ELEMENT

La última acción de un solo elemento a cubrir es DeleteItem. Habrá ocasiones en las que desee eliminar elementos de sus tablas, y esta es la acción que utilizará.

La acción DeleteItem es bastante simple: solo proporcione la clave del elemento que desea eliminar:

aws dynamodb delete-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "alexdebrie"}
    }' \
    $LOCAL



### EXPRESIONES PARA LEER ELEMENTOS EN LAS TABLAS

Las expresiones son cadenas que utilizan la lógica de expresión específica del dominio de DynamoDB para comprobar la validez de una declaración descrita. Con las expresiones, puede utilizar símbolos de comparación, como "=" (igual a), ">" (mayor que) o "> =" (mayor o igual que).

Para usar nombres de atributos de expresión, pasa un mapa (diccionario) donde la clave es el marcador de posición para usar en su expresión y el valor es el nombre del atributo al que desea expandir. Por ejemplo, si quisiera usar un marcador de posición de "#a" para mi nombre de atributo de "Edad", mi mapa de nombres de atributo de expresión se vería así:


 --expression-attribute-names '{
    "#a": "Age"
  }'

Entonces, podría usar "#a" en mi expresión cuando quisiera referirme al atributo Edad.

Cuando se utilizan nombres de atributos de expresión, el marcador de posición debe comenzar con un signo de almohadilla ("#").

En el ejemplo "GetItem" de la lección anterior, usamos la **--projection-expression** para devolver un subconjunto de los atributos del elemento. Para modificarlo para usar nombres de atributos de expresión, la llamada a la API se vería así:

aws dynamodb get-item \
    --table-name UsersTable \
    --projection-expression "#a, #u" \
    --expression-attribute-names '{
      "#a": "Age",
      "#u": "Username"
    }' \
    --key '{
      "Username": {"S": "JulianPal"}
    }' \
    $LOCAL

Además de los comparadores, también puede usar ciertas funciones en sus expresiones. Esto incluye verificar si un atributo particular existe ( attribute_exists()función) o no existe ( attribute_not_exists()función), o si un atributo comienza con una subcadena particular ( begins_with()función).

La lista completa de funciones disponibles es:

attribute_exists(): Comprobar la existencia de un atributo;
attribute_not_exists(): Comprobar la inexistencia de un atributo;
attribute_type(): Comprueba si un atributo es de un tipo determinado;
begins_with(): Compruebe si un atributo comienza con una subcadena en particular;
contains(): Compruebe si un atributo de cadena contiene una subcadena en particular o un atributo de conjunto contiene un elemento en particular; y
size(): Devuelve un número que indica el tamaño de un atributo.



### LISTAR TODAS LAS TABLAS

aws dynamodb list-tables

### DESCRIBIR EL ESQUEMA DE UNA TABLA

aws dynamodb describe-table --table-name "nombreTabla"

# CREAR TABLA CON VARIOS CON CLAVE COMPUESTA

La clave HASH es cómo se particionan sus datos, mientras que la clave RANGE es cómo se clasifican esos datos dentro de una clave HASH en particular. La clave HASH es particularmente importante: solo puede obtener datos para una sola clave HASH en una operación de consulta. Las teclas HASH y RANGE permiten una estructura similar a la de uno a muchos; para una sola tecla HASH, puede haber varias teclas RANGE.


aws dynamodb create-table \
    --table-name UserOrdersTable \
    --attribute-definitions '[
      {
          "AttributeName": "Username",
          "AttributeType": "S"
      },
      {
          "AttributeName": "OrderId",
          "AttributeType": "S"
      }
    ]' \
    --key-schema '[
      {
          "AttributeName": "Username",
          "KeyType": "HASH"
      },
      {
          "AttributeName": "OrderId",
          "KeyType": "RANGE"
      }
    ]' \
    --provisioned-throughput '{
      "ReadCapacityUnits": 1,
      "WriteCapacityUnits": 1
    }' \
    $LOCAL

# FILTROS

aws dynamodb query \
    --table-name UserOrdersTable \
    --key-condition-expression "Username = :username" \
    --filter-expression "Amount > :amount" \
    --expression-attribute-values '{
        ":username": { "S": "julianPal" },
        ":amount": { "N": "100" }
    }' \
    $LOCAL


# SCAN


La operación de escaneo opera en toda su tabla. Para tablas de tamaño real, esto puede agotar rápidamente toda su capacidad de lectura. Si lo está utilizando en la ruta crítica de su aplicación, será muy lento para devolver una respuesta a sus usuarios.

La operación de escaneo generalmente tiene sentido solo en las siguientes situaciones:

tenes una tabla muy pequeña
está exportando todos los datos de su tabla a otro sistema de almacenamiento
utiliza índices secundarios globales de una manera especial para configurar una cola de trabajo (muy avanzada).

La llamada de exploración es probablemente la más fácil de todas las llamadas de DynamoDB. Simplemente proporcione un nombre de tabla y devolverá todos los elementos de la tabla (hasta un límite de 1 MB):

aws dynamodb scan \
    --table-name UserOrdersTable \
    $LOCAL

# MODELADO DE TABLAS

ELEMENTOS INCRUSTRADOS

--RELACIONES:
Hay dos formas por referencia o incrustrada. La forma incrustrada tiene la ventaja de tener toda la informacion en un solo documento pero tiene la desventaja de que si existen muchos documentos incrustrados en uno computacionalmente se volveria muy lento y dificil de procesar. En cambio por referencia a pesar de no tener toda la informacion del documento en uno solo se puede consultar en cuento se requiera debido a que existe un campo referente a las relaciones existentes con otros documentos.

UNO A UNO:

uno a uno incrustrado:
Se puede hacer relacion uno a uno, uno a muchos y muchos a muchos. Se pueden modelar de forma integrada o mediante el enfoque por referencia

Relacion uno a uno de forma incrustado:
Incrustar datos conectados en un solo elemento puede reducir el numero de opraciones de lectura necesarias para obtener datos. En general, debe estructurar su esquema para que su aplicacion reciba toda la informacion requerida en una sola operacion delectura.

Para mas información sobre modelado:

<https://www.alexdebrie.com/posts/dynamodb-one-to-many/>


uno a uno por referencia:
Las referencias son muy parecidas a las tablas relacionales en sql, ya que se hace referencia mediante un campo id este nos servira para poder crear relacion con un documento o varios. Usamos la order_key como referencia


# CREANDO LA TABLA MAESTRA WEB CENTER



## INSERTANDO DATA aws cli

aws dynamodb put-item --table-name web_center --item '{
"clasificacion":{"S":"bot_arba"},
"compania":{"S":"grupo_darc"},
"entidad":{"S":"bot"},
"nombre":{"S":"bot_darc"}, "cron":{"S":"00***"}, "custom_id":{"S":"DC_Test"}, "descripcion":{"S":"1.0v"},"tipo":{"S":"A demanda"}, "fecha":{"S":"2021-08-19T18:25:43522Z"}, "status":{"S":"Fallo ejecucion"},"fecha_inicio":{"S":"2021-08-15T16:34:40.43SZ"}, "fecha_finalizacion":{"S":"2021-08-19T18:35:50.432Z"}, "evento":{"M":{"date":{"S":"2021-08-19T18:25:43.600Z"}, "description":{"S":"algo1"},"title": {"S":"algo1"}, "type": {"S":"Funcional"}, "status": {"S":"Advertencia"}}}}' $LOCAL


### LAMBDA INSERTAR DATA

import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    
    table = dynamodb.Table('web_center')
    
    events_to_get = event
    
    if events_to_get["clasificacion"] == "":
        raise Exception(400)
    
    
    
    response = table.put_item(
    Item = { 
        "clasificacion":events_to_get["clasificacion"],
        "compania":events_to_get["compania"],
        "entidad":events_to_get["entidad"],
        "nombre":events_to_get["nombre"], 
        "cron":events_to_get["cron"], 
        "custom_id":events_to_get["custom_id"], 
        "descripcion":events_to_get["descripcion"],
        "tipo":events_to_get["tipo"], 
        "fecha":events_to_get["fecha"], 
        "status":events_to_get["status"],
        "fecha_inicio":events_to_get["fecha_inicio"], 
        "fecha_finalizacion":events_to_get["fecha_finalizacion"], 
        "evento":events_to_get["evento"]
         }
    )
    
### LAMBDA GET ITEM

import boto3
from boto3.dynamodb.conditions import Attr, Key

def lambda_handler(event, context):
    """Obtiene un elemento por el sort y el partitionKey"""
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    
    table = dynamodb.Table('web_center')
    
    bot_to_get = event
    
    if bot_to_get["clasificacion"] == "" or bot_to_get["compania"] == "":
        raise Exception(400)
    
    bot_exist = table.query(
        KeyConditionExpression=Key("clasificacion").eq(bot_to_get["clasificacion"]) & Key("compania").eq(bot_to_get["compania"])
        )["Items"]  
    
    if bot_exist:
        response = table.get_item(Key=bot_to_get)["Item"]
    else:
        raise Exception(404)

    return response
    
### LAMBDA DELETE ITEM
