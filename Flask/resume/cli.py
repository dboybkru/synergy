import click
from app import db
from app.models import User

def register(app):
    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        click.echo('Initialized the database.')

    @app.cli.command("create-admin")
    @click.argument('username')
    @click.argument('password')
    def create_admin(username, password):
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f'Created admin user: {username}')