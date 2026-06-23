import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

api_key ="d98f9d2a7704992962145edf038b9784"

class WeatheraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.input_city = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("Temperature: ", self)
        self.emojie_label = QLabel("🌞", self)
        self.description_label = QLabel("Description: ", self)
        self.setObjectName("main_window")
        self.setWindowIcon(QIcon("thekawas.webp"))
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App by Lim (NO AI)")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.input_city)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emojie_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.input_city.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emojie_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.input_city.setObjectName("input_city")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emojie_label.setObjectName("emojie_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget#main_window {
                background-color: #556085;
            }
            
                           
            QLabel, QPushButton {
                font-family: Arial;
                background-color : #e3a2fc;
            }
            QLabel#city_label {
                font-size: 40px;
                font-weight: bold;
                color: #333;
            }
            QLineEdit#input_city {
                font-size: 30px;
                padding: 10px;
            }
            QPushButton#get_weather_button {
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 24px;
                font-weight: bold;
            }
            QLabel#emojie_label {
                font-size: 48px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 20px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)       


    def get_weather(self):
        city = self.input_city.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
             self.display_error("ERRRRRORRRR")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects")
        except requests.exceptions.RequestException:
             self.display_error("too many requests")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red")
        self.temperature_label.setText(message)
    def display_weather(self, data):
        temperatur = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        self.temperature_label.setStyleSheet("color: black")
        self.temperature_label.setText(f"The temperatur is {temperatur} Celcius")
        self.description_label.setText(weather)
        if "clear" in weather.lower():
            emoji = "☀️"

        elif "cloud" in weather.lower():
            emoji = "☁️"

        elif "rain" in weather.lower():
            emoji = "🌧️"

        elif "drizzle" in weather.lower():
            emoji = "🌦️"

        elif "thunderstorm" in weather.lower():
            emoji = "⛈️"

        elif "snow" in weather.lower():
            emoji = "❄️"

        elif "haze"or "fog"or"mist" in weather.lower():
            emoji = "🌫️"

        else:
            emoji = "🌍"
        self.emojie_label.setText(emoji)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatheraApp()
    weather_app.show()
    sys.exit(app.exec_())