from scapy.all import *
import socket

#inisialisasi fungsi traceroute
def traceroute(destination, max_hops=30, timeout=2):
	destination_ip = socket.gethostbyname(destination)
	# mengubah alamat domain menjadi alamat IP
	for ttl in range(1, max_hops + 1):
	# ttl menghitung berapa banyak hops yang sudah dilalui
		pkt = IP(dst=destination_ip, ttl=ttl) / ICMP()
		#pembuatan paket jaringan,
		# tujuan paket adalah input user,
		# menambahkan header ICMP agar paket dapat diterima dengan baik oleh hops
		reply = sr1(pkt, timeout=timeout, verbose=0)
		#menyimpan reply hasil pengiriman paket+header ke jaringan
		
		#kondisi untuk menentukan output hasil reply,
		# dari tiap-tiap hops yang berhasil dilintasi
		if reply is None:
			print(f"{ttl:<2} *")
			#kondisi timeout atau tak ada balasan,
			# looping kembali
		elif reply.type == 0:
			print(f"{ttl:<2} {reply.src}")
			break
			#kondisi terdapat reply dan destination IP berhasil ditemukan,
			# output ttl & alamat IP,
			# keluar dari loop
		else:
			print(f"{ttl:<2} {reply.src}")
			#kondisi terdapat reply namun bukan destination IP,
			# output ttl & alamat IP,
			# looping kembali

def main():
	# mengambil input dari pengguna
	destination = input("Masukkan alamat IP atau domain yang akan di traceroute: ")
	max_hops = int(input("Masukkan batasan output (maksimum jumlah hops): "))
	    
	# menjalankan fungsi traceroute berdasarkan input dari pengguna
	traceroute(destination, max_hops=max_hops)

if __name__ == "__main__":
    	main()
