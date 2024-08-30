import sys
import socket
from scapy.all import *
import scapy.all as scapy

# Fungsi untuk Traceroute
def traceroute(destination, max_hops=30, timeout=2):
    destination_ip = socket.gethostbyname(destination)
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=destination_ip, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=timeout, verbose=0)
        
        if reply is None:
            print(f"{ttl:<2} *")
        elif reply.type == 0:
            print(f"{ttl:<2} {reply.src}")
            break
        else:
            print(f"{ttl:<2} {reply.src}")

# Fungsi untuk Port Scan
def port_scan(target_input):
    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("Hostname tidak valid")
        sys.exit()

    print("-" * 50)
    print("Scanning/Memindai Target: " + target)
    print("-" * 50)

    try:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(5)
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\nExiting Program!!!!")
        sys.exit()

# Fungsi untuk ARP Scan
class Scan:
    def arp(self, ip):
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br / arp_r
        answered, unanswered = scapy.srp(request, timeout=1, verbose=False)

        print('_' * 50)
        print('\tIP\t\t\tMAC')
        print('_' * 50)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 50)

# Antarmuka Pengguna
def main():
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Traceroute")
    print("2. Port Scan")
    print("3. ARP Scan")
    
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        destination = input("Masukkan alamat IP atau domain yang akan di traceroute: ")
        max_hops = int(input("Masukkan batasan output (maksimum jumlah hops): "))
        traceroute(destination, max_hops=max_hops)
    elif choice == '2':
        target_input = input("Masukkan alamat yang akan di-scan: ")
        port_scan(target_input)
    elif choice == '3':
        target_ip = input("Masukkan alamat IP/subnet (misalnya 192.168.0.1/24): ")
        arp = Scan()
        arp.arp(target_ip)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
