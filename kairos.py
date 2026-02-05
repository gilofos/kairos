import requests

# Η ΔΙΕΥΘΥΝΣΗ ΤΗΣ ΦΟΡΜΑΣ ΣΟΥ
URL = "https://docs.google.com/forms/d/e/1FAIpQLSeVcHvv0c3pR53N5X8NP7sg2KY4hLxPAZXBHyhM1cxh4_KYbQ/formResponse"

def update_weather():
    # Ο ΚΑΙΡΟΣ ΓΙΑ ΤΟΝ ΓΗΛΟΦΟ
    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=39.91&lon=21.81&appid=154abadcd6dbf332847ef2f672a9793c&units=metric"
    try:
        res = requests.get(weather_url).json()
        temp = res['main']['temp']
        keimeno = f"{temp} C"
        
        # Στέλνουμε τη θερμοκρασία στο Excel
        data = {
            "entry.1147714150": keimeno
        }
        
        requests.post(URL, data=data)
        print(f"Efyge h thermokrasia: {keimeno}")
    except:
        print("Sfalma sth lhpsh")

if __name__ == "__main__":
    update_weather()
