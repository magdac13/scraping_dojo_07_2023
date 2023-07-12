from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from seleniumwire import webdriver
from dotenv import load_dotenv

import jsonlines
import os


class QuotesToScrape:

    """ This class is used to scrape quotes from the input url and store them in a json file."""

    def __init__(self):
        self.__load_env()
        self.__create_driver()
        self.__timeout = 60
        self.__output = []
        return

    def __create_driver(self):
        self.__driver = webdriver.Chrome()
        return

    # seleniumwire_options = {'proxy': {'https': self.__env['proxy']}}
    def __load_env(self):
        load_dotenv()
        self.__env = {
            # 'proxy': 'http://' + os.getenv('PROXY'),
            'input_url': os.getenv('INPUT_URL'),
            'output_file': os.getenv('OUTPUT_FILE')
        }
        return

    def __scrape_page(self, url):
        self.__driver.get(self.__env['input_url'])

        self.__wait_for_page_to_load()
        return [{
            'text': quote.find_element(By.CLASS_NAME, 'text').text,
            'by': quote.find_element(By.CLASS_NAME, 'author').text,
            'tags': [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')],
        } for quote in self.__driver.find_elements(By.CLASS_NAME, 'quote')]

    def __find_next_page_url(self, base_url):
        self.__driver.get(base_url)
        return self.__driver.find_element(By.CLASS_NAME, 'next').find_element(By.TAG_NAME, 'a').get_attribute('href')

    def __wait_for_page_to_load(self):
        WebDriverWait(self.__driver, self.__timeout).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, 'quote')
        ))
        return

    def scrape_pages(self, base_url=None):
        if base_url is None:
            base_url = self.__env['input_url']

        self.__output.append(self.__scrape_page(base_url))

        try:
            self.scrape_pages(self.__find_next_page_url(base_url))

        except NoSuchElementException:
            self.__driver.quit()

        finally:
            return self

    def save_to_file(self):
        with jsonlines.open(self.__env['output_file'], mode='w') as writer:
            for output_line in self.__output:
                writer.write_all(output_line)
        return


QuotesToScrape().scrape_pages().save_to_file()
