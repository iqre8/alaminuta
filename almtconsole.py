#!/usr/bin/env python3
#vim: set syntax=python
from pkg import install, remove
import os
from process import lst
from process import kill
import scriptsrc
import distro
from termcolor import cprint, colored
clear = lambda: os.system('clear')
print(colored(" __ _| |__ _ _ __ (_)_ _ _  _| |_ __ _ ", "yellow", attrs=['bold']))
print(colored("/ _` | / _` | '  \| | ' \ || |  _/ _` |", "yellow", attrs=['bold']))
print(colored("\__,_|_\__,_|_|_|_|_|_||_\_,_|\__\__,_|", "yellow", attrs=['bold']))
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
    print(colored("Enter number of the operation you want:", "yellow", attrs=['bold']))
    cprint("[1] Process Management", "magenta")
    cprint("[2] Package management", "magenta")
    cprint("[3] Firewall management (UFW)", "magenta")
    cprint("[4] Clear thumbnail cache", "magenta")
    cprint("[5] Encrypt or Decrypt files", "magenta")
    cprint("[6] Get network information", "magenta")
    cprint("[7] User management", "magenta")
    cprint("[0] Exit alaminuta", "magenta")
while True:
    option()
    operation = int(input("almf> "))
    if(operation == 1):
        clear()
        cprint("    [1] List processes", "magenta")
        cprint("    [2] Kill Process", "magenta")
        cprint("    [0] Return to main menu", "magenta")
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
            cprint("    [1] Install package", "magenta")
            cprint("    [2] Remove package", "magenta")
            cprint("    [3] Install essential packages", "magenta")
            cprint("    [0] Return to main menu", "magenta")
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
            cprint("Your system doesn't support APT package manager!", "red")
            continue
    if(operation == 3):
        clear()
        cprint("    [1] Enable firewall (with default rules)", "magenta")
        cprint("    [2] Disable firewall", "magenta")
        cprint("    [0] Return to main menu", "magenta")
        suboperation = int(input("almf> "))
        if(suboperation == 1):
                defaultFirewall()
                cprint("Firewall started successfully", "green")
        if(suboperation == 2):
                firewall.disable()
                cprint("Firewall disabled successfully", "green")
        if(suboperation == 0):
            continue
    if(operation == 4):
        clear()
        scriptsrc.cleanCache()
        cprint("Thumbnail cache cleaned successfully", "green")
    if(operation == 5):
        clear()
        cprint("    [1] Encrypt", "magenta")
        cprint("    [2] Decrypt", "magenta")
        cprint("    [0] Return to main menu", "magenta")
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
        cprint("    [1] Get WAN IP", "magenta")
        cprint("    [2] Get LAN IP(s)", "magenta")
        cprint("    [3] Get router IP", "magenta")
        cprint("    [4] Get DNS Nameserver", "magenta")
        cprint("    [5] Get MAC Address for interface", "magenta")
        cprint("    [6] Get current IP Geodata", "magenta")
        cprint("    [0] Return to main menu", "magenta")
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
        cprint("    [1] Create new user", "magenta")
        cprint("    [2] Delete user", "magenta")
        cprint("    [3] Set root password", "magenta")
        cprint("    [0] Return to main menu", "magenta")
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

    if(operation == 0):
        exit()
