import rsa
import json
with open("out/config.json", mode="r") as f:
    d = json.load(f)
privFileName = d["PrivateKeyFilename"]
print('='*80)
# gerar assinatura digital
# carregar a chave privada
with open(privFileName, mode='rb') as privatefile:
    privkey = rsa.PrivateKey.load_pkcs1(privatefile.read())

# carregar a mensagem de assinatura do arquivo
mensagemDeAssinatura = open('in/mensagem_de_assinatura.txt', mode='rb').read()

# gerar assinatura
assinatura = rsa.sign(mensagemDeAssinatura, privkey, 'SHA-256')

# escrever assinatura em um arquivo
with open('out/assinatura', mode='wb') as f:
    f.write(assinatura)

print("A assinatura foi gerada com o algoritimo de hash: SHA-256")
print("Assinatura gerada com a chave privada")
print('='*80)
