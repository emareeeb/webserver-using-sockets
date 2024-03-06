import socket
import ssl
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"[{addr}] {msg}")
        response = "Message received by server."
        conn.send(response.encode())
    conn.close()

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certificate.crt', 'private.key')
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_server_socket = context.wrap_socket(server_socket, server_side=True)
    ssl_server_socket.bind(('192.168.0.216', 5566))
    ssl_server_socket.listen(5)
    print("[LISTENING] Server is listening on 192.168.0.216:5566")
    
    while True:
        conn, addr = ssl_server_socket.accept()
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
