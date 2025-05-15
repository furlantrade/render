FROM python:3.11-slim

WORKDIR /app

# Instala curl e unzip
RUN apt update && apt install -y curl unzip

# Baixa e instala o anvil
RUN curl -L https://foundry.paradigm.xyz | bash && \
    ~/.foundry/bin/foundryup && \
    cp ~/.foundry/bin/anvil /usr/local/bin/anvil && \
    chmod +x /usr/local/bin/anvil

# Copia os arquivos Python
COPY impersonate_send.py .
COPY impersonate_send_usdt.py .
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8545

# Inicia o Anvil
CMD ["anvil", "--fork-url", "https://ethereum.publicnode.com", "--chain-id", "1"]
