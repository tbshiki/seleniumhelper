import os
import time


def get_latest_file_path(directory, timeout_seconds=30, previous_path=None):
    """
    Finds the latest file in the specified directory, ensuring it's not a temporary download file.

    Args:
        directory: The directory to search in.
        timeout_seconds: The maximum time to wait for a new file to appear.
        previous_path: The path of the previously latest file, if any.

    Returns:
        The path of the latest file, None if no files exist, or raises an exception if waiting for a new file and the timeout is exceeded.
    """

    def get_latest_file():
        try:
            return max((os.path.join(directory, f) for f in os.listdir(directory) if not f.endswith((".crdownload", ".tmp"))), key=os.path.getctime)
        except ValueError:
            return None

    # If previous_path is not provided, return the current latest file (or None if directory is empty)
    if previous_path is None:
        return get_latest_file()

    # If previous_path is provided, wait for a new file
    end_time = time.time() + timeout_seconds
    while time.time() < end_time:
        latest_file = get_latest_file()
        if latest_file and latest_file != previous_path:
            return latest_file
        time.sleep(1)

    raise Exception(f"No new file found in {directory} within {timeout_seconds} seconds.")


def get_latest_file_after_action(directory, action, timeout_seconds=30):
    """
    Executes a download action and finds the latest file in the specified directory.

    Args:
        directory: The directory to search in.
        action: A function representing the download action to perform.
        timeout_seconds: The maximum time to wait for a new file to appear after the action.

    Returns:
        The path of the latest file, or raises an exception if the timeout is exceeded.
    """
    # Get the current latest file before the action
    latest_file_before_action = get_latest_file_path(directory, timeout_seconds)

    # Perform the download action
    action()

    # Get the latest file after the action
    return get_latest_file_path(directory, timeout_seconds, latest_file_before_action)
