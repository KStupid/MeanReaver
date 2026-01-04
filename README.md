# 📚 MeanReaver
*Uncover the hidden vocabulary in your books!*

## 🚀 What is this?
Ever been reading a complex PDF and got stuck on difficult words? This tool is your personal vocabulary assistant! 
It scans your PDF documents, filters out the easy words based on your proficiency level, and presents you with the challenging ones. You can then instantly get their definitions without leaving the terminal.

## ✨ Features
- **📄 PDF Scanning**: Reads text directly from your PDF books.
- **🧠 Smart Filtering**: Uses CEFR levels (A1-C2) to show only the words you *actually* need to learn.
- **📖 Instant Dictionary**: Fetches meanings, parts of speech, and definitions on the fly.
- **🧹 Auto-Clean**: Handles hyphenated words and weird formatting automatically.
- **🔍 Search Anywhere**: Look up any word manually, right from the prompt.

## 🛠️ Prerequisites
- Python 3.12+
- `pip` (Python package manager)

## ⚡ Quick Start

### 1. Clone & Enter
```bash
git clone <your-repo-url>
cd MeanReaver
```

### 2. Set up Environment
It's best to keep things tidy with a virtual environment.
```bash
python -m venv porenv
source porenv/bin/activate  # Windows: porenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*Note: This will also download the necessary Spacy language model (`en_core_web_sm`).*

### 4. Run it!
Point the tool to your PDF and set a difficulty level.
- **Level 1**: Easy (A1/A2)
- **Level 5**: Advanced (C1/C2)

```bash
python main.py data/your_book.pdf 3
```
*Tip: Place your PDF files in the `data/` folder for easy access.*

## 🎮 How to Use
Once the app is running:

1. **Enter a Page Number**: Type the page number you are reading to analyze it.
   - *Example:* `42`
2. **Review Words**: The tool lists words harder than your chosen level.
3. **Get Definitions**: Type the **index number** next to the word to see what it means.
   - *Example:* `5` (if that's the number next to 'ephemeral')
4. **Manual Search**: Type any word directly text input if you're curious about a specific term.
   - *Example:* `serendipity`
5. **Navigation**: 
   - Enter `-1` to go back or quit.

## 📂 Project Structure
- `main.py`: The brain of the operation.
- `wordrank.py`: The filter (CEFR logic).
- `meaningretriever.py`: The dictionary (API fetcher).
- `show.py`: The display logic.
- `data/`: Put your PDFs here!

---
*Happy Reading!* 🤓