import scapy.all as scapy

#inisialisasi class berisi method scanning/pemindaian
class Scan:
	def arp(self, ip):
    	# ip berisi alamatIP/subnet
		arp_r = scapy.ARP(pdst=ip)
		# inisialisasi paket ARP sesuai alamat IP tujuan
		br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
		# broadcast paket Ethernet ke semua perangkat local network
		request = br/arp_r
		# membuat payload request,
		# dengan tujuan alamat IP local lalu di broadcast
		answered, unanswered = scapy.srp(request, timeout=1)
		# srp digunakan untuk pengiriman payload berisikan frame ethernet,
		# mengembalikan nilai answered jika dibalas, unaswered jika tidak
		
		# Banner Output
		print('_' * 50)
		print('\tIP\t\t\tMAC')
		print('_' * 50)
		for i in answered:
		    	ip, mac = i[1].psrc, i[1].hwsrc
		    	print(ip, '\t\t' + mac)
		    	print('-' * 50)
		# menampilkan alamat IP dan MAC perangkat yang merespon request
       		

# Minta input dari pengguna
target_ip = input("Masukkan alamat IP/subnet (misalnya 192.168.0.1/24): ")

arp = Scan()  # Membuat instance dari kelas
arp.arp(target_ip)  # Memanggil metode dengan input pengguna
