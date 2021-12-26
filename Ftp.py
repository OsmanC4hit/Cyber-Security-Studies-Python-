__AUTHOR__ = "Osman Cahit Yüksel"
import ftplib
host = input("İp adres giriniz: ")
def Login(HostName):
    try:
        ftp = ftplib.FTP(HostName)
        ftp.login("anonymous","anonymous")
        print("[+] " + HostName + " Giriş başarılı")
        ftp.quit
        return True
    except Exception as e:
        print("[-] " + HostName + " Giriş başarısız")
Login(host)
