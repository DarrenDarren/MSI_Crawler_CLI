
class CurryService:
    
    def __init__(self, browser_helper, config, table):
        self.browser_helper = browser_helper
        self.config = config
        self.table = table
    
    def __preprocess(self):
        preprocess = self.config.preprocess
        
        # deal with the popup coockie
        coockie_btn = self.browser_helper.get_element_with_id("onetrust-accept-btn-handler")
        coockie_btn.click()

        pass

    
    def _can_find_link():
        pass

    def _get_stock_status():
        pass

    def _get_price():
        pass
        
    def crawl(self, url):
        self.browser_helper.open_page(url)
        self.__preprocess()
        pass