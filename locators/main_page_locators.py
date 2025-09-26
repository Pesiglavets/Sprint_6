from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

class FAQPageLocators:
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__button']")
    FAQ_ANSWERS = (By.XPATH, "//div[@class='accordion__panel']")