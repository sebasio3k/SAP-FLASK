from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuracion de BD
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # no tracking de modificaciones sobre bd (puede alentar bd)

# Inicializar objeto BD de SQLAchemy
db = SQLAlchemy(app)

# Configurar extension flask-migrate, para mappeo de clase de modelo a BD:
migrate = Migrate()
migrate.init_app(app, db)


# Clase de modelo:
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return (
            f'ID: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Email: {self.email}.'
        )


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    personas = Persona.query.all()  # regresa objetos de tipo Persona de la BD
    total_personas = Persona.query.count()

    # Imprimir a consola los objetos:
    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')

    return render_template('index.html', people=personas, total_people=total_personas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    # Recuperar persona segun id:

    # persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)

    app.logger.debug(f'Ver persona: {persona}')

    return render_template('detalle.html', person_obj=persona)
