import fitz
import sys
import wordrank
import remove_hyphen
import show
import show_particular_words
import spacy

# Load the small English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

from cefrpy import CEFRSpaCyAnalyzer

# Mapping for expanding English contractions to help the CEFR analyzer identify root words correctly
ABBREVIATION_MAPPING = {
    "'m": "am",
    "'s": "is",
    "'re": "are",
    "'ve": "have",
    "'d": "had",  # or "would", depending on context
    "n't": "not",
    "'ll": "will",
    "ain't": "is not",  # or "are not", depending on context
    "can't": "cannot",
    "won't": "will not",
    "shan't": "shall not",
    "let's": "let us",
    "ma'am": "madam",
    "y'all": "you all",
    "o'clock": "of the clock",
    "could've": "could have",
    "should've": "should have",
    "would've": "would have",
    "might've": "might have",
    "must've": "must have",
    "who's": "who is",  # or "who has"
    "what's": "what is",  # or "what has"
    "where's": "where is",  # or "where has"
    "there's": "there is",  # or "there has"
    "here's": "here is",  # or "here has"
    "it's": "it is",  # or "it has"
    "that's": "that is",  # or "that has"
    "how's": "how is",  # or "how has"
    "she's": "she is",  # or "she has"
    "he's": "he is",  # or "he has"
    "they're": "they are",
    "we're": "we are",
    "I'm": "I am",
    "you're": "you are",
    "I'll": "I will",
    "you'll": "you will",
    "she'll": "she will",
    "he'll": "he will",
    "they'll": "they will",
    "we'll": "we will",
    "I'd": "I had",  # or "I would"
    "you'd": "you had",  # or "you would"
    "she'd": "she had",  # or "she would"
    "he'd": "he had",  # or "he would"
    "they'd": "they had",  # or "they would"
    "we'd": "we had",  # or "we would"
    }

# Entities to ignore during vocabulary analysis as they aren't generally "vocabulary" words
ENTITY_TYPES_TO_SKIP_CEFR = {
    'QUANTITY', 'MONEY', 'LANGUAGE', 'LAW',
    'WORK_OF_ART', 'PRODUCT', 'GPE', 'LOC',
    'ORG', 'FAC', 'PERSON', 'DATE', 'TIME',
    'ORDINAL', 'CARDINAL', 'NORP', 'EVENT',
    'PERCENT'
    }

# Initialize the CEFR analyzer with the custom mapping and skip list
analyzer = CEFRSpaCyAnalyzer(entity_types_to_skip=ENTITY_TYPES_TO_SKIP_CEFR, abbreviation_mapping=ABBREVIATION_MAPPING)

# Validate command line arguments
if len(sys.argv) != 3:
    print("Usage: python main.py <file_path> <CEFR_level>\nExample: python main.py book.pdf 5")
    sys.exit(1)

file = sys.argv[1]
try:
    level = int(sys.argv[2])
except ValueError:
    print("Error: CEFR_level must be an integer.")
    sys.exit(1)

# Open the PDF document
try:
    book = fitz.open(file)
except Exception as e:
    print(f"Error opening PDF: {e}")
    sys.exit(1)

# Main interaction loop
while True:
    pageno = input("Enter the page no (starting from 1)\nTo quit, press (-1)\nOr enter a word: ")

    try:
        # If the input is an integer, treat it as a page number request
        pageno_int = int(pageno)

        if pageno_int == -1:
            print("Wow, you know everything! Goodbye!")
            break
        elif 1 <= pageno_int <= len(book):
            page = book[pageno_int-1]
            text = page.get_text("text")

            if text:
                # Clean text: remove hyphens and formatting weirdness
                text = remove_hyphen.hr(text)
                # Extract words that are above the user's proficiency level
                words = wordrank.words_or_text_to_CEFR(nlp, analyzer, text, level)

                if words:
                    # Display the list of difficult words to the user
                    show.s_r(words)
                else:
                    print("Looks like you know everything from this page!\n")
            else:
                print("No text found on the page.")
        else:
            print("#### CHECK YOUR DAMN EYES #### Page number out of range.")
    
    except ValueError:
        # If input is not an integer, assume the user is searching for a specific word
        print(f"\nword\t:{pageno}\n")
        show_particular_words.wordmeaning(pageno)
        input("\nPress Enter to continue...")
