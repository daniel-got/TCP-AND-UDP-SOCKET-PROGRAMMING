import socket
from datetime import datetime

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '127.0.0.1'
    port = 12345
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[TCP SERVER] Server listening on {host} : {port} . . .")
        
        while True:
            client_socket, addr = server_socket.accept()
            print(f"[TCP SERVER] connected : {addr}")
            
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                waktu = datetime.now().strftime("%H:%M:%S")
                
                pesan_upper = data.upper()
                panjang_char = len(data)
                
                response = f"[{waktu}] {pesan_upper} (Panjang: {panjang_char} char)"
                
                client_socket.send(response.encode('utf-8'))
            except Exception as e:
                print(f"Error saat handling client: {e}")
            finally:
                client_socket.close()

    except OSError as e:
        print(f"Error Port: {e}")
        print(f"Coba jalankan: fuser -k {port}/tcp")  #sesuaikan dengan port yang digunakan
    except Exception as e:
        print(f"Critical Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()
