def wtk(text):
    try:
        namefile = "Private key.txt"
        open(namefile, 'w')
        with open(namefile, 'ab') as file:
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(namefile) + " successfully overwritten!")


def wtpk(text):
    try:
        namefile = "Public key.txt"
        open(namefile, 'w')
        with open(namefile, 'ab') as file:
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(namefile) + " successfully overwritten!")


def wtf(text):
    try:
        namefile = "Crypted text.txt"
        open(namefile, 'w')
        with open(namefile, 'ab') as file:
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(namefile) + " successfully overwritten!")


def aes():
    import pyAesCrypt
    from os import remove
    from os.path import splitext
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!");
        raise SystemExit
    fileName = input("Write the file: ")
    paswFile = input("Write the password: ")
    wtk(paswFile)
    bufferSize = 64 * 1024

    def encryptDecrypt(mode, file, password, final=""):
        if mode == 'E':
            try:
                pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, bufferSize)
                remove(file)
            except FileNotFoundError:
                return "[x] File not found!"
            else:
                return "[+] File '" + str(file) + "' overwritten!"
        else:
            try:
                pyAesCrypt.decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
                remove(file)
            except FileNotFoundError:
                return "[x] File not found!"
            except ValueError:
                return "[x] Password is False!"
            else:
                return "[+] File '" + str(splitext(file)[0]) + ".crp' overwritten!"

    print(encryptDecrypt(cryptMode, fileName, paswFile))


def rsa():
    import rsa
    (pub, priv) = rsa.newkeys(1024)
    print("\n" + str(pub))
    wtpk(pub)
    print("\n" + str(priv) + "\n")
    wtk(priv)
    with open("crypt.py", "w") as crypt:
        crypt.write('''
    import rsa 
    pub_key=int(input("Write the PublicKey: "))
    text=input("\\n[*] Write the text:\\n\\n[text] >> ")
    message=text.encode("utf8")
    crypt=rsa.encrypt(message,rsa.PublicKey(pub_key,65537))
    with open("text_crypt.txt","wb") as w:
    	w.write(crypt)
    	print("\\n[*] Crypt-text:\\n\\n"+str(crypt)+"\\n\\n[+] File: 'text_crypt.txt' successfully saved!\\n")
    ''')
    print("\n[+] File: 'crypt.py' successfully saved!")
    with open("key.py", "w") as key:
        key.write('''
    import rsa
    file=input("Write the filename: ")
    with open(file,"rb") as r:
    	read=r.read()
    	message=rsa.decrypt(read,rsa.''' + str(priv) + ''')
    	print("\\n[*] Decrypted text:\\n\\n[text] << "+str(message.decode("utf8"))+"\\n")
    ''')
    print("[+] File: 'key.py' successfully saved!\n")


def caesar():
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!");
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    try:
        rotKey = int(input("Write the key: "))
        wtk(rotKey)
    except ValueError:
        print("Only numbers!");
        raise SystemExit

    def encryptDecrypt(mode, message, key, final=""):
        for symbol in message:
            if mode == 'E':
                final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
            else:
                final += chr((ord(symbol) - key - 13) % 26 + ord('A'))
        return final

    wtf(encryptDecrypt(cryptMode, startMessage, rotKey))
    print("Final message:", encryptDecrypt(cryptMode, startMessage, rotKey))


cryptMode = input("[A]es|[R]sa|[C]aesar: ").upper()
if cryptMode not in ['A', 'R', 'C']:
    print("Error: mode is not Found!");
    raise SystemExit

if cryptMode in ['A', 'a']:
    aes()
if cryptMode in ['R', 'r']:
    rsa()
if cryptMode in ['C', 'c']:
    caesar()
