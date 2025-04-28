from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API_KEY = "bf0cf1bb3473a8fb6620f8b801caf18a"  # Replace with your real API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            weather = {"error": data.get("message", "City not found")}
        else:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"].title()
            icon = data["weather"][0]["icon"]
            city_name = data["name"]

            # Convert times using timezone offset
            timezone_offset = data["timezone"]
            local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)
            sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + timezone_offset).strftime('%H:%M:%S')
            sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + timezone_offset).strftime('%H:%M:%S')
            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')

            weather = {
                "temperature": round(temp, 2),
                "feels_like": round(feels_like, 2),
                "humidity": humidity,
                "wind": wind,
                "description": description,
                "icon": icon,
                "city": city_name,
                "sunrise": sunrise,
                "sunset": sunset,
                "local_time": formatted_time
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)