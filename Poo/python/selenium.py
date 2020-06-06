from selenium import webdriver
from time import sleep

class UsingUnnittest(unittest.Testcase):

    def setUp(self):
        self.driver = webdriver.chromedriver(executable_path = '.\Users\user\Documents\GitHub\JavaScript\Poo\python\chromedriver')
        driver = self.driver
        
    def test_get_ptyhon_website(self):
        driver = self.driver
        driver.get("https://www.python.org")
        
    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()
  
if __name__ == '__main__':
  unittest.main(verbosity = 2)