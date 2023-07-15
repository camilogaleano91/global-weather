FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Install ipywidgets
RUN pip install geonamescache
RUN pip install ipywidgets
RUN pip install scipy

COPY . .

CMD ["python", "app.py"]

