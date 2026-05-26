<<<<<<< HEAD
FROM python:3.10.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
=======
FROM python:3.10.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
>>>>>>> c55ef92f5cbf4d7ebb45c635610cb3537a88c623
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]