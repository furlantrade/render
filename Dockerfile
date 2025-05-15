FROM python:3.10-slim

# Instala dependências
RUN apt update && \
    apt install -y curl unzip && \
    curl -L https://github.com/foundry-rs/foundry/releases/latest/download/anvil-linux.zip -o anvil.zip && \
    unzip anvil.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/anvil && \
    rm anvil.zip

# Copia os arquivos do projeto
WORKDIR /app
COPY . .

# Instala bibliotecas Python
RUN pip install -r requirements.txt

# Expõe a porta do Anvil
EXPOSE 8545

# Executa o script inicial
CMD ["bash", "start.sh"]