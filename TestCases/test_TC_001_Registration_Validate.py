from Base import InitiateDriver
from Pages import RegistrationPage
from selenium import webdriver


def test_ValidateRegistration():
    print("inside validate method")
    drv = InitiateDriver.startBrowser()
    print(drv)
    reg = RegistrationPage.registrationclass(drv)
    reg.enter_kwsearch()



#test_ValidateRegistration()


