from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redirect')
def make_request_and_redirect():
    client_id = '7a6a9ab9eed58a166ff3c9b936294818f4116e23e72d511f46dd4f8209b104d3'
    redirect_uri = 'https://2a9a-167-57-99-42.ngrok-free.app'
    redirect_uri_encoded = 'https%3A%2F%2F2a9a-167-57-99-42.ngrok-free.app'
    url = "https://tstdrv2049642.app.netsuite.com/app/login/oauth2/authorize.nl?client_id="+client_id+"&redirect_uri="+redirect_uri_encoded+"&response_type=code&scope=rest_webservices&state=Gb50fW4HU2q9gpOH"
    headers = {
        "client_id": client_id,
        # "client_id": "c6e22d0ee5b5f769bc32c99a80ad85a1d05df2d41ef42e5a0bdfd60166e08b9f",
        # "client_id": "063ff281c2df90b14e85dcc15b0928f0a3d68a50eb38f113bde98dc908458418",
        # "redirect_uri": "https%3A%2F%2Ffedericodonner.com",
        # "redirect_uri": "https%3A%2F%2Fplatform.panoply.io%2Fsources%2Fcallback.html",
        "redirect_uri": redirect_uri_encoded,
        "response_type": "code",
        "scope": "rest_webservices",
        "state": "Gb50fW4HU2q9gpOH"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return redirect(url)
    else:
        return "Error", 500

if __name__ == '__main__':
    app.run(debug=True)
