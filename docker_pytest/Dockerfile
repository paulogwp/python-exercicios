# 1. Usa a versão do seu Python local
FROM python:3.14-slim

# 2. Cria a pasta do app dentro do container
WORKDIR /app

# 3. Copia a lista de dependências
COPY requirements.txt .

# 4. Instala o pytest
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia seus códigos e testes
COPY . .

# 6. Comando para rodar os testes automaticamente
CMD ["pytest", "-vs"]