# Student toolbox: everything the TP needs, nothing to install on the laptop.
FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-cryptography openssl curl wget xxd file imagemagick steghide sox libsox-fmt-all ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /work
CMD ["sleep", "infinity"]
