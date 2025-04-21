import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil
import time
import os
import HtmlTestRunner # type: ignore

DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
DOWNLOAD_FILE = os.path.join(DOWNLOAD_DIR, "sampleFile.jpeg")

class DemoQATests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_prefs = {
            "download.default_directory": DOWNLOAD_DIR,
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)

        self.driver = webdriver.Chrome(options=chrome_options)

    def test_form_submission(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.find_element(By.ID, "firstName").send_keys("Brayan")
        self.driver.find_element(By.ID, "lastName").send_keys("Fuentes")
        self.driver.find_element(By.ID, "userEmail").send_keys("brayanfuentes@correo.com")
        self.driver.find_element(By.XPATH, "//label[text()='Male']").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("3123915523")
        time.sleep(1)
        submit_button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(1)
        submit_button.click()
        time.sleep(1)
        title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text
        self.assertIn("Thanks for submitting the form", title)

    def test_file_upload(self):
        self.driver.get("https://demoqa.com/upload-download")
        file_path = os.path.join(os.path.dirname(__file__), "ImagenPrueba.jpg")
        self.driver.find_element(By.ID, "uploadFile").send_keys(file_path)
        uploaded_text = self.driver.find_element(By.ID, "uploadedFilePath").text
        self.assertIn("ImagenPrueba.jpg", uploaded_text)

    def test_file_download(self):
        if os.path.exists(DOWNLOAD_FILE):
            os.remove(DOWNLOAD_FILE)  # Eliminar archivo si ya existe

        self.driver.get("https://demoqa.com/upload-download")
        self.driver.find_element(By.ID, "downloadButton").click()
        time.sleep(5)  # Esperar a que se descargue el archivo

        self.assertTrue(os.path.exists(DOWNLOAD_FILE), "El archivo no se descargo.")
        print("Descarga exitosa.")

    def test_alerts(self):
        self.driver.get("https://demoqa.com/alerts")

        # 1. Alerta simple
        self.driver.find_element(By.ID, "alertButton").click()
        self.driver.switch_to.alert.accept()

        # 2. Confirm alert - ocultar anuncio antes
        try:
            self.driver.execute_script("""
                const iframe = document.querySelector("iframe[id^='google_ads_iframe']");
                if (iframe) {
                    iframe.style.display = 'none';
                }
            """)
            time.sleep(1)
        except Exception as e:
            print("No se encontro anuncio:", e)

        self.driver.find_element(By.ID, "confirmButton").click()
        self.driver.switch_to.alert.accept()
        result = self.driver.find_element(By.ID, "confirmResult").text
        self.assertIn("Ok", result)

        # 3. Prompt alert
        self.driver.find_element(By.ID, "promtButton").click()
        prompt = self.driver.switch_to.alert
        prompt.send_keys("Prueba de alerta")
        prompt.accept()
        prompt_result = self.driver.find_element(By.ID, "promptResult").text
        self.assertIn("Prueba de alerta", prompt_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reportes_html"))

    
