# API REST de Gestión de Inmuebles

API REST desarrollada con **Python, Django y Django REST Framework**
para administrar usuarios, inmuebles y solicitudes de arriendo. El
proyecto contempla perfiles de **Arrendador** y **Arrendatario**, además
de información territorial de regiones y comunas de Chile.

## Características principales

-   **Gestión de usuarios:** creación y consulta de usuarios con datos
    de perfil y asignación al grupo correspondiente (`Arrendador` o
    `Arrendatario`).
-   **Gestión de inmuebles:** endpoints para listar, consultar, crear,
    actualizar y eliminar inmuebles.
-   **Solicitudes de arriendo:** los arrendatarios autenticados pueden
    enviar solicitudes; estas quedan inicialmente en estado `PENDIENTE`.
-   **Datos territoriales:** consulta de regiones y comunas.
-   **Autenticación JWT:** emisión, renovación, verificación y
    revocación de tokens de actualización.
-   **Permisos por rol:** se utilizan grupos de Django para distinguir
    las acciones de arrendadores y arrendatarios.

## Tecnologías

-   Python
-   Django
-   Django REST Framework
-   Simple JWT (`djangorestframework-simplejwt`)
-   SQLite para desarrollo

## Estructura del proyecto

``` text
proyecto_inmuebles_apis/
├── gestion_apis/
│   ├── fixtures/
│   ├── migrations/
│   ├── models/
│   │   ├── comuna.py
│   │   ├── inmueble.py
│   │   ├── region.py
│   │   ├── solicitud_arriendo.py
│   │   ├── tipo_inmueble.py
│   │   └── usuario.py
│   ├── views/
│   ├── permissions.py
│   ├── serializers.py
│   └── urls.py
├── proyecto_inmuebles_apis/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Requisitos previos

-   Python instalado.
-   `pip`, el administrador de paquetes de Python.
-   Git, para clonar el repositorio.

## Instalación y ejecución local

### 1. Clonar el repositorio

Reemplaza la URL de ejemplo por la URL real del repositorio:

``` bash
git clone https://github.com/USUARIO/REPOSITORIO.git
cd proyecto_inmuebles_apis
```

### 2. Crear y activar un entorno virtual

En Windows:

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En macOS o Linux:

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

``` bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones

``` bash
python manage.py migrate
```

### 5. Crear un usuario administrador

``` bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor

``` bash
python manage.py runserver
```

La API estará disponible normalmente en `http://127.0.0.1:8000/` y el
administrador de Django en `http://127.0.0.1:8000/admin/`.

> **Nota sobre los grupos:** para usar los permisos por rol, crea los
> grupos `Arrendador` y `Arrendatario` en el administrador de Django.
> Los usuarios deben pertenecer al grupo que corresponda.

## Endpoints principales

La URL base de los recursos es `/api/`.

  ------------------------------------------------------------------------------
  Método                  Endpoint                       Descripción
  ----------------------- ------------------------------ -----------------------
  `POST`                  `/api/token/`                  Obtener tokens JWT
                                                         usando usuario y
                                                         contraseña

  `POST`                  `/api/token/refresh/`          Renovar el token de
                                                         acceso

  `POST`                  `/api/token/verify/`           Verificar un token

  `POST`                  `/api/token/logout/`           Solicitar la revocación
                                                         del refresh token

  `GET`                   `/api/mi-usuario/`             Consultar los datos del
                                                         usuario autenticado

  `GET`                   `/api/usuarios/`               Listar usuarios

  `POST`                  `/api/usuarios/`               Registrar un usuario
                                                         con perfil

  `GET`                   `/api/inmuebles/`              Listar inmuebles

  `GET`                   `/api/inmuebles/{id}/`         Consultar un inmueble

  `POST`                  `/api/inmuebles/`              Crear un inmueble

  `PUT/PATCH`             `/api/inmuebles/{id}/`         Actualizar un inmueble

  `DELETE`                `/api/inmuebles/{id}/`         Eliminar un inmueble

  `GET`                   `/api/regiones/`               Consultar regiones

  `GET`                   `/api/comunas/`                Consultar comunas

  `GET`                   `/api/solicitudes-arriendo/`   Consultar las
                                                         solicitudes del usuario
                                                         autenticado

  `POST`                  `/api/solicitudes-arriendo/`   Crear una solicitud de
                                                         arriendo como
                                                         arrendatario
  ------------------------------------------------------------------------------

Los endpoints y permisos efectivos dependen de la configuración del
proyecto. En la implementación actual, el endpoint de usuarios tiene
permisos abiertos (`AllowAny`); antes de desplegar la API, restringe el
registro, listado, modificación y eliminación según las necesidades de
seguridad.

## Autenticación con JWT

Para obtener los tokens, envía una petición `POST` a `/api/token/` con
un cuerpo JSON:

``` json
{
  "username": "tu_usuario",
  "password": "tu_contrasena"
}
```

La respuesta incluye normalmente `access` y `refresh`. Para acceder a
endpoints protegidos, agrega el token de acceso en el encabezado HTTP:

``` http
Authorization: Bearer <access_token>
```

La configuración actual establece una duración de **30 minutos para el
access token** y **1 día para el refresh token**. El endpoint de logout
está configurado para revocar el refresh token mediante la lista de
bloqueo de Simple JWT.

## Ejemplo: solicitar un inmueble

Un arrendatario autenticado puede enviar un `POST` a
`/api/solicitudes-arriendo/` con el identificador del inmueble:

``` json
{
  "inmueble": 1
}
```

El usuario arrendatario se obtiene del token de autenticación y la
solicitud se crea con estado `PENDIENTE`; no es necesario enviar esos
campos manualmente. El inmueble debe existir y el usuario debe
pertenecer al grupo `Arrendatario`.

## Datos de prueba

El proyecto incluye fixtures en `gestion_apis/fixtures/` para tipos de
inmueble y datos territoriales. Si deseas cargarlos, revisa los nombres
de las fixtures y ejecuta, según corresponda:

``` bash
python manage.py loaddata nombre_de_la_fixture.json
```

## Consideraciones de seguridad antes de publicar

-   No publiques contraseñas, tokens, archivos `.env` ni claves
    secretas.
-   Cambia `SECRET_KEY` por una variable de entorno y desactiva `DEBUG`
    en producción.
-   Configura `ALLOWED_HOSTS` para el entorno de despliegue.
-   Usa HTTPS en producción.
-   Restringe los permisos de los endpoints de usuarios y verifica que
    cada rol solo pueda realizar las acciones autorizadas.
-   Evita subir la base de datos local `db.sqlite3` si contiene datos
    personales o credenciales de prueba.

## Objetivo del proyecto

Practicar el diseño y la implementación de una API REST con Django REST
Framework, incluyendo modelos relacionados, serializadores, vistas
basadas en ViewSets y vistas genéricas, autenticación JWT y permisos
asociados a roles de usuario.
