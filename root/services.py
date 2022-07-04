from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Chrome:

    def install_driver(self) -> None:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.options)
    
    def quit(self) -> None:
        self.driver.quit()


@dataclass
class Scrapper:
    browser: Chrome
    url: str
    selections: dict

    def open_page(self)->None:
        self.browser.install_driver()
        self.browser.driver.get(self.url)
    
    def navigate(self) -> None:
        randomness_button_path = self.selections['randomness'].values()
        name_style_button_path = self.selections['name style'].values()
        generate_button_path = self.selections['generate']

        randomness_button_instances = [self.browser.driver.find_element(
            by=By.XPATH, value=btn) for btn in randomness_button_path]
        name_style_button_instances = [self.browser.driver.find_element(
            by=By.XPATH, value=btn) for btn in name_style_button_path]
        generate_button_instance = self.browser.driver.find_element(
            by=By.XPATH, value=generate_button_path)

        [btn.click() for btn in randomness_button_instances]
        [btn.click() for btn in name_style_button_instances]

        generate_button_instance.click()

    
    def scroll_to_element(self, total: int) -> None:
        for i in range(total):
            self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.1)
            try:
                self.browser.driver.find_element(by=By.XPATH, value=f"//*[@id='logos_scroll']/div[2]/div[{total}]")
                return
            except:
                pass

    
    def get_sample_names(self) -> list:
        name_list = []
        total = 200

        wait = WebDriverWait(self.browser.driver, 5)
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='logos_scroll']/div[2]")))    

        self.scroll_to_element(total)
            
        for i in range(1, total):
            element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//*[@id='logos_scroll']/div[2]/div[{i}]/div/div[1]/div")))
            html = element.get_attribute('innerHTML')
            
            if len(html) > 2:
                html = '<div class="name-container">{}</div>'.format(html)
                name_list.append(html)
            else:
                element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="logos_scroll"]/div[2]/div[{i}]/div/div[1]/div[2]')))
                html = '<div class="name-container">{}</div>'.format(element.get_attribute('innerHTML'))
                name_list.append(html)
        
        return name_list




@dataclass
class BusinessNameGenerator:
    url: str
    keywords: str
    selections: dict

    def get_names(self) -> None:
        url = "https://namelix.com/"
        url = "{}app/?keywords={}".format(url, "+".join(self.keywords.split()))

        chrome = Chrome() 
               
        scrapper = Scrapper(chrome, url, self.selections)
        scrapper.open_page()
        scrapper.navigate()
        name_list = scrapper.get_sample_names()
        chrome.driver.quit()
        return name_list

