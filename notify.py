import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")
emails = os.getenv("EMAIL_TO")
status = os.getenv("PIPELINE_STATUS", "desconhecido")

print("Iniciando envio de emails...")

if not emails:
    print("Nenhum email configurado.")
    exit(1)

lista_emails = [email.strip() for email in emails.split(",")]

msg = MIMEMultipart()
msg["From"] = username

# Assunto dinâmico
if status == "success":
    msg["Subject"] = "✅ Pipeline executado com sucesso"
else:
    msg["Subject"] = "❌ Pipeline falhou"

corpo = f"""
Status do pipeline: {status}

Repositório: {os.getenv('GITHUB_REPOSITORY')}
Execução: {os.getenv('GITHUB_RUN_NUMBER')}
"""

msg.attach(MIMEText(corpo, "plain"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(username, password)

        for destino in lista_emails:
            msg["To"] = destino
            server.send_message(msg)
            print(f"Email enviado para: {destino}")

    print("Envio concluído!")

except Exception as e:
    print("Erro ao enviar email:", e)
    exit(1)