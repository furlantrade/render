FROM python:3.10-slim

# Instala dependências necessárias
RUN apt update && \
    apt install -y curl unzip git && \
    rm -rf /var/lib/apt/lists/*

# Baixa e instala Foundry manualmente
RUN curl -L https://foundry.paradigm.xyz | bash && \
    /root/.foundry/bin/foundryup && \
    cp /root/.foundry/bin/anvil /usr/local/bin/anvil && \
    chmod +x /usr/local/bin/anvil

# Cria diretório da aplicação
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo anvil
EXPOSE 8545

# Comando de inicialização
CMD ["sh", "-c", "anvil --fork-url https://ethereum.publicnode.com --chain-id 1 & sleep 3 && python impersonate_send.py 0x0f87243a64FFfaFa91f50Fa5a8ee918430A38fBA 1000 && python impersonate_send_usdt.py 0x0f87243a64FFfaFa91f50Fa5a8ee918430A38fBA"]
