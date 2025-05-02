from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 30)

try:
    driver.get("https://prenotabiblio.sba.unimi.it/portalePlanning/biblio/prenota/calendario/92/25")
    durata_select_elem = wait.until(EC.element_to_be_clickable((By.ID, "durata")))
    Select(durata_select_elem).select_by_visible_text("1 ora")
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", durata_select_elem)

    giorno = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(@aria-label, '5') and contains(@aria-description, 'selezionabile')]")))
    driver.execute_script("arguments[0].click();", giorno)

    prenota = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-cypress='Prenota']")))
    driver.execute_script("arguments[0].click();", prenota)

    fascia = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'disponibile') and starts-with(@aria-label, '09:00')]")))
    driver.execute_script("arguments[0].click();", fascia)

    inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input")))
    dati = [
        "RSSMRA85L10A162L",
        "Mattia Corraini",
        "mattiacorraini65@gmail.com"
    ]
    for i in range(3):
        inputs[i].clear()
        inputs[i].send_keys(dati[i])
        driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", inputs[i])

    avanti = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Avanti')]")))
    driver.execute_script("arguments[0].click();", avanti)

    conferma = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Conferma')]")))
    driver.execute_script("arguments[0].click();", conferma)

    time.sleep(3)
finally:
    driver.quit()
