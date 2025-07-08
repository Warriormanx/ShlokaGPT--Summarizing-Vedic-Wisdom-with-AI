FROM python:3.10-slim

WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all 
COPY . .

# Expose ports: FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Run both apps using a shell script
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.address=0.0.0.0"]
