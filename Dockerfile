FROM python:3.11-slim

WORKDIR /app

# Copia tudo
COPY . .

# Torna o anvil executável
RUN chmod +x ./anvil

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Anvil
EXPOSE 8545

# Comando para iniciar o Anvil no Render
CMD ["./anvil", "--fork-url", "https://ethereum.publicnode.com", "--chain-id", "1"]
