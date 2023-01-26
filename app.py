from flask import Flask
from flask import request
import os
import math

app = Flask(__name__)

@app.route('/')
def hello():
    ns = request.args.get('num')
    if ns:
        try:
            nb = int(ns)
        except:
            return "bad num {ns}"
    else:
         return "no num!"
        
    out = [] 
    match [ nb ]:
        case [ number ]:
            out.append(f"Look at this square root: {math.sqrt(number)}\n")
    
    for key, value in os.environ.items():
        out.append(f"{key}={value}\n")
            
    return ''.join(out)
    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    app.debug = True

    app.run(port=port,host='0.0.0.0')
