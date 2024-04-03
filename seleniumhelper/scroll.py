from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


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


def scroll_to_target(driver, target, top_offset=100, time_sleep=1):
    """
    Scrolls the browser window to the specified target, which can be a web element or an XPath string.
    Optionally positions the target at a specified offset from the top and waits for a specified time.

    Args:
        driver: The WebDriver instance controlling the browser.
        target: The web element or the XPath string of the element to scroll to.
        top_offset: The vertical offset from the top of the page to position the target at. Defaults to 100 pixels.
        time_sleep: Optional; Time to wait after scrolling to the target. Defaults to 1 second.
    """

    if not target:
        raise ValueError("The 'target' must not be None or empty.")

    try:
        if isinstance(target, WebElement):
            element = target
        else:
            element = driver.find_element(By.XPATH, target)
    except NoSuchElementException:
        print("Element not found.")
        return

    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        WebDriverWait(driver, time_sleep).until(lambda d: element.is_displayed())

    except Exception as e:
        # Element not found, fallback to scroll_to_element_by_js using XPath
        if target:
            scroll_to_element_by_js(driver, element, top_offset)
        else:
            print("Cannot scroll to element")


##
# Anything below this is not recommended : It's a legacy function
##
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
