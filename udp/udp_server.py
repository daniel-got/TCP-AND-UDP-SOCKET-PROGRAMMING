import socket
import sys

def start_udp_server():
    # Setup Socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind ke '' (All Interfaces) sesuai slide kuliah Hal. 103
    host = '' 
    port = 54321
    
    try:
        print(f"[DEBUG] Binding ke port {port}...")
        server_socket.bind((host, port))
        print(f"[UDP SERVER] Ready to receive on port {port} (All Interfaces)...")
        
        while True:
            print("[DEBUG] Menunggu paket masuk (recvfrom)...")
            
            # Tangkap data
            data, addr = server_socket.recvfrom(1024)
            
            message = data.decode('utf-8')
            print(f"[UDP SERVER] Menerima dari {addr}: {message}")
            
            # Logika Perkalian
            try:
                angka = int(message)
                hasil = angka * 2
                response = str(hasil)
            except ValueError:
                response = "Error: Input harus angka!"
            
            # Kirim Balasan
            server_socket.sendto(response.encode('utf-8'), addr)

    except KeyboardInterrupt:
        print("\n[UDP SERVER] Matikan manual.")
    except Exception as e:
        print(f"[UDP SERVER] CRITICAL ERROR: {e}")
        # Tampilkan baris error biar jelas
        import traceback
        traceback.print_exc()
    finally:
        server_socket.close()
        print("[DEBUG] Socket ditutup.")

if __name__ == "__main__":
    start_udp_server()
