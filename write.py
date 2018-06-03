try:
    namefile = input("File name: ")
    with open(namefile, 'ab') as file:
        text = input("Write the text: ")
        file.write(text.encode("utf-8"))
except FileNotFoundError:
    print("[x] File: '" + str(namefile) + "' is not defined!")
    raise SystemExit
else:
    print("[+] File: " + str(namefile) + " successfully overwritten!")
