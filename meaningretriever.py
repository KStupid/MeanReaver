import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_word_definitions(word):
    """
    Fetches meanings and definitions for a given word from the Free Dictionary API.
    Returns a dictionary mapping parts of speech to a list of definitions.
    """
    url = f"{BASE_URL}{word.lower()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            word_data = response.json()
            if not word_data:
                return {}
            
            # Use the first entry from the API response
            entry = word_data[0]
            meanings = {}
            for item in entry.get("meanings", []):
                pos = item.get("partOfSpeech")
                definitions = [d["definition"] for d in item.get("definitions", [])]
                meanings[pos] = definitions
            return meanings
        
        elif response.status_code == 404:
            return {}  # Word not found
        
        else:
            print(f"API Error: {response.status_code} for word '{word}'")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None
