FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    requests \
    beautifulsoup4 \
    torch \
    transformers \
    jupyter

COPY Vedic_Text_Summ.ipynb .

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]