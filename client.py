import socket
import ssl

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE


    client = context.wrap_socket(client, server_hostname=None)
    client.connect(('192.168.127.151', 5566)) 
    
    print("[CONNECTED] Client connected to server.")
    while True:
        msg = input("Enter message: ")
        client.send(msg.encode())
        if msg == 'exit':
            break
        response = client.recv(1024).decode()
        print(f"[SERVER] {response}")
    client.close()

if __name__ == "__main__":
    main()
