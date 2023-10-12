import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Cargar la clave pública del servidor
with open("server_public_key.pem", "rb") as f:
    server_public_pem = f.read()
    server_public_key = serialization.load_pem_public_key(server_public_pem, backend=default_backend())

# Establecer la conexión con el servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Datos a enviar al servidor
#data = "Hola, servidor!"
data = input()
encrypted_data = server_public_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# Enviar datos cifrados al servidor
print(encrypted_data)
client.send(encrypted_data)
client.close()
