import socket

def start_tcp_client():
    host = '127.0.0.1'
    port = 12345

    try:
        while True:
            # 1. Bikin Socket BARU setiap kali mau kirim
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            try:
                # 2. Connect dulu
                client_socket.connect((host, port))
                
                # 3. Input & Kirim
                message = input("Masukkan pesan (TCP): ")
                if message.lower() == 'exit': break # Cara keluar loop
                
                client_socket.send(message.encode('utf-8'))
                
                # 4. Terima
                client_socket.settimeout(10)
                response = client_socket.recv(1024).decode('utf-8')
                print(f"[TCP CLIENT] Respon: {response}")
                
            except Exception as e:
                print(f"Error: {e}")
            finally:
                # 5. WAJIB TUTUP per pesan karena Server juga menutup per pesan
                client_socket.close()
                
    except KeyboardInterrupt:
        print("\nKeluar...")

if __name__ == "__main__":
    start_tcp_client()
