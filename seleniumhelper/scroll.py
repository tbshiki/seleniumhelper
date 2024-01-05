from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


def scroll_to_xpath(driver, element_xpath, time_sleep=1):
    """
    Scrolls the browser window to the element specified by the XPath.

    Args:
        driver: The WebDriver instance controlling the browser.
        element_xpath: The XPath of the element to scroll to.
        time_sleep: Optional; Time to wait after scrolling to the element.

    """
    scroll_point = driver.find_element(By.XPATH, element_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(scroll_point).perform()

    # Optional: Wait for a certain time after scrolling
    WebDriverWait(driver, time_sleep).until(lambda d: scroll_point.is_displayed())


def scroll_to_element_by_js(driver, element, top_offset=100):
    """
    Scrolls to the specified web element, ensuring it's positioned at a specified offset from the top.

    Args:
        driver: The WebDriver instance controlling the browser.
        element: The web element to scroll to.
        top_offset: The vertical offset from the top of the page to position the element at.
                   Defaults to 100 pixels.
    """
    y_position = element.location["y"]
    scroll_position = max(0, y_position - top_offset)  # Ensure the scroll position is not negative

    driver.execute_script(f"window.scrollTo(0, {scroll_position});")
