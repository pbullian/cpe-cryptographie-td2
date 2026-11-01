# Service de chiffrement du Bureau (mission S2).
FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends python3-flask python3-cryptography \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY app.py classified.dat ./
EXPOSE 8000
CMD ["python3", "app.py"]
