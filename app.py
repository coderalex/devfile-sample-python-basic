from flask import Flask
import os
import math

app = Flask(__name__)

@app.route('/')
def hello():

    out = [] 
    match [ 2 ]:
        case [ number ]:
            out.append(f"Look at this square root: {math.sqrt(number)}\n"))
    
    for key, value in os.environ.items():
        out.append(f"{key}={value}\n")
            
    return ''.join(out)
    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
