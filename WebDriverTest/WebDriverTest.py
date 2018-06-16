
from selenium import webdriver
from page_objects import PageObject,PageElement

class Google(PageObject):
    pagina = PageElement(id_='gb')
    search_bar = PageElement(id_='lst-ib')
    button_search = PageElement(name='btnK')
    button_lucky = PageElement(name='btnI')


    def search(self, text):
        self.search_bar.send_keys(text)
        self.pagina.click()
        self.button_search.click()
        #self.button_search.send_keys(Keys.RETURN)

    def search_lucky(self, text):
        self.search_bar.send_keys(text)
        self.pagina.click()
        self.button_lucky.click()


browser = webdriver.Chrome()
g = Google(browser, 'http://www.google.com.br')
g.get('')
g.search_lucky('Universidade Positivo')
