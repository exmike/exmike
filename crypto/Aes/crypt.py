
import pyAesCrypt
print("---------------------------------------------------------------" )
file=input("File name: ")
password=input("Password: ")
bufferSize = 64*1024
try: 
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
except FileNotFoundError: 
	print("[x] File not found!")
else: 
	print("[+] File '"+str(file)+".crp' successfully saved!")
finally: 
	print("---------------------------------------------------------------")
