
     import requests

# ΡΥΘΜΙΣΕΙΣ ΓΗΛΟΦΟΥ (ΟΡΙΣΤΙΚΕΣ)
API_KEY = "154abadcd6dbf332847ef2f672a9793c"
LAT = "39.91"
LON = "21.81"
# Η ΝΕΑ ΦΟΡΜΑ ΠΟΥ ΔΟΥΛΕΥΕΙ
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfysH7ZjlCObq_M09Jzk7lSHYL3r_VVsTGNO3CDynHxiU6myw/formResponse"
ENTRY_ID = "entry.170560205"

def run():
    w_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=el"
    try:
        # Παίρνουμε τον καιρό
        res = requests.get(w_url, timeout=10).json()
        temp = res['main']['temp']
        desc = res['weather'][0]['description']
        
        # Φτιάχνουμε το μήνυμα
        icon = "☀️" if "καθ" in desc.lower() or "αίθ" in desc.lower() else "☁️"
        msg = f"{icon} {temp}°C | {desc.capitalize()}"
        
        # Το στέλνουμε στη Google
        requests.post(FORM_URL, data={ENTRY_ID: msg}, timeout=10)
        print(f"✅ ΕΣΤΑΛΗ: {msg}")
    except Exception as e:
        print(f"❌ Σφάλμα: {e}")

if __name__ == "__main__":
    run()
