from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_graphql import GraphQLView

from modules.core.db import db_session
from modules.core.schemas import schema
from modules.core.settings import DATABASE_URL, DEBUG, HOST

load_dotenv(find_dotenv(), verbose=True)
app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['DATABASE_URL'] = DATABASE_URL
app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view(
        'graphql', schema=schema, graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host=HOST)
