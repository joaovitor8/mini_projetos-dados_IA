from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get()


botao_login = navegador.find_element("id", "")
botao_login.click()

navegador.find_element("id", "").send_keys("")
navegador.find_element("id", "").send_keys("")

botao_logar = navegador.find_element("id", "")
botao_logar.click()

time.sleep(100)
