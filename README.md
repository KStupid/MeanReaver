# Meaning Retriever & Word Ranker

This project is a Python-based tool designed to analyze text from PDF documents, filter words based on their CEFR (Common European Framework of Reference for Languages) proficiency levels, and retrieve definitions for selected words. It helps users identify and learn difficult vocabulary from their reading materials.

## Features

- **PDF Text Extraction:** Reads text directly from PDF files.
- **Text Cleaning:** Automatically removes hyphens and normalizes text for better analysis.
- **CEFR Level Analysis:** Uses `cefrpy` and `spacy` to analyze and filter words that are above a specified proficiency level (e.g., words harder than level 2).
- **Dictionary Lookup:** Fetches definitions, parts of speech, and meanings using the Free Dictionary API.
- **Interactive CLI:** Allows users to select pages and query specific words.

## Project Structure

- `main.py`: The entry point of the application. Handles user interaction and PDF processing.
- `meaningretriver.py`: Fetches word definitions from the API.
- `wordrank.py`: Filters words based on CEFR levels using `cefrpy`.
- `show.py`: Displays the list of filtered words and handles user selection for meanings.
- `remove_hyphen.py`: Cleans and normalizes raw text extracted from PDFs.
- `show_particular_words.py`: Helper script to display detailed meanings of a single word.

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv porenv
    source porenv/bin/activate  # On Windows use `porenv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download Spacy Model (if not installed automatically):**
    The `requirements.txt` includes the direct link for `en_core_web_sm`, so it should install automatically. If not, run:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

Run the `main.py` script with the path to your PDF file and the desired CEFR difficulty threshold (integer).

```bash
python main.py <path_to_pdf> <cefr_level>
```

**Example:**

```bash
python main.py data/orwell1984.pdf 3
```

- **`<path_to_pdf>`**: Path to the PDF file you want to analyze.
- **`<cefr_level>`**: An integer representing the difficulty threshold. Words above this level will be shown.
    - Levels are generally mapped internally by `cefrpy` (e.g., 0-5 or similar scale). Try starting with 2 or 3.

### Interactive Controls
Once the application is running:
1.  Enter a **page number** to analyze text on that page.
2.  The script will list words exceeding the specified difficulty level.
3.  Select a word by its **index number** to see its definition.
4.  Enter `-1` to go back or quit.
5.  You can also directly type a word to search its meaning.

## Notes
- Ensure your PDF contains selectable text (not scanned images).
- The `data/` folder is ignored by git to keep the repository light. Place your own PDFs there.
