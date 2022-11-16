from utils_selenium import *
from utils_class import *

def create_driver():
    driver = init_driver()
    return driver
def get_links(driver):
    # B1
    driver.get("https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567")
    # B2
    wait_element_can_located(driver=driver,css_element="footer")
    footer = driver.find_element(By.CSS_SELECTOR, "footer")
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    time.sleep(5)
    elems = []
    print(1)
    while len(elems) < 59:
        print(len(elems))
        time.sleep(2)
        elems = driver.find_elements(By.CSS_SELECTOR, "a[data-sqe='link'")
        driver.execute_script("arguments[0].scrollIntoView();", elems[len(elems) - 10])
    links = [elem.get_attribute('href') for elem in elems]
    print(3)

    print(len(links))
    file = File_Interact('links.txt')
    file.write_file_from_list(links)

def save_rating(driver):
    rating_elems = driver.find_elements(By.CSS_SELECTOR, "._280jKz")
    L_rating = [rating.text for rating in rating_elems]
    if L_rating:
        print(L_rating)
        file = File_Interact('rating.txt')
        file.write_file_from_list(L_rating)
        print(1)
        return 1
    else:
        print(0)
        print(L_rating)
        return 0

def get_rating(driver):
    # lay link
    file = File_Interact('links.txt')
    links=file.read_file_list()
    index_link=0
    link=links[index_link]
    print(index_link)
    print(link)
    file = File_Interact('rating.txt')
    driver.get(link)

    # Chon tu 1 sao den 5 sao
    start_click=driver.find_elements(By.CSS_SELECTOR,".product-rating-overview__filter")
    # lay rating
    while (True):
        if(save_rating()==0):
            break
        print("ok")
        time.sleep(2)
        click_button_next = driver.find_element(By.CSS_SELECTOR, ".shopee-icon-button.shopee-icon-button--right ").click()
        time.sleep(2)
    print("Break")

    # for i in range(10):
    #     file = File_Interact('rating.txt')
    #     file.write_file_from_list(["1"])
    #     file.write_file_from_list(links[index_link])
    #     driver.get(links[i])
    #     # lay rating
    #     while(True):
    #         if save_rating():
    #             time.sleep(2)
    #             click_button_next = driver.find_element(By.CSS_SELECTOR, ".shopee-icon-button.shopee-icon-button--right ")
    #             click_button_next.click()
    #         else:
    #             break
if __name__=="__main__":
    driver=create_driver()
    get_links(driver)













