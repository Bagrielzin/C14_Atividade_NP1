import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

username = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")
emails = os.getenv("EMAIL_TO")
status = os.getenv("PIPELINE_STATUS", "desconhecido")

repo = os.getenv("GITHUB_REPOSITORY", "N/A")
run_number = os.getenv("GITHUB_RUN_NUMBER", "N/A")

print("Iniciando envio de emails...")

if not username or not password:
    print("Erro: credenciais de email não configuradas.")
    exit(1)

if not emails:
    print("Erro: nenhum destinatário configurado.")
    exit(1)

lista_emails = [email.strip() for email in emails.split(",") if email.strip()]

if status == "success":
    subject = "✅ Pipeline executado com sucesso"
else:
    subject = "❌ Pipeline falhou"

corpo = f"""
Status do pipeline: {status}

Repositório: {repo}
Execução: #{run_number}
"""

try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(username, password)

        for destino in lista_emails:
            try:
                msg = MIMEMultipart()
                msg["From"] = username
                msg["To"] = destino
                msg["Subject"] = subject

                msg.attach(MIMEText(corpo, "plain"))

                server.send_message(msg)
                print(f"Email enviado para: {destino}")

            except Exception as e:
                print(f"Erro ao enviar para {destino}: {e}")

    print("Envio finalizado!")

except Exception as e:
    print("Erro geral ao conectar/enviar emails:", e)
    exit(1)