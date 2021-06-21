from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def show_more_results(driver_obj):
    if driver_obj.findElements(
            By.id("uitk-button uitk-button-medium uitk-button-has-text uitk-button-secondary")).size() > 0:
        driver_obj.find_element_by_class_name(
            'uitk-button uitk-button-medium uitk-button-has-text uitk-button-secondary').click()


def get_paginations(website_url):
    chrome_driver_path = r"drivers/chromedriver.exe"
    driver_obj = webdriver.Chrome(chrome_driver_path)
    driver_obj.get((website_url))
    driver_obj.maximize_window()
    go_ahead = True

    pages = list()
    hotels_list = list()

    while go_ahead:
        time.sleep(2)
        try:
            next_button_wrapper = driver_obj.find_element_by_xpath('//div[contains(@class, "kK2YDd")]')
            next_button = next_button_wrapper.find_element_by_xpath(
                "//span[contains(@class,'RveJvd snByac') and contains(text(), 'Next')]")
            # ActionChains(driver_obj).click(next_button)
            next_button.click()
            go_ahead = True
            pages.append(driver_obj.current_url)
            google_list_wrapper = driver_obj.find_element_by_xpath(
                "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[1]/div[2]/main/div/div[2]/c-wiz")

            hotel_list = google_list_wrapper.find_elements_by_class_name('f1dFQe')

            print(f"page {len(pages)}, {len(hotel_list)} results found")

            for id, hotel in enumerate(hotel_list):
                try:
                    hotel_name = hotel.find_element_by_xpath(
                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[1]/div[2]/main/div/div[2]/c-wiz/div[6]/c-wiz[' + str(
                            id + 1) + ']/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2')
                    hotel_stars = None
                    # hotel_stars = hotel.find_element_by_xpath(
                    #     '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/div[1]/div[2]/main/div/div[2]/c-wiz/div[6]/c-wiz[' + str(
                    #         id + 1) + ']/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/span[2]')
                    show_more = hotel.find_element_by_tag_name("a").get_attribute('href')
                    # hotels_list.append(hotel_name.text)
                    # print(f"{id + 1} => hotel_data: {hotel_name.text}")
                    print(f"\n{id + 1} => hotel_data: {hotel_name.text}, {hotel_stars}, {show_more}")
                except Exception as e:
                    # print(e)
                    print(f"Failed to extract data")
        except Exception as e:
            print(f"No Show more results \n{e}")
            go_ahead = False

    print(f"{len(pages)} pages found")

    # for page in pages:
    #     find_hotels(page)


def print_hotel(id, name, stars, url):
    print(f"\n{id + 1} => hotel_data: {name}, {stars}, {url}")


def find_hotels(website_url):
    go_ahead = True
    chrome_driver_path = r"drivers/chromedriver.exe"
    driver_obj = webdriver.Chrome(chrome_driver_path)
    driver_obj.get((website_url))
    driver_obj.maximize_window()

    print(f"Finding hotels in {driver_obj.current_url}")
    # while go_ahead:
    google_list_wrapper = driver_obj.find_element_by_xpath(
        "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[1]/div[2]/main/div/div[2]/c-wiz")

    hotel_list = google_list_wrapper.find_elements_by_class_name('f1dFQe')

    print(f"{len(hotel_list)} results found")

    for id, hotel in enumerate(hotel_list):
        try:
            hotel_data = hotel.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[1]/div[2]/main/div/div[2]/c-wiz/div[6]/c-wiz[' + str(
                    id + 1) + ']/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2')
            print(f"{id + 1} => hotel_data: {hotel_data.text}")
        except Exception as e:
            # print(e)
            print(f"Failed to extract data")

    driver_obj.close()

    # while go_ahead:
    #     try:
    #         # driver_obj.find_element_by_xpath('//*[@id="app-layer-base"]/div/main/div/div/div/section/div[2]/section[3]/button').click()
    #         driver_obj.find_element_by_css_selector(
    #             "button[data-stid='show-more-results']").location_once_scrolled_into_view
    #         driver_obj.find_element_by_css_selector("button[data-stid='show-more-results']").click()
    #         go_ahead = True
    #     except Exception as e:
    #         print(f"No Show more results \n{e}")
    #         go_ahead = False
    #
    # hotel_list_wrapper = driver_obj.find_element_by_xpath("//ol[@class='results-list no-bullet']")
    # hotel_list = hotel_list_wrapper.find_elements_by_class_name("listing")
    #
    # print(f"{len(hotel_list)} results found")
    #
    # for id, hotel in enumerate(hotel_list):
    #     try:
    #         name = hotel.find_element_by_class_name("truncate-lines-2")
    #         stars = hotel.find_element_by_class_name("uitk-type-300")
    #         price = hotel.find_element_by_class_name("loyalty-display-price")
    #         print(f"[{id + 1}]hotel: {name.text}\n\tstars: {stars.text}\n\tprice: {price.text}")
    #         # print(f"[{id}]\t hotel: {hotel.text}")
    #     except Exception as e:
    #         print(e)
    #         print(f"Failed to extract data")


if __name__ == "__main__":
    get_paginations(
        "https://www.google.com/travel/hotels?utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAAaUAoyEi4yJTB4ODhkOWIwYTIwZWM4YzExMToweGZmOTZmMjcxZGRhZDRmNjU6BU1pYW1pGgASGhIUCgcI5Q8QBhgeEgcI5Q8QBxgBGAEyAhAAKgsKBygBOgNVU0QaAA&rp=OAFIAg&destination=Miami&ap=MAFa7QIKBgjg1AMQACIDTEtSKhYKBwjlDxAGGB4SBwjlDxAHGAEYASgAsAEAWAFoAXIECAIYAJoBLhIFTWlhbWkaJTB4ODhkOWIwYTIwZWM4YzExMToweGZmOTZmMjcxZGRhZDRmNjWiAREKCC9tLzBmMnYwEgVNaWFtaaoBDgoCCCESAggvEgIIWhgBqgEKCgIIEhICCGkYAaoBDgoCCBQSAghwEgIIGxgBqgEHCgMInAEYAKoBBwoDCKECGACqAR4KAggcEgIIBxICCFESAghzEgIIRxICCDYSAghNGAGqARIKAgglEgIIdxICCHgSAgh6GAGqARYKAggREgIIQBICCFcSAggCEgIIfxgBqgFBCgIILhIDCIABEgIIPBICCDsSAghWEgIIOhIDCIcBEgIIGhICCD0SAghLEgIIAxICCAwSAghTEgIIKBIDCIkBGAGqAQsKAwjhAhICCGMYAaoBCgoCCDUSAggQGAGSAQIgAWgA&ved=0CAAQ5JsGahcKEwjg-JbPv6bxAhUAAAAAHQAAAAAQAg")
