
import pyAesCrypt, os
print("---------------------------------------------------------------")
file=input("File name: ")
password=input("Password: ")
bufferSize = 64*1024
try: 
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
except FileNotFoundError: 
	print("[x] File not found!")
except ValueError: 
	print("[x] Password is Fasle!")
else: 
	print("[+] File '"+str(os.path.splitext(file)[0])+"' successfully saved!")
finally: 
	print("---------------------------------------------------------------")
