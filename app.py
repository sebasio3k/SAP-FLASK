import secrets

from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from database import db
from forms import PersonaForm
from models import Persona

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
# db = SQLAlchemy(app)
db.init_app(app)

# Configurar extension flask-migrate, para mappeo de clase de modelo a BD:
migrate = Migrate()
migrate.init_app(app, db)

# Configurar flask-wtf:
# app.config['SECRET_KEY'] = 'llave_secreta'
app.config['SECRET_KEY'] = secrets.token_hex()
print(secrets.token_hex())


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    # personas = Persona.query.all()
    personas = Persona.query.order_by(Persona.id).all()  # regresa objetos de tipo Persona de la BD
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


@app.route('/agregar', methods=['GET', 'POST'])
def agregar_persona():
    persona = Persona()  # objeto tipo Persona
    persona_form = PersonaForm(obj=persona)  # asociar el formulario con el objeto Persona

    # Validar formulario:
    if request.method == 'POST':
        if persona_form.validate_on_submit():
            persona_form.populate_obj(persona)  # llenar objeto persona con datos del formulario
            app.logger.debug(f'Persona a insertar {persona}')
            # Insertar el nuevo registro:
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))

    return render_template('agregar.html', person_form=persona_form)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_persona(id):
    # Recuperar objeto de tipo Persona a editar:
    persona = Persona.query.get_or_404(id)
    forma_persona = PersonaForm(obj=persona)  # asosicar los valores de la bd con el objeto persona

    if request.method == 'POST':
        if forma_persona.validate_on_submit():
            forma_persona.populate_obj(persona)  # llenar objeto persona con datos del formulario
            app.logger.debug(f'Persona a editar {persona}')
            # Insertar el nuevo registro editado:
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))

    return render_template('editar.html', person_form=forma_persona)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    # Recuperar objeto de tipo Persona a eliminar:
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar {persona}')

    # Eliminar el nuevo registro editado:
    db.session.delete(persona)
    db.session.commit()  # guardar cambios en BD
    return redirect(url_for('inicio'))

    return render_template('eliminar.html', person_form=forma_persona)
