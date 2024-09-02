from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import itertools

def install_dependencies():
    os.system('pip install requests beautifulsoup4 selenium pandas')

install_dependencies()

proxies = [
    "67.213.212.36:12107"
]

proxy_pool = itertools.cycle(proxies)

def create_driver_with_proxy(proxy):
    chrome_options = Options()
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    # chrome_options.add_argument("--headless")  # Run in headless mode for performance

    # Path to ChromeDriver
    service = Service('/opt/homebrew/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Get the next proxy
proxy = next(proxy_pool)
print(f"Using proxy: {proxy}")

driver = create_driver_with_proxy(proxy)

url = 'https://www.jalan.net/100000/LRG_100800/?stayYear=2025&stayMonth=3&stayDay=5&stayCount=9&roomCount=10&adultNum=2&ypFlg=1&kenCd=100000&screenId=UWW1380&roomCrack=200000,200000,200000,200000,200000,200000,200000,200000,200000,200000&lrgCd=100800&distCd=01&rootCd=04'
driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".p-searchResultItem__summary"))
    )
except Exception as e:
    print("Timed out waiting for page to load")

hotels = driver.find_elements(By.CSS_SELECTOR, ".p-yadoCassette__row")
data = []

for hotel in hotels:
    try:
        name = hotel.find_element(By.CSS_SELECTOR, ".p-searchResultItem__facilityName").text
        price = hotel.find_element(By.CSS_SELECTOR, ".p-searchResultItem__lowestPriceValue").text
        description = hotel.find_element(By.CSS_SELECTOR, ".p-searchResultItem__description").text

        data.append({
            "Name": name,
            "Price": price,
            "Description": description
        })
    except Exception as e:
        print(f"Error extracting data: {e}")

driver.quit()

df = pd.DataFrame(data)
df.to_csv('hotel_prices.csv', index=False)

report = df.describe()
report.to_csv('summary_report.csv')

print("Scraping completed and files generated.")
