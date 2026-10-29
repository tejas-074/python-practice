FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium
COPY . .
RUN python setup_foodapp.py
CMD ["pytest"]