# Import Module
import hashlib

# Colors 
Blue = "\033[1;0;34m"
Green = "\033[1;92m"
White = "\033[1;97m"

def BannerFunction():
    

    print(f"""{Blue}
                
          ---------------------------------------
          |  PyHasees v1.0 - Hash Generator     |
          ---------------------------------------

                 Author : Md. Nur Habib
             Programmer & Full Stack Developer.
     
          GitHub     : github.com/thenurhabib
          Twitter    : twitter.com/thenurhab1b
          Facebook   : facebook.com/thenurhab1b 
          HackerRank : hackerrank.com/thenurhabib
    
    """)


# Hash Variabls.
hash1 = hashlib.md5()
hash2 = hashlib.sha1()
hash3 = hashlib.sha224()
hash4 = hashlib.sha256()
hash5 = hashlib.sha384()
hash6 = hashlib.sha3_224()
hash7 = hashlib.sha3_256()
hash8 = hashlib.sha3_384()
hash9 = hashlib.sha3_512()
hash10 = hashlib.sha512()




# Print banner
BannerFunction()

# Print Options
print(f""" {Green}
         
   Select a number.
   ----------------
   01. MD5
   02. sha1
   03. sha224
   04. sha256
   05. sha384
   06. sha3_224
   07. sha3_256
   08. sha3_384
   09. sha3_512
   10. sha512

"""
)


# get Input From User
getanumber = input(f"{White}Select a Number : ")
password = input("Enter Your text : ")


# Password Hashing
hash1.update(password.encode("utf-8"))
hash2.update(password.encode("utf-8"))
hash3.update(password.encode("utf-8"))
hash4.update(password.encode("utf-8"))
hash5.update(password.encode("utf-8"))
hash6.update(password.encode("utf-8"))
hash7.update(password.encode("utf-8"))
hash8.update(password.encode("utf-8"))
hash9.update(password.encode("utf-8"))
hash10.update(password.encode("utf-8"))

# Hashes
md5 = f"MD5 Encryption  : {hash1.hexdigest()}"
sha1 = f"sha1 Encryption : {hash2.hexdigest()}"
sha224 = f"sha224 Encryption : {hash3.hexdigest()}"
sha256 = f"sha256 Encryption : {hash4.hexdigest()}"
sha384 = f"sha384 Encryption : {hash5.hexdigest()}"
sha3_224 = f"sha3_224 Encryption : {hash6.hexdigest()}"
sha3_256 = f"sha3_256 Encryption : {hash7.hexdigest()}"
sha3_384 = f"sha3_384 Encryption : {hash8.hexdigest()}"
sha3_512 = f"sha3_512 Encryption : {hash9.hexdigest()}"
sha512 = f"sha512 Encryption : {hash10.hexdigest()}"


# Print Selected hash.
try:
    while True:
        if getanumber == "1" or "01":
            print(md5)
            break
        if getanumber == "2" or "02":
            print(sha1)
            break
        if getanumber == "3" or "03":
            print(sha224)
            break
        if getanumber == "4" or "04":
            print(sha256)
            break
        if getanumber == "5" or "05":
            print(sha384)
            break
        if getanumber == "6" or "06":
            print(sha3_224)
            break
        if getanumber == "7" or "07":
            print(sha3_256)
            break
        if getanumber == "8" or "08":
            print(sha3_384)
            break
        if getanumber == "9" or "09":
            print(sha3_512)
            break
        if getanumber == "10":
            print(sha512)
            break
        else:
            print("Please Enter a Number Between 1 or 10.")
except Exception as err:
    print(f"An Error Occund : {err}")
