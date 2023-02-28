from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import platform
import time
import os
import sys

# コントロール押しながらクリック
# browser_operation.click_C(driver, element)
class clickC:
    def __init__(self, driver, element):

        # クリック前のハンドル数を取得
        handles = len(driver.window_handles)

        # 要素がウインドウ外だとエラーになるのでスクロールしておく
        driver.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(driver)
        time.sleep(1)

        if platform.system() == "Darwin":
            # Macなのでコマンドキー
            actions.key_down(Keys.COMMAND)

        else:
            # Mac以外なのでコントロールキー
            actions.key_down(Keys.CONTROL)

        actions.click(element)
        time.sleep(1)
        actions.perform()
        time.sleep(1)

        try:
            # 新しいタブが開くのを最大30秒まで待機
            WebDriverWait(driver, 30).until(lambda a: len(a.window_handles) > handles)
        except TimeoutException:
            print("新しいタブが開かずタイムアウトしました")
            sys.exit(1)

        time.sleep(1)

    # コントロール押しながらクリックして一番右のタブに移動
    def rightmost(driver, element):
        clickC(driver, element)
        driver.switch_to.window(driver.window_handles[-1])

    def switchnew(driver, element):
        handle_list_befor = driver.window_handles

        clickC(driver, element)
        time.sleep(1)

        handle_list_after = driver.window_handles
        handle_list_new = list(set(handle_list_after) - set(handle_list_befor))
        driver.switch_to.window(handle_list_new[0])
        time.sleep(1)


def chrome_scrolle(driver, scrolle_xpath, seconds=1):
    scrolle_point = driver.find_element(By.XPATH, scrolle_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(scrolle_point)
    actions.perform()
    time.sleep(seconds)


# 指定したフォルダの最新のファイルパスを取得する
# ダウンロード直後の最新ファイルを取得して待機したいときは before_path を必ず指定すること
# ダウンロード待機参考:https://note.com/kohaku935/n/n87903c010d28
def get_latest_file_path(path, timeout_second=30, before_path=None):

    file_path = ""

    # 指定秒待機して最新ファイルが.crdownload.tmpでないことを確認
    for i in range(timeout_second + 1):
        # 指定時間待っても 最新ファイルが確認できない場合 エラーを返す
        if i >= timeout_second:
            raise Exception("Csv file cannnot be finished downloading!")

        time.sleep(1)  # wait 1sec

        if len(os.listdir(path)) != 0:  # if there are files in the folder
            file_path = max([os.path.join(path, f) for f in os.listdir(path)], key=os.path.getctime)  # get the latest flilepath
        else:
            file_path = ""  # there are no files in the folder

        if ".crdownload" in file_path or ".tmp" in file_path:  # .crdownload or .tmp are downloading ,so go back to loop and wait rerun
            continue
        else:
            if before_path == None:  # before_pathが未入力なので直前にダウンロードが無いパターン 最新ファイルを取りたいだけ
                return file_path

            elif before_path == file_path:  # ファイルパスが変わっていないので戻って待機
                continue

            else:  # ファイルパスが変わっているので、ダウンロードがあるパターン
                file_path = max([os.path.join(path, f) for f in os.listdir(path)], key=os.path.getctime)  # retrieve get the latest flilepath
                return file_path

    return file_path


# カレントハンドル以外のハンドル(タブ)を閉じてカレントハンドルに戻す
def close_other_current_handle(driver, current_handle):
    handles_array = driver.window_handles
    for handle_ in handles_array:
        if handle_ != current_handle:
            driver.switch_to.window(handle_)
            driver.close()
            time.sleep(1)

    driver.switch_to.window(current_handle)
    time.sleep(1)


def set_location(driver: object, ele: object, y_location: int = 100):
    """ Set location of element scroll to top of element

    Args:
        driver (object): chromedriver
        ele (object): element
    """

    if ele.location["y"] > y_location:
        driver.execute_script("window.scrollTo(0, " + str(ele.location["y"] - y_location) + ");")
    else:
        driver.execute_script("window.scrollTo(0, 0);")
