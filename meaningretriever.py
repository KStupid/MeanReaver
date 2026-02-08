import requests

# Base URL for the Free Dictionary API
BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_word_definitions(word):
    """
    Fetches meanings and definitions for a given word from the Free Dictionary API.
    
    Args:
        word (str): The English word to look up.
        
    Returns:
        dict: A dictionary where keys are parts of speech (e.g., 'noun', 'verb') 
              and values are lists of definition strings.
              Returns an empty dict if the word is not found.
              Returns None if a connection or API error occurs.
    """
    url = f"{BASE_URL}{word.lower()}"
    try:
        response = requests.get(url)
        
        # HTTP 200: Success
        if response.status_code == 200:
            word_data = response.json()
            if not word_data:
                return {}
            
            # Use the first entry from the API response (some words have multiple entries)
            entry = word_data[0]
            meanings = {}
            
            # Iterate through meanings grouped by part of speech
            for item in entry.get("meanings", []):
                pos = item.get("partOfSpeech")
                definitions = [d["definition"] for d in item.get("definitions", [])]
                meanings[pos] = definitions
            return meanings
        
        # HTTP 404: Word not found in dictionary
        elif response.status_code == 404:
            return {}
        
        # Other HTTP errors (500, etc.)
        else:
            print(f"API Error: {response.status_code} for word '{word}'")
            return None
            
    except requests.exceptions.RequestException as e:
        # Network issues, timeouts, etc.
        print(f"Connection Error: {e}")
        return None
