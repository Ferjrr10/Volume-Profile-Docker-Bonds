try:
    import json
    from flask import Flask, render_template,make_response
    import requests
    import json
    import os
    print("ALl modules Loaded ")
except Exception as e:
    print("Error : {} ".format(e))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    payload = {}
    headers = {}
    url = "http://node-red:1880/al30d1"
    r = requests.get(url, headers=headers, data ={})
    r = r.json()
    return {"res":r}


if __name__ == '__main__':
    #app.run(debug=True, host='127.0.0.1', port=5000)

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)