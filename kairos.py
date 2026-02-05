import requests
from datetime import datetime

# --- ΡΥΘΜΙΣΕΙΣ ΓΗΛΟΦΟΥ (API & ΣΥΝΤΕΤΑΓΜΕΝΕΣ) ---
# Το API Key του Αχιλλέα για τον καιρό
API_KEY = "154abadcd6dbf332847ef2f672a9793c"
LAT = "39.91"
LON = "21.81"

# --- ΡΥΘΜΙΣΕΙΣ GOOGLE (WIDGET ΣΥΝΔΕΣΗ) ---
# Η Φόρμα που δέχεται τα δεδομένα για το gilofos.com
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfysH7ZjlCObq_M09Jzk7lSHYL3r_VVsTGNO3CDynHxiU6myw/formResponse"
# Το κουτάκι (entry) που γράφουμε τον καιρό
ENTRY_ID = "entry.170560205"

def get_weather():
    """Παίρνει δεδομένα από το OpenWeatherMap"""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=el"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return temp, desc
        else:
            print(f"Σφάλμα API Καιρού: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"Αποτυχία σύνδεσης: {e}")
        return None, None

def send_to_google(temp, desc):
    """Στέλνει το τελικό μήνυμα στη Google Φόρμα"""
    # Επιλογή εικονιδίου για το Widget
    icon = "🌡️"
    d = desc.lower()
    if "καθαρός" in d or "αίθριος" in d: icon = "☀️"
    elif "σύννεφα" in d or "νέφη" in d: icon = "☁️"
    elif "βροχή" in d: icon = "🌧️"
    elif "χιόνι" in d: icon = "❄️"
    
    # Το μήνυμα που θα δει ο κόσμος στο site
    formatted_msg = f"{icon} {temp}°C | {desc.capitalize()}"
    payload = {ENTRY_ID: formatted_msg}
    
    try:
        res = requests.post(FORM_URL, data=payload, timeout=10)
        if res.status_code == 200:
            print(f"✅ ΕΠΙΤΥΧΙΑ: {formatted_msg}")
        else:
            print(f"❌ Σφάλμα Google: {res.status_code}")
    except Exception as e:
        print(f"❌ Σφάλμα αποστολής: {e}")

if __name__ == "__main__":
    # Αυτό το τρέχει το GitHub Actions αυτόματα
    print(f"--- Έναρξη: {datetime.now().strftime('%H:%M:%S')} ---")
    t, d = get_weather()
    if t is not None:
        send_to_google(t, d)
    print("--- Τέλος ---")
    
         
