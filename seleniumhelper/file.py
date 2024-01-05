from selenium import webdriver

import time
import os


def get_latest_file_path(directory, timeout_seconds=30, previous_path=None):
    """
    Finds the latest file in the specified directory, ensuring it's not a temporary download file.

    Args:
        directory: The directory to search in.
        timeout_seconds: The maximum time to wait for a new file to appear.
        previous_path: The path of the previously latest file, if any.

    Returns:
        The path of the latest file, or raises an exception if the timeout is exceeded.

    Raises:
        DownloadTimeoutException: If no new file is found within the timeout period.
    """
    end_time = time.time() + timeout_seconds
    while time.time() < end_time:
        try:
            latest_file = max((os.path.join(directory, f) for f in os.listdir(directory) if not f.endswith((".crdownload", ".tmp"))), key=os.path.getctime, default="")
            if latest_file and (previous_path is None or latest_file != previous_path):
                return latest_file
        except ValueError:
            # Handles the case where max() is given an empty sequence
            pass
        time.sleep(1)

    raise Exception(f"No new file found in {directory} within {timeout_seconds} seconds.")
