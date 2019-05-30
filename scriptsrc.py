import subprocess
from pkg import install, remove
def wanIp():
    subprocess.call(["scriptsh/geo.sh", "-w"])
def lanIp():
    subprocess.call(["scriptsh/geo.sh", "-l"])
def routerIp():
    subprocess.call(["scriptsh/geo.sh", "-r"])
def dnsNameserver():
    subprocess.call(["scriptsh/geo.sh", "-d"])
def macAddress(interface):
    subprocess.call(["scriptsh/geo.sh", "-m", interface])
def ipGeodata():
    subprocess.call(["scriptsh/geo.sh", "-g"])
def cleanCache():
    subprocess.call("scriptsh/clean.sh")
def encrypt(inputf, outputf):
    subprocess.call(["scriptsh/crypt.sh", "-e", inputf, outputf])
def decrypt(inputf, outputf):
    subprocess.call(["scriptsh/crypt.sh", "-d", inputf, outputf])
def installEssential():
    install.install("unace")
    install.install("rar")
    install.install("unrar")
    install.install("p7zip-rar")
    install.install("p7zip")
    install.install("sharutils")
    install.install("uudeview")
    install.install("mpack")
    install.install("arj")
    install.install("cabextract")
    install.install("lzip")
    install.install("lunzip")
    install.install("plzip")
    install.install("default-jre")
    install.install("default-jdk")
def adduser(name):
    subprocess.call(["scriptsh/useradd.sh", name])
def deluser(name):
    subprocess.call(["scriptsh/userdel.sh", name])
def rootpasswd():
    subprocess.call("scriptsh/passwdroot.sh")
