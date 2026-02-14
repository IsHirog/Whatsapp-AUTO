from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome() 
driver.get("https://web.whatsapp.com")
input("Faça o login e pressione Enter ")

numeros = [
            "5582999999999",
            "5582999999999",
            "5582999999999",
            "5582999999999"
            # Adicione mais números aqui no formato "55 DDD XXXXxXXXX, como os acima"
            ]


mensagem = "Digite sua mensagem aqui"
# Adicione a mensagem que deseja enviar acima

for numero in numeros:
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(url)
    time.sleep(2.5)
    
    # Localiza o campo de texto e dá Enter
    campo = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    campo.send_keys(Keys.ENTER)
    time.sleep(1)

driver.quit()