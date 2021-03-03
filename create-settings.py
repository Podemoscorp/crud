import os
import json

dados = {
    "type": "service_account",
    "project_id": os.environ.get("PROJECT_ID"),
    "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
    "private_key": os.environ.get("PRIVATE_KEY"),
    "client_email": os.environ.get("CLIENT_EMAIL"),
    "client_id": os.environ.get("CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/254642947670-compute%40developer.gserviceaccount.com",
}

print("[INFO] Criando arquivo...")

with open(os.environ.get("CREDENCIAIS_FILE"), "w") as json_file:
    json.dump(dados, json_file, indent=4)

print("[INFO] Verificando existensia do arquivo...")

if os.path.exists(os.environ.get("CREDENCIAIS_FILE")):
    print("[INFO] Arquivo criado com sucesso ...")
else:
    print("[INFO] Erro ao criar arquivo ...")


print("[INFO] finalizando programa.")
