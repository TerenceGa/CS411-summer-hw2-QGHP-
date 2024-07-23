from flask import Flask, make_response, request
import os
app = Flask(__name__)
port = int(os.getenv('PORT'))

@app.route('/')
def hello():
    response = make_response('Hello, World!', 200)
    return response

@app.route('/repeat')
def repeat():
    input=request.args.get('input')
    response = make_response(input, 200)
    return response

@app.route('/health')
@app.route('/healthcheck')
def health():
    # same as hello
    response = make_response('OK', 200)
    return response

@app.route('/onpurpose')
def badidea():
    while True:
        pass

if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)

    app.run(host='0.0.0.0',port=port, debug=True, threaded=False)
