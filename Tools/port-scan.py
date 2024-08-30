import sys
import socket

# Mengambil input dari pengguna
target_input = input("Masukkan alamat yang akan di-scan: ")

# Menyaring input
try:
	target = socket.gethostbyname(target_input)
    	# mengubah semua input user menjadi format IPv4
except socket.gaierror:
	print("Hostname tidak valid")
	sys.exit()
	#error code jika input tak valid

# Banner Output
print("-" * 50)
print("Scanning/Memindai Target: " + target)
# menampilkan input user berupa alamat IP
print("-" * 50)

# fungsi utama
try:
	# Memindai port dari 1 hingga 65,535
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# buka socket (TCP)
		socket.setdefaulttimeout(5)
		# set timeout 5
		 
		# Mengembalikan indikator kesalahan
		result = s.connect_ex((target, port))
		# cek apakah port dalam range bisa di koneksian atau tidak
		# jika bisa -> result = 0
		if result == 0:
			print("Port {} is open".format(port))
			# mengembalikan port yang tersedia
		s.close()
		# menutup socket
         
except KeyboardInterrupt:
    	print("\n Exiting Program !!!!")
    	sys.exit()
    	# exit program jika di interupt user
