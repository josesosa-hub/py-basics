#!/usr/bin/env python3

#BRUTEFORCE SIMPLE 28/12/2025

### VARIABLES ###

passwords = ["admin123", "admin", "root", "toor", "user", "password", "contraseña", "login", "administrator"]

password = "login"

intentos = 0

contraseña_encontrada = False

### DATOS ###

user = input("\nUSUARIO --> ")

intentos = 0

### SCRIPT ###

print("\n")
for passwd in passwords:

    intentos += 1

    if passwd == password:

        print(f"\n[+] CONTRASEÑA ENCONTRADA: {passwd} / USUARIO: {user}")
        contraseña_encontrada = True
        break

    else:
        print(f"PROBANDO CONTRASEÑA: {passwd}")


if contraseña_encontrada:

    print(f"\nCONTRASEÑA ENCONTRADA TRAS {intentos} INTENTOS")

else:
        
    print("\n[!] NO SE HA ENCONTRADO LA CONTRASEÑA")

