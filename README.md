# SAP-FLASK
Sistema Administrador de Personas en framework de python: Flask

**Tecnologías:**
**Microframework: Flask**
> python -m pip install flask

**Flask SQL Alchemy: librería orm: permite crear clases de modelo para mappear hacia la BD**
> python -m pip install flask-sqlalchemy

<br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
<br>
https://www.sqlalchemy.org/

**Flask Migrate: para migraciones y modificaciones de clases de modelos hacia BD, (proyecto: alembic, crea archivos de migraciones)**
> python -m pip install flask-migrate

**Plugin (extension python)Psycopg2 para trabajar con postores**
> pip install psycopg2
**or**
> pip install psycopg2-binary

**Crear carpeta de migrations:**
> flask db init

**Crear archivo de migraciones de mappeo (sql que se va a ejecutar) en migrations/versions:**
> flask db migrate

**Ejecutar archivo de migración en la bd:**
> flask db upgrade

**Para modificaciones...
Verificar que todo esté actualizado al momento:**
> flask db stamp head 
> flask db migrate
> flask db upgrade
