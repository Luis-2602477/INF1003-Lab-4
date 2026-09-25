FROM python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .

CMD ["python", "modular_auditor.py"]