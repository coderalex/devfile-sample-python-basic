from flask import Flask
from flask import request
import os
import math

app = Flask(__name__)

@app.route('/')
def hello():
    default_num = 2
    ns = request.args.get('num')
    out = [
        '<form>Number to find square root of: <input type=text name=num> <input type=submit></form>',
    ]
    if ns:
        try:
            nb = int(ns)
        except:
            return "<p>bad num {ns}</p>"
    else:
         out.append(f"<p>no num! using {default_num}</p>")
         nb = default_num

    match [ nb ]:
        case [ number ]:
            out.append(f"<p>The square root of {nb} is: {math.sqrt(number)}</p>")

    return '\n'.join(out) + '\n'
    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
