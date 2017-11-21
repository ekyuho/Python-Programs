from flask import Flask, request
from datetime import datetime
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    str = datetime.now().strftime('%Y-%m-%d %H:%M:%S {')
    comma = ""
    with open("log.txt", "a") as f:   
        for p in request.args:
            str += comma + "'%s':%s" % (p, request.args[p])
            comma = ", "
        str += "}"
        f.write("%s\n"%(str));
        sys.stdout.write("%s\n"%(str))
        sys.stdout.flush()
    return 'X_ACK: ' + str

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

print("Waiting at port 5000")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
