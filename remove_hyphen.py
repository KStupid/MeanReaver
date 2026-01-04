import unicodedata
import re

def hr(text):
    # 1. Normalize unicode characters (e.g., ligatures like 'ﬁ' to 'fi')
    normalized_text = unicodedata.normalize('NFKD', text)
    
    # 2. Encode to ascii, ignoring characters that cannot be encoded, then decode back.
    cleaned_text = normalized_text.encode('ascii', 'ignore').decode('utf-8')

    # 3. Replace newlines with spaces.
    cleaned_text = cleaned_text.replace("\n", " ")
    
    # 4. Remove hyphens from broken words using regex.
    # Matches: hyphen, optional space, followed by a non-space character.
    cleaned_text = re.sub(r'- ?(?=[^ ])', '', cleaned_text)
    
    return cleaned_text