import requests
from flask import Flask, render_template, request



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def get_location_details(city):
    url = f"https://nominatim.openstreetmap.org/search?city={city}&format=json&limit=1"
    headers = {"User-Agent": "weather-app"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        display_name = data.get("display_name", "")
        address = data.get("address", {})
        print("ADDRESS DEBUG:", address)
        state = address.get("state", "")
        country = address.get("country", "")
        return state, country
    return "", ""

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(weather_url)
            if response.status_code == 200:
                data = response.json()

                # Get state and country
                state, country = get_location_details(city)

                location_full = f"{city}"
                if state:
                    location_full += f", {state}"
                if country:
                    location_full += f", {country}"

                weather_data = {
                    "city": city,
                    "state": state,
                    "country": country,
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
