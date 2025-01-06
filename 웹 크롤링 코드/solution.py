import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 웹 드라이버 설정
options = Options()
#options.add_argument("--headless")  # 창을 띄우지 않고 실행
options.add_argument("--ignore-certificate-errors")  # SSL 인증서 오류 무시
options.add_argument("--incognito")  # 시크릿 모드로 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 웹사이트 접속
url = "https://www.bottegaveneta.com/ko-kr/%EC%97%AC%EC%84%B1/%ED%95%B8%EB%93%9C%EB%B0%B1"
driver.get(url)

# 팝업, 쿠키 허용 창 처리
time.sleep(3)
try:
    # 쿠키 허용 버튼 클릭
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]")
    cookie_button.click()
except:
    pass

# 페이지 끝까지 스크롤하여 모든 상품 로딩
scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 페이지 끝까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
    time.sleep(scroll_pause_time)
    
    # 새로운 높이 얻기
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break
    
    last_height = new_height

# 크롤링할 데이터 저장할 리스트
products = []

# 상품 리스트의 각 상품 정보 크롤링
product_elements = driver.find_elements(By.CSS_SELECTOR, '.c-product__focus')
print(product_elements)
for product_element in product_elements:
    try:
        # 상품명
        name = product_element.find_elements(By.CSS_SELECTOR, ".c-product__name").text.strip()
        print(name)
    except:
        name = None
    
    try:
        # 가격
        price = product_element.find_elements(By.CSS_SELECTOR, ".c-price__value--current").text.strip()
        print(price)
    except:
        price = None
    
    try:
        # 상품 링크 URL
        product_link = product_element.find_elements(By.CSS_SELECTOR, ".c-product__link.c-product_focus").get_attribute("href")
        print(product_link)
    except:
        product_link = None
    
    try:
        # 이미지 URL
        image_url = product_element.find_elements(By.CSS_SELECTOR, ".c-product__image.lazyloaded").get_attribute("src")
        print(image_url)
    except:
        image_url = None
    
    products.append([name, price, product_link, image_url])

# 크롤링한 데이터를 pandas DataFrame으로 저장
df = pd.DataFrame(products, columns=['상품명', '가격', '상품 링크 URL', '이미지 URL'])

# 엑셀 파일로 저장
df.to_excel('bottegaveneta_products.xlsx', index=False)

# 드라이버 종료
driver.quit()

print("크롤링이 완료되었습니다. 'bottegaveneta_products.xlsx' 파일을 확인하세요.")
