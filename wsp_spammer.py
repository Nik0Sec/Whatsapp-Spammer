# Whatsapp spammer
# Creado por Nik0
from colorama import init
from selenium import webdriver
from time import sleep, time
import colorama as colorama
from selenium.webdriver.common.keys import Keys
from progress.bar import Bar
import os

init(autoreset=True)


def banner1():
    os.system("clear")
    print(colorama.Fore.YELLOW + """Spammer Whatsapp 
    Creado por: https://nik0sec.github.io/""")
    bar = Bar('Cargando', max=100)
    for i in range(100):
        sleep(0.03)
        bar.next(1)
    bar.finish()
    sleep(1)
    os.system("clear")


def main():
    while True:
        driver = webdriver.Firefox() # Se inicia la página
        for i in range(8):
            print(colorama.Fore.RED + "Espera a que cargue la pagina!")
            sleep(1)
        os.system("clear")
        driver.get('http://web.whatsapp.com') # Se carga la url junto con la variable "driver" asignada
        x = input(colorama.Fore.RED + "Presiona enter después que te hayas conectado con el codigo QR")
        try:
            msj = input(colorama.Fore.BLUE + "Escribe el mensaje que quieras enviar: \n")
            receptor = input(colorama.Fore.BLUE + "¿A quien le quieres enviar el mensaje?: \n")
            veces = int(input(colorama.Fore.BLUE + "Ingresa el número de veces que le vas a enviar el mensaje: \n"))

            usuario = driver.find_element_by_xpath('//span[@title = "{}"]'.format(receptor)) # Encuentra el receptor via Xpath (identificado en la variable "receptor"
            usuario.click() #Le hace click al receptor
            sleep(2)
            click = driver.find_element_by_xpath(
                "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]") # Hace click a la caja de mensaje del receptor
            for i in range(veces): # Itera en X tiempo (definido en variable "veces" y envia el mensaje para luego presionar Enter
                click.click()
                click.send_keys(msj)
                click.send_keys(Keys.ENTER)
        except: #Si algo falla o el usuario es erróneo, lo vuelve a empezar 
            print(colorama.Fore.RED + "Nada encontrado, reinicia el script!")
        cool = input(colorama.Fore.GREEN + "¿Quieres seguir spameando? S/N:\n")
        if cool == "S":
            pass
        else:
            print(colorama.Fore.CYAN + "Adiós ;)")
            break


if __name__ == "__main__": 
    banner1()
    main()
