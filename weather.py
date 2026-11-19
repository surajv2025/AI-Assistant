import requests
 

def weather(query="Varanasi"):
    url = f"https://wttr.in/{query}?format=j1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        
        result_text = f"Varanasi mein abhi temperature {temp}°C hai aur mausam {desc} hai."
        return result_text

    except Exception as e:
        return f"Weather data fetch nahi ho paya: {e}"


 