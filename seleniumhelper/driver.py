from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import platform
import time


class ClickControl:
    """
    Control-click action on a web element, handling new tabs and window switches.
    """

    def __init__(self, driver, element):
        """
        Initializes the ClickControl instance.
        Args:
            driver: WebDriver instance.
            element: The web element to be clicked.
        """
        self._perform_click(driver, element)

    def _perform_click(self, driver, element):
        """
        Perform a control-click on the specified element and wait for a new tab to open.

        This method scrolls the element into view, performs a control-click (Command-click on macOS,
        Control-click on other systems), and waits for a new browser tab to open.

        Args:
            driver: The WebDriver instance controlling the browser.
            element: The web element to be clicked.

        Raises:
            TimeoutException: If no new tab is opened within 30 seconds.
        """

        handles_before_click = len(driver.window_handles)  # Get the number of handles before the click

        driver.execute_script("arguments[0].scrollIntoView();", element)  # Scroll the element into view to avoid errors

        # Setup action chains for the click
        actions = ActionChains(driver)
        control_key = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL
        actions.key_down(control_key).click(element).key_up(control_key).perform()

        # Wait for a new tab to open (up to 30 seconds)
        try:
            WebDriverWait(driver, 30).until(lambda d: len(d.window_handles) > handles_before_click)
        except TimeoutException:
            print("Timeout occurred: No new tab was opened.")
            return

    @staticmethod
    def switch_to_rightmost(driver, element):
        """
        Control-clicks on the given element and switches to the rightmost tab.
        Args:
            driver: WebDriver instance.
            element: The web element to be clicked.
        """
        ClickControl(driver, element)
        driver.switch_to.window(driver.window_handles[-1])

    @staticmethod
    def switch_to_new_tab(driver, element):
        """
        Control-clicks on the given element and switches to the newly opened tab.
        Args:
            driver: WebDriver instance.
            element: The web element to be clicked.
        """
        handle_list_before = driver.window_handles
        ClickControl(driver, element)

        handle_list_after = driver.window_handles
        handle_list_new = list(set(handle_list_after) - set(handle_list_before))
        driver.switch_to.window(handle_list_new[0])


def open_new_tab(driver, url, time_sleep=1):
    """
    Opens a new tab with the specified URL and switches the driver's context to this new tab.

    Args:
        driver: The WebDriver instance controlling the browser.
        url: The URL to be opened in the new tab.
        time_sleep: Optional; The time to wait for the new tab to open.

    Returns:
        A list of new window handle(s) created.
    """
    handles_before = driver.window_handles
    driver.execute_script(f"window.open('{url}');")

    # Wait for the new tab to open
    WebDriverWait(driver, time_sleep).until(lambda d: len(d.window_handles) > len(handles_before))

    handles_after = driver.window_handles
    new_handles = list(set(handles_after) - set(handles_before))
    driver.switch_to.window(new_handles[0])

    return new_handles


def close_other_tabs(driver, current_tab_handle):
    """
    Closes all browser tabs except for the current tab and switches back to the current tab.

    Args:
        driver: The WebDriver instance controlling the browser.
        current_tab_handle: The handle of the current tab that should remain open.
    """
    for handle in driver.window_handles:
        if handle != current_tab_handle:
            driver.switch_to.window(handle)
            driver.close()

    driver.switch_to.window(current_tab_handle)
