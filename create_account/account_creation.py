import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="..//create_account//chromedriver.exe")


class LoginJabatalks:
    """
    Creating an account
    """

    # parameterized constructor with valid inputs as a parameter
    def __init__(self, username, organisation_name, email):
        self.username = username
        self.organisation_name = organisation_name
        self.email = email

    #  creating an account and verifing the languages
    def loginPage(self):
        driver.implicitly_wait(30)
        driver.maximize_window()

        # opening the URL
        driver.get("http://jt-dev.azurewebsites.net/#/SignUp")

        # verifing the languages present in the login page using assertion
        languages = driver.find_elements(By.XPATH, "//div[@id='language']//li//a/div")
        l = []
        for language in languages:
            l.append(language.text)
        assert 'English', 'Dutch' in l
        print("VERIFICATION OF LANGUAGES IS SUCCESSFULLY VERIFIED ")

        # login with valid credential and email should not be registered with jabatalks
        driver.find_element(By.ID, "name").send_keys(
            self.username + Keys.TAB + self.organisation_name + Keys.TAB + self.email)
        driver.find_element(By.XPATH,"//span[@class='black-color ng-binding']").click()
        driver.find_element(By.XPATH, "//button[text()='Get Started' and @type='submit']").click()
        print("LOGIN SUCCESSFULLY")
        time.sleep(3)

        # Verifing email confirmation message
        assert driver.find_element_by_xpath(
            "//span[text()=' A welcome email has been sent. Please check your email. ']").is_displayed()
        print("EMail AS BEEN SENT SUCCESSFULLY")

    def login_gmail(self):
        driver.execute_script("window.open('https://www.gmail.com/', 'tab2');")
        driver.switch_to.window("tab2")
        driver.find_element_by_id("identifierId").send_keys(username + Keys.ENTER)

        driver.quit()


print("***********ACCOUNT CREATION FOR JABATALKS*********")
print("Please enter a details...")
username = input("Enter name    : ")
organisation_name = input("Enter organisation name  :  ")
print("#### ENTER THE VALID GMAIL ACCOUNT AND IT SHOULD NOT BE REGISTERED BEFORE WITH JABATALKS ######")
print("### IF U HAVE ALREADY AN ACCOUNT THEN PLEASE LOGIN WITH VALID CREDENTIALS ###")
# SUBMIT BUTTON WILL BE DISABLED IF THE EMAIL IS ALREADY REGISTERED/
email = input("Enter email  : ")

o = LoginJabatalks(username, organisation_name, email)
o.loginPage()
