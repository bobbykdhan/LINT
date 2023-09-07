

import time
import json
import random
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from driver_handler import create_driver
from login import *

@dataclass
class ReportInfo:
    building: str
    machineNumber: str
    problemDetail: str

def main():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=3000,3000")
    options.headless = False  # Set this to True if you want a headless browser
    driver = webdriver.Chrome(options=options)
    return driver


def api_request(machine_report: ReportInfo):
    driver = create_driver()
    try:
        make_request(driver, machine_report)
    except Exception as exc:
        print("An Error Has Occurred")
        print(exc)
        driver.quit()


def make_request(driver, machine_report: ReportInfo):
    driver.get("https://mylife.rit.edu")
    wait = WebDriverWait(driver, 150, poll_frequency=1)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "ui-btn-external-provider")))
    sign_in_button = driver.find_element(By.CLASS_NAME, "ui-btn-external-provider")
    sign_in_button.click()
    time.sleep(2)
    sign_in(driver, True)
    input("make whoever do duo")
    # driver.get("https://mylife.rit.edu/StarRezPortalX/A74DA9CE/28/406/Maintenance-Maintenance?HadEmptyContext=True")
    # Not 100 percent sure that this link will always work so we might need to get the actual button
    driver.get(
    "https://mylife.rit.edu/StarRezPortalX/338C2D63/28/407/Maintenance-Maintenance_Job_Deta?UrlToken=342BAFB1&RoomSpaceMaintenanceID=-1")

    wait.until(ec.visibility_of_element_located((By.NAME, "RoomSpaceMaintenanceCategoryID")))
    category_select = Select(driver.find_element(By.NAME, "RoomSpaceMaintenanceCategoryID"))
    item_select = Select(driver.find_element(By.NAME, "RoomSpaceMaintenanceItemID"))
    description = driver.find_element(By.NAME, "Description")

    category_select.select_by_visible_text("LAUNDRY ROOM")
    time.sleep(1)
    item_select.select_by_visible_text("washer")

    description.send_keys(machine_report.building + " Laundry, Machine" + machine_report.machineNumber + ": " + machine_report.problemDetail)
    time.sleep(5)
    description.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    driver = main()
    # make_request(driver, "Gleason", "35-A079", "Washer", "17", "It seems that this machine is not receiving power")
