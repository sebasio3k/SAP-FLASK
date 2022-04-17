# SAP-FLASK
Sistema Administrador de Personas en framework de python: Flask

<br>

**Tecnologías:**
**Microframework: Flask**
> python -m pip install flask

<br>

**Flask SQL Alchemy: librería orm: permite crear clases de modelo para mappear hacia la BD**
https://www.sqlalchemy.org/
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
> flask db stamp head 
> <br>
> flask db migrate
> <br>
> flask db upgrade
