import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.decolar.com/shop/flights/results/roundtrip/SAO/SSA/2022-12-01/2022-12-02/1/0/0/NA/NA/NA/NA/NA?from=SB&di=1-0')
 
def main():

        golPreco = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="toolbox-tabs-position"]/toolbox-tabs/div/tabs/div/div[2]/tab[1]/div/airlines-matrix/span/div/div/div/div/airlines-matrix-airline[3]/ul/li[2]/span/flights-price/span/flights-price-element/span/span'))
        )   

        latamPreco = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="toolbox-tabs-position"]/toolbox-tabs/div/tabs/div/div[2]/tab[1]/div/airlines-matrix/span/div/div/div/div/airlines-matrix-airline[1]/ul/li[2]/span/flights-price/span/flights-price-element/span/span/em/span[2]'))
        )

        azulPreco = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="toolbox-tabs-position"]/toolbox-tabs/div/tabs/div/div[2]/tab[1]/div/airlines-matrix/span/div/div/div/div/airlines-matrix-airline[2]/ul/li[2]/span/flights-price/span/flights-price-element/span/span/em/span[2]'))
        )
    
        dadosPrecoPassagem = []

        dadosPrecoPassagem.append({
            'gol': golPreco.get_attribute('innerHTML'),
            'latam': latamPreco.get_attribute('innerHTML'),
            'azul': azulPreco.get_attribute('innerHTML')
        })

        print(dadosPrecoPassagem)

driver.close()	
 

if __name__ == '__main__':
    main()