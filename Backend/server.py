from flask import Flask, request
from flask_cors import CORS
import json
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def Home():
    print(request.args.get("expr"))
    return json.dumps({
        "arr":list(np.arange(-5000, 5000, 0.05))
    })

app.run(debug=True, host='0.0.0.0', port=443)