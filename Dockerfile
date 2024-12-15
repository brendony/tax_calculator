FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends locales=2.36-9+deb12u9 && \
    sed -i -e 's/# en_AU.UTF-8 UTF-8/en_AU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN useradd -m taxman
USER taxman

CMD ["sh", "-c", "/usr/local/bin/textual serve -h 0.0.0.0 -p 8000 \"python -m tax_calculator\""]
