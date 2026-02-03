from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def get_reviews(product_url, max_reviews=20):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(product_url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    reviews = []

    review_divs = soup.find_all("span", {"data-hook": "review-body"})

    for div in review_divs[:max_reviews]:
        text = div.get_text(strip=True)
        reviews.append({"text": text})

    return reviews


# TEST BLOCK — DO NOT REMOVE
if __name__ == "__main__":
    url = "https://www.amazon.in/product-reviews/B0CHX7HK9Y"
    data = get_reviews(url)
    print(data)
