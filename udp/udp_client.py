import socket

def start_udp_client():
    # 1. Setup Socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client_socket.settimeout(5)
    
    host = '127.0.0.1'
    port = 54321
    
    print("=== UDP CLIENT (Variasi Perkalian) ===")
    print("Ketik 'exit' untuk keluar.")
    
    try:
        while True:
            # 2. Input User
            pesan = input("\nMasukkan angka: ")
            
            if pesan.lower() == 'exit':
                break
            
            try:
                client_socket.sendto(pesan.encode('utf-8'), (host, port))
                
                # 4. Terima Balasan (Pake Timeout)
                response, server_addr = client_socket.recvfrom(1024)
                print(f"[UDP CLIENT] Hasil dari Server: {response.decode('utf-8')}")
                
            except socket.timeout:
                print("[UDP CLIENT] Timeout! Server tidak merespon atau paket hilang.")
            except Exception as e:
                print(f"[UDP CLIENT] Error transmisi: {e}")
                
    except KeyboardInterrupt:
        print("\nKeluar...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_udp_client()
