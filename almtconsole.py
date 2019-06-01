#!/usr/bin/env python3
#vim: set syntax=python
from pkg import install, remove
import os
from process import lst
from process import kill
import scriptsrc
import distro
clear = lambda: os.system('clear')
print("|=============================================|")
print("|                                             |")
print("|  A    L    A    M    I    N    U    T    A  |")
print("|                                             |")
print("|=============================================|")
import firewall
print("")
print("")
def defaultFirewall():
    firewall.enable()
    firewall.allow(22)
    firewall.allow(80)
    firewall.allow(443)
    firewall.allow(3306)
    firewall.allow(465)
    firewall.allow(587)
    firewall.allow(993)
    firewall.allow(995)

def option():
    print("Enter number of the operation you want:")
    print("[1] Process Management")
    print("[2] Package management")
    print("[3] Firewall management (UFW)")
    print("[4] Clear thumbnail cache")
    print("[5] Encrypt or Decrypt files")
    print("[6] Get network information")
    print("[7] User management")
while True:
    option()
    operation = int(input("almf> "))
    if(operation == 1):
        clear()
        print("    [1] List processes")
        print("    [2] Kill Process")
        print("    [0] Return to main menu")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
            lst.listproc()
        if(suboperation == 2):
            pidtokill = int(input("PID of the process to kill: "))
            kill.kill(pidtokill)
        if(suboperation == 0):
            continue
    if(operation == 2):
        distro = distro.os_release_info()['id_like']
        if(distro == 'ubuntu' or distro == "debian"):
            clear()
            print("    [1] Install package")
            print("    [2] Remove package")
            print("    [3] Install essential packages")
            print("    [0] Return to main menu")
            suboperation = int(input("almf> "))
            if(suboperation == 1):
                packagetoinstall = input("Package to install: ")
                install.install(packagetoinstall)
            if(suboperation == 2):
                packagetoremove = input("Package to remove: ")
                remove.remove(packagetoremove)
            if(suboperation == 3):
                scriptsrc.installEssential()
            if(suboperation == 0):
                continue
        else:
            print("Your system doesn't support APT package manager!")
    if(operation == 3):
        clear()
        print("    [1] Enable firewall (with default rules)")
        print("    [2] Disable firewall")
        print("    [0] Return to main menu")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
                defaultFirewall()
                print("Firewall started successfully")
        if(suboperation == 2):
                firewall.disable()
                print("Firewall disabled successfully")
        if(suboperation == 0):
            continue
    if(operation == 4):
        clear()
        scriptsrc.cleanCache()
        print("Thumbnail cache cleaned successfully")
    if(operation == 5):
        clear()
        print("    [1] Encrypt")
        print("    [2] Decrypt")
        print("    [0] Return to main menu")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
            clear()
            inputf = input("Enter the input file path: ")
            outputf = input("Enter the output file path: ")
            scriptsrc.encrypt(inputf, outputf)
        if(suboperation == 2):
            clear()
            inputf = input("Enter the input file path: ")
            outputf = input("Enter the output file path: ")
            scriptsrc.decrypt(inputf, outputf)
        if(suboperation == 0):
            continue
    if(operation == 6):
        print("    [1] Get WAN IP")
        print("    [2] Get LAN IP(s)")
        print("    [3] Get router IP")
        print("    [4] Get DNS Nameserver")
        print("    [5] Get MAC Address for interface")
        print("    [6] Get current IP Geodata")
        print("    [0] Return to main menu")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
            scriptsrc.wanIp()
        if(suboperation == 2):
            scriptsrc.lanIp()
        if(suboperation == 3):
            scriptsrc.routerIp()
        if(suboperation == 4):
            scriptsrc.dnsNameserver()
        if(suboperation == 5):
            iface = input("Interface: ")
            scriptsrc.macAddress(iface)
        if(suboperation == 6):
            scriptsrc.ipGeodata()
        if(suboperation == 0):
            continue
    if(operation == 7):
        clear() 
        print("    [1] Create new user")
        print("    [2] Delete user")
        print("    [3] Set root password")
        print("    [0] Return to main menu")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
            newusername = input("Name of the new user: ")
            scriptsrc.adduser(newusername)
        if(suboperation == 2):
            usertodel = input("Name of the user to delete: ")
            scriptsrc.deluser(usertodel)
        if(suboperation == 3):
            scriptsrc.rootpasswd()
        if(suboperation == 0):
            continue
