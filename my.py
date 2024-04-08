from flask import Flask
from routes.home import home_route 
from routes.pedidos import pedidos_route


app= Flask(__name__)


app.register_blueprint(home_route)
app.register_blueprint(pedidos_route, url_prefix='/')

app.run(debug=True)