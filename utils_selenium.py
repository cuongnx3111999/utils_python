from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import  time

def init_driver(headless=False):
    options = Options()
    options.headless = headless
    # # ko hien image
    # # prefs = {"profile.managed_default_content_settings.images": 2}
    # # options.add_experimental_option('prefs',prefs)
    #
    # options.add_argument("--user-data-dir={}".format('C:\\Users\\cucun\\AppData\\Local\\Google\\Chrome\\User Data'))
    #
    # options.add_argument('--profile-directory=project1')
    # options.add_argument("--user-data-dir={}".format('C:\\Users\\cucun\\AppData\\Local\\Google\\Chrome\\User Data'))
    # options.add_argument('--profile-directory=khach')
    driver = webdriver.Chrome(executable_path="F:\\chromedriver",options=options)
    return driver

def check_curent_ip(driver):
    driver.get('https://api6.ipify.org?format=json')
    text=driver.find_element(By.CSS_SELECTOR,'body').text
    # print(text)
    return text

def wait_element_can_click(driver,css_element):
    return WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_element)))

    def upload_file(self, driver, file_path):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(file_path)


def login(self, driver, url, css_user, user, css_pass, password, css_submit):
    driver.get(url)
    time.sleep(5)

    # wait until element located
    self.wait_element_can_located(driver, css_user)
    print('css_user', css_user)
    print('user', user)

    driver.find_element_by_css_selector(css_user).send_keys(user)
    time.sleep(1)
    driver.find_element_by_css_selector(css_pass).send_keys(password)
    time.sleep(1)
    driver.find_element_by_css_selector(css_submit).click()
    time.sleep(10)

    list_err = driver.find_elements_by_css_selector('#login_error')
    print(len(list_err))

    if len(list_err):
        driver.find_element_by_css_selector(css_user).send_keys(user)
        time.sleep(1)
        driver.find_element_by_css_selector(css_pass).send_keys(password)
        time.sleep(1)
        driver.find_element_by_css_selector(css_submit).click()
        time.sleep(10)


def post_anhAll_wp(self, driver, url, list_image_locals):
    driver.get(url)
    time.sleep(5)
    dem = 0
    for filePath in list_image_locals:
        try:
            time.sleep(2)
            file_ip = WebDriverWait(driver, 10).until(
                ec.invisibility_of_element_located((By.CSS_SELECTOR, "input[type=file]")))
            file_ip.send_keys(filePath)
            dem += 1
        except:
            print("err")

    # wait until all upload success
    eles = driver.find_elements_by_css_selector('.edit-attachment')
    demtimeout = 0
    timeout = 60
    while (len(eles) < dem):
        print('len(eles)', len(eles))
        eles = driver.find_elements_by_css_selector('.edit-attachment')
        time.sleep(2)

        demtimeout += 1
        if demtimeout > timeout:
            break

    print('dem', dem)
    time.sleep(10)
    print("upload done")


def get_list_link_after_upload_all_wp(self, driver1):
    list_link_image = driver1.find_elements_by_css_selector('.pinkynail')
    list_link_image = [link_image.get_attribute('src') for link_image in list_link_image]
    list_link_image = [self.remove_ext(link_image) for link_image in list_link_image]

    list_file_name = driver1.find_elements_by_css_selector('.title')
    list_file_name = [file_name.text for file_name in list_file_name]

    return list_link_image, list_file_name


def post_bai(self, driver, url, title, ndung, description='', id_wp=''):
    driver.get(url)
    time.sleep(0.5)
    driver.get(url)
    time.sleep(5)

    html_btn = self.wait_element_can_click(driver, '#content-html')
    html_btn.click()

    ndung = ndung.replace("'", '')
    try:
        driver.execute_script("document.querySelector('#content').value=`" + ndung + "`")
    except:
        return 'err_post'

    title_input = self.wait_element_can_located(driver, '#title')
    title_input.send_keys(title)

    if description:
        driver.find_element_by_css_selector('[name="aiosp_description"]').send_keys(description)
    if id_wp:
        js = "document.querySelector('#category-" + '%s' % id_wp + " label').click()"
        driver.execute_script(js)

    driver.find_element_by_css_selector('#set-post-thumbnail.thickbox').click()
    # chuyen tab chon anh
    # menu_item_browse = self.wait_element_can_click(driver, '#menu-item-browse')
    # menu_item_browse.click()

    thumbnail_btn = self.wait_element_can_click(driver, '.thumbnail')
    thumbnail_btn.click()

    set_thumnail_btn = self.wait_element_can_click(driver, '.search-form button')
    set_thumnail_btn.click()

    # public_btn = self.wait_element_can_click(driver, '#publish')
    # public_btn.click()
    time.sleep(10)
    driver.execute_script("document.querySelector('#publish').click()")

    link_post = self.wait_element_can_located(driver, '#sample-permalink a')
    link_post = link_post.get_attribute('href')
    time.sleep(5)
    return link_post
if __name__=='__main__':
    driver=init_driver()
    driver.get('https://selenium-python.readthedocs.io/waits.html')
    print(check_curent_ip(driver))



