import requests
from datetime import datetime

# --- ΣΤΟΙΧΕΙΑ ΓΗΛΟΦΟΥ ---
API_KEY = "154abadcd6dbf332847ef2f672a9793c"
LAT = "39.91"
LON = "21.81"

# Η ΦΟΡΜΑ ΠΟΥ ΣΥΝΔΕΕΤΑΙ ΜΕ ΤΟ SITE ΣΟΥ (Η σωστή που βρήκαμε)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfysH7ZjlCObq_M09Jzk7lSHYL3r_VVsTGNO3CDynHxiU6myw/formResponse"
ENTRY_ID = "entry.170560205"

def get_weather_icon(desc):
    d = desc.lower()
    if "καθαρός" in d or "αίθριος" in d: return "☀️"
    if "συννεφιά" in d or "νέφη" in d: return "☁️"
    if "βροχή" in d: return "🌧️"
    if "χιόνι" in d: return "❄️"
    return "🌡️"

def run_update():
    # 1. Λήψη καιρού από OpenWeather
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=el"
    
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            icon = get_weather_icon(desc)
            
            # Μήνυμα: "☀️ 12.5°C | Αίθριος"
            weather_msg = f"{icon} {temp}°C | {desc.capitalize()}"
            
            # 2. Αποστολή στη Google Φόρμα για να ενημερωθεί το site
            payload = {ENTRY_ID: weather_msg}
            post_r = requests.post(FORM_URL, data=payload, timeout=15)
            
            if post_r.status_code == 200:
                print(f"✅ ΕΠΙΤΥΧΙΑ: {weather_msg}")
            else:
                print(f"❌ Σφάλμα Google: {post_r.status_code}")
        else:
            print(f"❌ Σφάλμα Καιρού: {r.status_code}")
    except Exception as e:
        print(f"❌ Σφάλμα σύνδεσης: {e}")

if __name__ == "__main__":
    run_update()
