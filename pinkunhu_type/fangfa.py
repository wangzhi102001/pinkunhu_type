
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,TimeoutException,StaleElementReferenceException

def retryingFindClick(by,driver):
    result = False
    attempts = 0
    while attempts < 2:
        try:
            driver.find_element_by_xpath(by).click()
            result = True
            break
        except StaleElementReferenceException as e :
            pass
        attempts+=1
        return result

