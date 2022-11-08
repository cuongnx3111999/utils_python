from utils_selenium import *
from utils_class import *

driver=init_driver()

driver.get("https://shopee.vn/search?keyword=%C3%A1o")


L_link=driver.find_elements(By.CSS_SELECTOR,"a[data-sqe=\"link\"]")
for link in L_link:
    print(link.get_attribute("href"))


def asd() -> int:

    return "a"
if __name__=="__main__":
    asd()










