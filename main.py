import paths_helper
import config
from src.util.config import Config
from src.util.browser_helper import BrowserHelper
from src.services.curry_service import CurryService
import time

def main():
    c = Config("curry")
    # c.show()

    browser = BrowserHelper()
    # browser.open_page("https://www.currys.co.uk/products/acer-predator-orion-7000-po7650-gaming-pc-intel-core-i9-rtx-4090-2-tb-hdd-and-1-tb-ssd-10246557.html")
    curry_svc = CurryService(browser, c, None)
    curry_svc.crawl("https://www.currys.co.uk/products/acer-predator-orion-7000-po7650-gaming-pc-intel-core-i9-rtx-4090-2-tb-hdd-and-1-tb-ssd-10246557.html")
    
    time.sleep(10)

if __name__ == '__main__':
    main()

