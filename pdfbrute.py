import pikepdf
from tqdm import tqdm
name = input("Enter Name first FOR CHARS in CPAS:- ")
start = 1900
end = 2022
dob_list = []
desktop = "C:/Users/PC/Desktop/"
filename = input("Enter File Name :- ")
location = desktop + filename
# making DOb LISt
for i in range (start, end):
    dob_list.append(i)

#making Password LISt
password = [name + str(x) for x in dob_list]

# iterate over passwords
for password in password:
    try:
        # open PDF file
        print("Tyring Password :-",password)
        with pikepdf.open(location, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            input('Press ENTER to exit')
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue