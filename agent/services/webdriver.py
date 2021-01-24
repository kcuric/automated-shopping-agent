from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import time
from agent.configuration import configuration

class WebDriverChrome():

  def run(self, url):
    self.driver = webdriver.Chrome()
    self.driver.get(url)

    time.sleep(2)
    
    #pick color
    element = self.driver.find_element(By.XPATH, 
      '/html/body/div[6]/div/div[2]/div/div[2]/div[7]/div/div/ul/li[6]'
    )
    element.click()

    time.sleep(2)

    #buy now
    buy_now_btn = self.driver.find_element(By.XPATH, 
      '/html/body/div[6]/div/div[2]/div/div[2]/div[11]/span[1]/button'
    )
    buy_now_btn.click()

    time.sleep(5)

    try:
      sign_in = self.driver.find_element(By.XPATH, 
        '/html/body/div[12]/div/div[2]/div/ul/li[2]'
      )
      sign_in.click()

      username_field = self.driver.find_element(By.XPATH, 
        '/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/div[1]/input'
      )
      username_field.click()
      username_field.send_keys(configuration.ALIEXPRESS_EMAIL)

      password_field = self.driver.find_element(By.XPATH, 
        '/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/div[2]/input'
      )
      password_field.click()
      password_field.send_keys(configuration.ALIEXPRESS_PASSWORD)

      sign_in_btn = self.driver.find_element(By.XPATH, 
        '/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/button'
      )
      sign_in_btn.click()
    except Exception:
      self.driver.switch_to.window(self.driver.window_handles[1])
      username_field = self.driver.find_element(By.XPATH, 
        '/html/body/div[2]/div/div/div/div/div[1]/input'
      )
      username_field.click()
      username_field.send_keys(configuration.ALIEXPRESS_EMAIL)

      password_field = self.driver.find_element(By.XPATH, 
        '/html/body/div[2]/div/div/div/div/div[2]/input'
      )
      password_field.click()
      password_field.send_keys(configuration.ALIEXPRESS_PASSWORD)

      sign_in_btn = self.driver.find_element(By.XPATH, 
        '/html/body/div[2]/div/div/div/div/button'
      )
      sign_in_btn.click()

      time.sleep(2)
    
      #pick color
      element = self.driver.find_element(By.XPATH, 
        '/html/body/div[6]/div/div[2]/div/div[2]/div[6]/div/div/ul/li[6]'
      )
      element.click()

      time.sleep(2)

      #buy now
      buy_now_btn = self.driver.find_element(By.XPATH, 
        '/html/body/div[6]/div/div[2]/div/div[2]/div[10]/span[1]/button'
      )
      buy_now_btn.click()

    time.sleep(5)
    
    buyer = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[1]'
    )
    delivery_address = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]'
    )
    city = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[4]'
    )


    charge_cost = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[3]/div/div[1]/div[2]'
    )
    shipping = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]'
    )
    total = self.driver.find_element(By.XPATH, 
      '/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[3]/div/div[4]/div[2]'
    )

    buyerName = buyer.get_attribute('innerHTML').split(',')[0].strip()
    buyerContact = buyer.get_attribute('innerHTML').split(',')[1].strip()
    buyerAdress = delivery_address.get_attribute('innerHTML').strip()
    buyerCity = city.get_attribute('innerHTML').split(',')[0].strip()
    buyerState = city.get_attribute('innerHTML').split(',')[2].strip()
    buyerPostCode = city.get_attribute('innerHTML').split(',')[3].strip()
    currency = total.get_attribute('innerHTML').split('$')[0].strip()
    price = charge_cost.get_attribute('innerHTML').split('$')[1].strip()
    shipping = shipping.get_attribute('innerHTML').split('$')[1].strip()
    total = total.get_attribute('innerHTML').split('$')[1].strip()

    transaction = {
      'buyerName': buyerName,
      'buyerContact': buyerContact,
      'buyerAdress': buyerAdress,
      'buyerCity': buyerCity,
      'buyerState': buyerState,
      'buyerPostCode': buyerPostCode,
      'price': price,
      'shipping': shipping,
      'total': total,
      'currency': currency,
      'purchased': True
    }

    self.driver.quit()

    return transaction
