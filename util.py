import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer

# Load summarization model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def scrape_purport(verse_ref: str) -> str | None:
    url = f"https://vedabase.io/en/library/sb/{verse_ref.replace('.', '/')}/"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        selectors = [
            'div.r-purport', 'div.purport-wrapper', 
            'div.verse-text', 'div#purport', 'article'
        ]
        for selector in selectors:
            purport = soup.select_one(selector)
            if purport:
                return purport.get_text(' ', strip=True)
        main_content = soup.find('main') or soup.find('div', class_='content')
        if main_content:
            return main_content.get_text(' ', strip=True)[:20000]
    except Exception as e:
        print(f"Error: {e}")
    return None

def summarize_text(text: str, max_length: int = 150, min_length: int = 30) -> str:
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
