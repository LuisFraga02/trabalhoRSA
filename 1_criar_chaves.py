import rsa
import json
# subprocess é uma biblioteca para executar comandos do sistema operacional
import subprocess

# .bat commands
commands = [
    'cls',
]

# Executa os comandos .bat na lista commands
for command in commands:
    subprocess.Popen(command, shell=True).wait()

hasPub = False
hasPriv = False

# mensagem de boas vindas
print('='*80)
print('+'*80)
print('Bem vindo ao gerador de chaves RSA')
print('Tamanho da chave em bits, quanto maior mais segura')
print('1 - 512 é muito inseguro')
print('2 - 1024 é o padrão')
print('3 - 2048 é mais seguro e mais lento')
print('4 - 4096 é ainda mais seguro, mas muito mais lento')
print('qualquer outro valor será considerado o padrão de 1024 bits')
print('+'*80)
inputSize = input("Digite o tamanho da chave desejada : ")
print('*'*80)

# definir o tamanho da chave
if inputSize == '1':
    size = 512
elif inputSize == '2':
    size = 1024
elif inputSize == '3':
    size = 2048
elif inputSize == '4':
    size = 4096
else:
    size = 1024



# gerar par de chaves com a biblioteca rsa
(publica, privada) = rsa.newkeys(size)



# o pkcs1 é um padrão de criptografia de chave pública
# que define o formato de chaves públicas e privadas em arquivos PEM (Privacy Enhanced Mail)
size = str(size)
# salvar a chave privada com pkcs1 e com o tamanho da chave no nome do arquivo
pubFileName = 'out/CHAVE_PUBLICA_RSA_'+ str(size) +'.pem'
with open(pubFileName, mode='wb') as f:
    f.write(publica.save_pkcs1())

# salvar a chave privada com pkcs1 e com o tamanho da chave no nome do arquivo
privFileName = 'out/CHAVE_PRIVADA_RSA_'+ size +'.pem'
with open(privFileName, mode='wb') as f:
    f.write(privada.save_pkcs1())

# criar o json de configuração
data = {
    "size": size,
    "PrivateKeyFilename" : privFileName,
    "PublicKeyFilename" : pubFileName
}
# setar o tamanho da chave no json de configuração e se tem chave privada e pública
with open('out/config.json', mode='w') as f:
    json.dump(data, f)

print('')
print("Chaves com o tamanho de {} bits criadas com sucesso".format(size))
print('')
print('='*80)
