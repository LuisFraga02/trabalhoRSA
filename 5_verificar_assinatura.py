import rsa
import json
with open("out/config.json", mode="r") as f:
    d = json.load(f)
pubFileName = d["PublicKeyFilename"]
print('='*80)
# carregar a chave publica do arquivo
with open(pubFileName, mode='rb') as publicfile:
    pubkey = rsa.PublicKey.load_pkcs1(publicfile.read())

# carregar a mensagem de assinatura do arquivo
mensagemDeAssinatura = open('in/mensagem_de_assinatura.txt', mode='rb').read()

# carregar a assinatura do arquivo
with open('out/assinatura', mode='rb') as f:
    assinatura = f.read()

# para verificar a assinatura, use a função rsa.verify com os seguintes parametros:
# chave publica
# mensagem de assinatura
# assinatura

# verificar assinatura digital
resultado = rsa.verify(mensagemDeAssinatura, assinatura, pubkey)
# resultado é o algoritmo de hash que foi usado para gerar a assinatura

print('-'*30)
print("Mensagem de assinatura: ")
print(mensagemDeAssinatura.decode())
print('-'*30)

# verificando se a assinatura é valida ou não
# se cair na exceção, a assinatura não é valida
try:
    print("A assinatura foi gerada com o algoritimo de hash: ",resultado)
    rsa.verify(mensagemDeAssinatura, assinatura, pubkey)
    print("A assinatura é valida")
    print('a assinatura foi validada com a chave publica')
except:
    print("A assinatura não é valida a mensagem foi alterada ou a chave publica não é a correta")
print('='*80)

