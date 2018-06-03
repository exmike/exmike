try:
    namefile = input("File-Cover: ")
    with open(namefile, 'rb') as file1:
        read1 = file1.read()
except FileNotFoundError:
    print("[x] File: '" + str(namefile) + "' is not defined!")
    raise SystemExit
try:
    zipfile = input("Zip-File: ")
    with open(zipfile, 'rb') as file2:
        read2 = file2.read()
except FileNotFoundError:
    print("[x] File: '" + str(zipfile) + "' is not defined!")
    raise SystemExit
with open(namefile, 'wb') as file3:
    file3.write(read1)
    file3.write(read2)
    print("[+] File: " + str(namefile) + " successfully overwritten!")
