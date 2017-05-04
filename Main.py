from flask import Flask, render_template, make_response, redirect, request
import json, ssl

app = Flask(__name__)

@app.route('/')
def index():
    with open("pages.json", "r") as f:
        pages = json.loads(f.read())
    
    return render_template('index.html', path=request.url_root, url=request.url, pages=pages)

@app.errorhandler(404)
def not_found(error):
    return make_response(redirect('/'))

if __name__ == "__main__":
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #context.load_cert_chain('../aiaeweb/host.crt', '../aiaeweb/aiae.key')
    #ssl_context=context
    app.run(debug=False, port=7001, host='0.0.0.0')
