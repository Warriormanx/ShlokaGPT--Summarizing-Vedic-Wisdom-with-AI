FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    requests \
    beautifulsoup4 \
    torch \
    transformers \
    notebook

COPY Vedic_Text_Summ.ipynb .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
