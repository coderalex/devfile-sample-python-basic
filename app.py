from flask import Flask
from flask import request
import os
import math

app = Flask(__name__)

@app.route('/')
def hello():
    nb = 2
    out = []
    out += request.args.items()
    match [ nb ]:
        case [ number ]:
            out.append(f"Look at this square root: {math.sqrt(number)}\n")
    
    return '<pre>\n' + '\n'.join(out) + '</pre>'
    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
