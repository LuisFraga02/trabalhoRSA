import rsa
import json
with open("out/config.json", mode="r") as f:
    d = json.load(f)
privFileName = d["PrivateKeyFilename"]
print('='*80)
# carregar a chave privada
with open(privFileName, mode='rb') as privatefile:
    privkey = rsa.PrivateKey.load_pkcs1(privatefile.read())

# carregar a mensagem encriptada do arquivo
mensagemEncriptada = open('out/mensagem_Encriptada.txt', mode='rb').read()

# decriptar a mensagem
mensagemDecriptada = rsa.decrypt(mensagemEncriptada, privkey)

# escrever mensagem decriptada em um arquivo
with open('out/mensagem_Decriptada.txt', mode='wb') as mensagemDecriptadaFile:
    mensagemDecriptadaFile.write(mensagemDecriptada)

print('Mensagem decriptada com a chave privada!')
print('='*80)