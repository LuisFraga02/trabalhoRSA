import rsa
import json


with open("out/config.json", mode="r") as f:
    d = json.load(f)
pubFileName = d["PublicKeyFilename"]

print('='*80)

with open("out/config.json", mode="r") as f:
    data = json.load(f)


# carregar a chave pública
with open(pubFileName, mode="rb") as publicfile:
    pubkey = rsa.PublicKey.load_pkcs1(publicfile.read())

# escrever mensagem
# message = input("Escreva uma mensagem para ser encriptada: ")

# pegar mensagem do arquivo
with open("in/mensagem.txt", mode="r") as f:
    mensagem = f.read()

# encriptar a mensagem
mensagemEncriptada = rsa.encrypt(mensagem.encode(), pubkey)

# escrever mensagem encriptada em um arquivo
with open("out/mensagem_Encriptada.txt", mode="wb") as f:
    f.write(mensagemEncriptada)

print("Mensagem encriptada com a chave publica")
print('='*80)