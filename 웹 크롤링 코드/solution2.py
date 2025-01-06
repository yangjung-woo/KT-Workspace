from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import urllib3
import ssl
from datetime import datetime

class SecureBottegaScraper:
    def __init__(self):
        self.url = "https://www.bottegaveneta.com/ko-kr/%EC%97%AC%EC%84%B1/%ED%95%B8%EB%93%9C%EB%B0%B1"
        self.products = []
        
    def setup_driver(self):
        """보안 우회 설정이 포함된 크롬 드라이버 설정"""
        chrome_options = Options()
        
        # SSL 에러 우회 설정
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--allow-insecure-localhost')
        
        # 봇 감지 우회 설정
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--disable-web-security')
        
        # User-Agent 설정
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # 헤드리스 모드 및 기타 설정
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # 성능 최적화 설정
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(30)
        
        return driver
    
    def create_ssl_context(self):
        """SSL 컨텍스트 설정"""
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        return context
    
    def scrape_product(self, product_element):
        """개별 상품 정보 추출"""
        try:
            name = product_element.find_element(By.CSS_SELECTOR, "c-product__link c-product_focus").text
            price = product_element.find_element(By.CSS_SELECTOR, "span.price-sales").text
            product_link = product_element.find_element(By.CSS_SELECTOR, "c-product__link c-product_focus").get_attribute("href")
            image_url = product_element.find_element(By.CSS_SELECTOR, "c-product__image lazyloaded").get_attribute("src")
            
            return {
                "상품명": name,
                "가격": price,
                "상품_링크": product_link,
                "이미지_URL": image_url,
                "수집_시간": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            print(f"상품 정보 추출 중 에러 발생: {str(e)}")
            return None
    
    def scrape_with_retry(self, max_retries=3, delay_between_retries=5):
        """재시도 로직이 포함된 스크래핑 실행"""
        retry_count = 0
        driver = None
        
        while retry_count < max_retries:
            try:
                driver = self.setup_driver()
                print(f"스크래핑 시도 {retry_count + 1}/{max_retries}")
                
                # SSL 컨텍스트 설정
                self.create_ssl_context()
                
                # 페이지 접속
                driver.get(self.url)
                time.sleep(5)  # 초기 로딩 대기
                
                # 상품 리스트 대기 및 추출
                product_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-tile"))
                )
                
                # 상품 정보 수집
                for product in product_elements:
                    product_info = self.scrape_product(product)
                    if product_info:
                        self.products.append(product_info)
                
                print(f"성공적으로 {len(self.products)}개의 상품 정보를 수집했습니다.")
                break
                
            except Exception as e:
                print(f"시도 {retry_count + 1} 실패: {str(e)}")
                retry_count += 1
                if retry_count < max_retries:
                    time.sleep(delay_between_retries)
                
            finally:
                if driver:
                    driver.quit()
        
        return len(self.products) > 0
    
    def save_results(self):
        """수집된 데이터 CSV 저장"""
        if not self.products:
            print("저장할 데이터가 없습니다.")
            return
        
        # CSV 파일명에 타임스탬프 추가
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"bottega_products_{timestamp}.csv"
        
        # DataFrame 생성 및 CSV 저장
        df = pd.DataFrame(self.products)
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        print(f"CSV 파일 저장 완료: {csv_filename}")

def main():
    scraper = SecureBottegaScraper()
    
    print("보테가 베네타 스크래핑 시작...")
    if scraper.scrape_with_retry():
        scraper.save_results()
        print("스크래핑 완료!")
    else:
        print("스크래핑 실패!")

if __name__ == "__main__":
    main()