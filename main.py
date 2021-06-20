from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\\Bibs\\chromedriver.exe")

def enviarMensagem(contato, msg, count):
    driver.get("https://web.whatsapp.com")
    print("Scaneie o QR Code.")
    wait = WebDriverWait(driver, 20)

    el_contato = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{contato}"]')))
    if el_contato is None:
        print("Contato não encontrado")
        driver.quit()
        quit()
    else:
        el_contato.click()
        print("Usuário encontrado")

    time.sleep(2)

    for i in range(count):
        try:
            el_click_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]'))) 
            el_click_input.click()
            el_click_input.send_keys(msg)
            print("Mensagem digitada")
        except:
            print("Falha ao encontrar o campo de input")
            driver.quit()
            quit()

        # time.sleep(1)

        try:
            el_send = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button/span')))
            el_send.click()
            print("Mensagem enviada")            
        except:
            print("Falha ao encontrar o campo de input")
            driver.quit()
            quit()

        # time.sleep(1)

    driver.quit()
    quit()

def criarGrupos(contatos, group_name):        
    # Iniciar criação do grupo
    try:
        el_opt = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/div/span')))
        el_opt.click()
        print("Click em Opções")            
    except:
        print("Falha ao encontrar o campo de opções")
        driver.quit()
        quit()

    time.sleep(1)

    try:
        el_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[1]/div[1]')))
        el_create.click()
        print("Click em Criar grupo")            
    except:
        print("Falha ao encontrar o campo de criar grupo")
        driver.quit()
        quit()

    time.sleep(1)

    try:
        el_con = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/div/input')))
        el_con.click()

        for contato in contatos: 
            el_con.send_keys(contato)
            time.sleep(1)
            el_con.send_keys(Keys.RETURN)        

        print("Adicionando contatos")            
    except:
        print("Falha ao adicionar contatos")
        driver.quit()
        quit()

    time.sleep(1)    

    try:
        el_complete = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/span/div/span')))
        el_complete.click()
        print("Click em criar")            
    except:
        print("Falha ao encontrar o campo de criar")
        driver.quit()
        quit()

    time.sleep(1)

    try:
        el_nome = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div/div[2]')))
        el_nome.click()
        el_nome.send_keys(group_name)
        time.sleep(0.5)
        el_nome.send_keys(Keys.RETURN)
        print("Click em nome grupo")            
    except:
        print("Falha ao encontrar o campo de nome do grupo")
        driver.quit()
        quit()

    time.sleep(1)


if __name__ == "__main__":
    # f = open("travazap", "r", encoding="utf8")

    # nome_contato = "Gustavo Voz"
    # # mensagem = "Spam"
    # mensagem = f.read()
    
    # enviarMensagem(nome_contato, mensagem, 20)
    contatos = ('randerson', 'reneclei', 'gestor')
    offset = 6    
    
    driver.get("https://web.whatsapp.com")
    print("Scaneie o QR Code.")
    wait = WebDriverWait(driver, 20)

    time.sleep(2)
    for i in range(8):
        numero_grupo = offset + i
        nome_grupo = f'INTENSIVO DE APH #00{numero_grupo}'
        criarGrupos(contatos, nome_grupo)

    driver.quit()