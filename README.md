# SAP-FLASK
Sistema Administrador de Personas en framework de python: Flask


<img width="885" alt="Captura de Pantalla 2022-04-19 a la(s) 16 19 36" src="https://user-images.githubusercontent.com/39862006/164103692-b2aec98e-cdde-4c4e-b5a2-734a04d7f4ef.png">

<br>

**Tecnologías:**
**Microframework: Flask**
> python -m pip install flask

<br>

**Flask SQL Alchemy: librería orm: permite crear clases de modelo para mappear hacia la BD**
<br>
https://www.sqlalchemy.org/
<br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
<br>
> python -m pip install flask-sqlalchemy
<br>

**Flask Migrate: para migraciones y modificaciones de clases de modelos hacia BD, (proyecto: alembic, crea archivos de migraciones)**
> python -m pip install flask-migrate

<br>

**Plugin (extension python)Psycopg2 para trabajar con postores**
> pip install psycopg2
**or**
> pip install psycopg2-binary

<br>

**Crear carpeta de migrations:**
> flask db init

<br>

**Crear archivo de migraciones de mappeo (sql que se va a ejecutar) en migrations/versions:**
> flask db migrate

<br>

**Ejecutar archivo de migración en la bd:**
> flask db upgrade

<br>

**Para modificaciones...
Verificar que todo esté actualizado al momento:**
> flask db stamp head <br>
> flask db migrate <br>
> flask db upgrade

<br>

**Trabajar con formularios (wtforms), integración(flask-wtf):**
> python -m pip install flask-wtf
 
_Configurar llave secreta_:

    app.config['SECRET_KEY'] = secrets.token_hex()

https://flask-wtf.readthedocs.io/en/1.0.x/
