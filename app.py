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
    nb = None
    if ns:
        try:
            nb = float(ns)
        except ValueError:
            out.append(f"<p>Bad number: <code>{ns}</code></p>")
    if nb is None:
         out.append(f"<p>No valid number entered; using <code>{default_num}</code> by default.</p>")
         nb = default_num

    match [ nb ]:
        case [ number ]:
            if number < 0:
                out.append(f"<p>Can't find the square root of <code>{nb}</code> since it's negative</p>")
            else:
                out.append(f"<p>The square root of {ns} is: {math.sqrt(number)}</p>")
    return '\n'.join(out) + '\n'
    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
