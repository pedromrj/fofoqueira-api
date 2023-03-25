from flask import Flask, jsonify
from src.routes.bazar import router_bazar

app = Flask(__name__)

app.register_blueprint(router_bazar, url_prefix="/fofoqueira/v1")

if __name__ == '__main__':
    app.run(debug=True)