# 🕉️ ShlokaGPT: Summarizing Vedic Wisdom with AI

ShlokaGPT is an AI-powered Python tool that scrapes purports (spiritual commentaries) from the Śrīmad-Bhāgavatam using [Vedabase.io](https://vedabase.io/) and summarizes them using the powerful `facebook/bart-large-cnn` NLP model. It helps seekers, students, and researchers understand ancient Vedic texts in a simple and digestible format.

---

## ✨ Features

- 🔍 Scrapes purports from specific verse references (e.g., SB 2.2.2)
- 🧠 Uses BART transformer model to generate concise summaries
- 📜FastAPI backend serves the summarization API
- 🖥️ Streamlit frontend provides a user-friendly UI
- 🐳 Dockerized: Easily run the full app in a single container

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – for backend API
- **Streamlit** – for interactive UI
- **BeautifulSoup4** – for HTML scraping from Vedabase
- **HuggingFace Transformers** – to use `facebook/bart-large-cnn`
- **PyTorch** – for model inference
- **Docker** – for containerized deployment


---

## 🧘 Use Cases

- 📖 Quick understanding of Vedic scriptures

- 🧑‍🎓 Study aid for Sanskrit and Vedantic students

- 📚 NLP research in low-resource spiritual languages

---

## ⚠️ Disclaimer

- Always refer to the full purports on Vedabase.io for complete context and spiritual integrity.
---

## 🙏 Acknowledgments
- Vedabase.io – for hosting the sacred Bhāgavatam text

- Facebook AI – for open-sourcing BART

- HuggingFace – for democratizing NLP

## 🧠 Future Improvements
- Add verse auto-suggestion

- Add audio narration of purports
