# 🌐 Web Server Design with SSL Connection Demonstration 🇮🇳

This project demonstrates the development of a basic web server using sockets in Python, showcasing the connection establishment between a client and a server with SSL encryption added for secure communication.

## Prerequisites 🛠️

Before starting, ensure you have OpenSSL installed on your system. If not, follow these steps to download and install OpenSSL:

1. Navigate to [Win32 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html).
2. Choose your operating system and preferred file type. (e.g., Win64 OpenSSL v3.2.1 200mb EXE).
3. Download the file.
4. Visit the location where Openssl is downloaded and navigate to the bin folder.
5. Copy the path and paste it in the System Environment Variables.

## Generating SSL Certificates 📜

To generate SSL certificates, execute the following commands in your terminal or command prompt:

```bash
openssl genrsa -aes256 -out private.key 2048
openssl rsa -in private.key -out private.key
openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500
openssl req -x509 -new -nodes -key private.key -sha1 -days 36500 -out ssl.pem
```

When prompted, provide the necessary details such as your name, organization name, etc.

Once the commands are executed, navigate to the location where OpenSSL is installed on your local machine (e.g., `C:/Users/YourName`). Copy the `certificate.crt` and `private.key` files generated there.

## Setup ⚙️

1. Place the `certificate.crt` and `private.key` files into the folder containing the server and client files.
2. Make sure that the server and client code files are present in the same directory.

## Running the Server and Client 🏃‍♂️🏃‍♀️

1. Run the server script first.
2. Run the client script next.
3. Ensure that the IP addresses in the code of both the client and server match.

You can run multiple clients simultaneously with the same server setup.

## Note 📝

This project provides a basic demonstration of establishing a secure connection between a client and a server using SSL encryption. Additional features and optimizations can be implemented based on specific requirements and use cases.

👨‍💻 **Author:** Areeb Ahmed 

🏢 **Organization:** Private/Curiosity

📬 **Mail Address:** areebmobile@gmail.com

🕸️ **Instagram:** @emareeeb 

📍 **Location:** Bengaluru 🇮🇳.
