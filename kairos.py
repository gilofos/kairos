import requests

URL = "https://docs.google.com/forms/d/e/1FAIpQLSeVcHvv0c3pR53N5X8NP7sg2KY4hLxPAZXBHyhM1cxh4_KYbQ/formResponse"
ENTRY = "entry.1147714150" 

def update_weather():
    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=39.91&lon=21.81&appid=154abadcd6dbf332847ef2f672a9793c&units=metric"
    try:
        res = requests.get(weather_url).json()
        temp = res['main']['temp']
        keimeno = f"{temp} C"
        requests.post(URL, data={ENTRY: keimeno})
        print(f"Efyge: {keimeno}")
    except:
        print("Sfalma")

if __name__ == "__main__":
    update_weather()
