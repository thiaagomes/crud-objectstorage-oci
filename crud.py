import boto3
import os

# Defina as credenciais da sua conta Oracle Cloud Infrastructure
access_key = ''
secret_key = ''

# Defina o nome do bucket no Oracle Object Storage
bucket_name = 'nome-bucket'

# Defina o caminho para o diretório local que contém os arquivos que você deseja enviar
local_path = (r'C:\Users\Thiago Gomes\repositorios')

# Crie uma conexão com o Oracle Object Storage
client = boto3.client('s3',
                      region_name='sa-saopaulo-1',  # substitua pelo nome da sua região
                      endpoint_url='https://.compat.objectstorage.sa-saopaulo-1.oraclecloud.com',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

# Itere sobre os arquivos no diretório local e faça o upload de cada arquivo para o bucket
for filename in os.listdir(local_path):
    file_path = os.path.join(local_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            client.upload_fileobj(f, bucket_name, filename)
        print(f'O arquivo {filename} foi enviado com sucesso para o bucket {bucket_name}!')

# Criar um objeto no bucket
object_name = 'teste-python'
file_path ='C:\\Users\\ThiagoGomes\\Downloads'
with open(file_path, 'rb') as f:
    client.upload_fileobj(f, bucket_name, object_name)
print(f'O objeto {object_name} foi criado com sucesso no bucket {bucket_name}!')

# Ler um objeto no bucket
response = client.get_object(Bucket=bucket_name, Key=object_name)
content = response['Body'].read()
print(f'O conteúdo do objeto {object_name} é: {content}')

# Atualizar um objeto no bucket
new_object_name = 'novo nome do seu objeto'
response = client.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': object_name},
                              Key=new_object_name)
client.delete_object(Bucket=bucket_name, Key=object_name)
print(f'O objeto {object_name} foi atualizado com sucesso para {new_object_name}!')

# Deletar um objeto no bucket
client.delete_object(Bucket=bucket_name, Key=new_object_name)
print(f'O objeto {new_object_name} foi deletado com sucesso do bucket {bucket_name}!')