# 🌦️ Weather Dashboard System

A simple, elegant weather dashboard web application built with **Flask** that fetches real-time weather data from a public **Weather API** (e.g., OpenWeatherMap API).  
Users can search for any city and view current weather details such as temperature, humidity, weather conditions, and more.

---

## 🚀 Features

- Search weather by city name
- View:
  - Temperature
  - Humidity
  - Wind speed
  - Weather description (e.g., cloudy, sunny)
- Responsive and clean UI
- Error handling for invalid city names
- Displays icons for weather conditions
- Easy to extend for 5-day forecasts or historical data

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3
- **APIs**: OpenWeatherMap API (or any similar weather API)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/hschinmayabharadwaj/weather_dashboard.git
cd weather-dashboard
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install required packages
```bash
pip install flask
pip install requests
```

### 4. Set up your API Key
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
- Create a `.env` file in the root directory and add your API key:
  ```env
  WEATHER_API_KEY=your_api_key_here
  ```

### 5. Run the application
```bash
python app.py
```
Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💂️ Project Structure

```
weather-dashboard/
│
├── static/
│   ├── style.css/
│   
│
├── templates/
│   └── index.html
│
├── app.py
├
└── README.md
```

---

## 🧹 Example API Usage

Example call to OpenWeatherMap API:
```plaintext
http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric
```

Sample JSON response:
```json
{
  "weather": [{ "description": "clear sky", "icon": "01d" }],
  "main": { "temp": 15.5, "humidity": 72 },
  "wind": { "speed": 4.1 },
  "name": "London"
}
```

---

## ⚡ Future Improvements

- 5-day / hourly forecasts
- Save and display recent search history
- Add geolocation support (auto-detect user's location)
- Beautiful animated weather backgrounds
- Deploy to cloud (Heroku, Render, AWS)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤛🏼 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

