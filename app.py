#Python HTTP server for GraphQL.
from flask import Flask
from flask_graphql import GraphQLView
from gettables import schema1
from flask_cors import CORS
import graphene
app = Flask(__name__)
CORS(app)

app.add_url_rule('/graphql/', view_func=GraphQLView.as_view('graphql',
                 schema=schema1, graphiql=True))

app.run(debug=True)