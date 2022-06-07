import Flask
from flask_restful import Resource, Api

# Ici nous créons des instances de l'application et de l'API 
app = Flask(__name__)
api = Api(app)

# Ici, nous créons une classe qui réagira lorsque l'API sera requêtée. Cette classe hérite de la classe "Resource" que nous avons importée.
# La fonction "get" est la fonction par défaut lorsque nous requêtons une API.
# Ici elle retournera systématiquement un dictionnaire, toujours identique.
class my_API_class(Resource):
    def get(self):
        return {'hello': 'Hi, welcome in my API'}

# Nous devons ensuite ajouter la ressource à notre classe
api.add_resource(my_API_class, '/')

# L'API sera lancée ici dans le script. Pour l'instant, tu peux laisser l'argument debug = True
if __name__ == '__main__':
    app.run(debug=True)