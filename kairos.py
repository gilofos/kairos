import requests
from datetime import datetime

# --- ΡΥΘΜΙΣΕΙΣ ---
POST_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeVcHvv0c3pR53N5X8NP7sg2KY4hLxPAZXBHyhM1cxh4_KYbQ/formResponse"
ENTRY_ID = "entry.1691993416" 
API_KEY = "154abadcd6dbf332847ef2f672a9793c"
LAT = "39.91"
LON = "21.81"

def update_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=el"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            temp = data['main']['temp']
            current_time = datetime.now().strftime('%H:%M')
            status = f"{temp}°C | {current_time}"
            
            # Αποστολή στη Φόρμα
            payload = {ENTRY_ID: status}
            requests.post(POST_URL, data=payload, timeout=10)
            print(f"✅ Επιτυχία: {status}")
        else:
            print("❌ Σφάλμα API")
    except Exception as e:
        print(f"❌ Σφάλμα: {e}")

if __name__ == "__main__":
    update_weather()
