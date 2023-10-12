import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Cargar la clave privada del servidor
with open("server_private_key.pem", "rb") as f:
    server_private_pem = f.read()
    server_private_key = serialization.load_pem_private_key(server_private_pem, password=None, backend=default_backend())

# Configurar el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Esperando conexiones...")

conn, addr = server.accept()
print(f"Conexión establecida con {addr}")

# Recibir datos cifrados del cliente
data = conn.recv(4096)
print(data)
decrypted_data = server_private_key.decrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print(f"Datos recibidos del cliente: {decrypted_data.decode()}")

conn.close()
server.close()
