import json
import threading
import time
from backend import backend
from flask import Flask, render_template

app = Flask(__name__)

results = '{"weather_forecast": 1}'

def call_backend():
    global results
    while True:
        results = backend()
        time.sleep(60)

@app.route("/")
def home():
    if json.loads(results)["weather_forecast"] in ["Fair", "Clear", "Fair with Haze", "Clear with Haze", "Fair and Breezy", "Clear and Breezy"]:
        weather_image = "fair.png"

    elif json.loads(results)["weather_forecast"] in ["A Few Clouds", "A Few Clouds with Haze", "A Few Clouds and Breezy"]:
        weather_image = "few.png"

    elif json.loads(results)["weather_forecast"] in ["Partly Cloudy", "Partly Cloudy with Haze", "Partly Cloudy and Breezy"]:
        weather_image = "partly.png"

    elif json.loads(results)["weather_forecast"] in ["Mostly Cloudy", "Mostly Cloudy with Haze", "Mostly Cloudy and Breezy"]:
        weather_image = "mostly.png"

    elif json.loads(results)["weather_forecast"] in ["Overcast", "Overcast with Haze", "Overcast and Breezy"]:
        weather_image = "overcast.png"

    else:
        weather_image = "unknown.webp"
        
    return render_template("index.html",  image=weather_image)

if __name__ == "__main__":
    thread = threading.Thread(target=call_backend).start()
    app.run(debug=False)

