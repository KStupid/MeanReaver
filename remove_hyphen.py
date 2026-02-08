import unicodedata
import re

def hr(text):
    """
    Cleans and prepares text extracted from a PDF for NLP analysis.
    Performs normalization, newline removal, and de-hyphenation.
    
    Args:
        text (str): Raw text from a PDF page.
        
    Returns:
        str: Cleaned text.
    """
    # 1. Normalize unicode characters
    # This converts ligatures (like 'ﬁ') into separate characters ('fi')
    normalized_text = unicodedata.normalize('NFKD', text)
    
    # 2. Encode to ascii, ignoring characters that cannot be encoded, then decode back.
    # NOTE: This effectively removes accents and non-ASCII symbols.
    cleaned_text = normalized_text.encode('ascii', 'ignore').decode('utf-8')

    # 3. Replace newlines with spaces to treat the text as a continuous stream.
    cleaned_text = cleaned_text.replace("\n", " ")
    
    # 4. Remove hyphens from broken words using regex.
    # PDFs often have line-break hyphens (e.g., "vocab- \n ulary").
    # Matches: hyphen followed by an optional space, then a non-space character (lookahead).
    cleaned_text = re.sub(r'- ?(?=[^ ])', '', cleaned_text)
    
    return cleaned_text