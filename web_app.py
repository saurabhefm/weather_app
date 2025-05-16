from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": city,
                    "temperature": data["current_condition"][0]["temp_C"],
                    "description": data["current_condition"][0]["weatherDesc"][0]["value"],
                    "humidity": data["current_condition"][0]["humidity"],
                    "wind_speed": data["current_condition"][0]["windspeedKmph"]
                }
            else:
                error = "City not found or invalid request."
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
