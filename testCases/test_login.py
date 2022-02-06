import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("************Test_001_Login***************")
        self.logger.info("************Verifying Home Page Title***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("************Home Page Title Passed***************")
            Path = r"./Screenshots/"+"test_homePageTitle.png"
            print(Path)
            self.driver.save_screenshot(Path)
            self.driver.close()
        else:
            Path = r"./Screenshots/" + "test_homePageTitle.png"
            self.driver.close()
            self.logger.info("************Verifying Login test***************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************Verifying Home Page Title***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************Login Page Title Passed***************")
            self.driver.save_screenshot(r"./Screenshots/"+"test_login.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(r"./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.info("************Login Page Title Failed***************")
            assert False
