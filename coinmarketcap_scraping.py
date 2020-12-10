from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
from csv import writer


def obtain_links():
    browser.get("https://coinmarketcap.com/es/historical/")

    xpath = xpath = "//div[@class='rj2g42-2 kWBnGH row']"
    years = browser.find_elements_by_xpath(xpath)

    xpath = xpath = ".//a[@class='cmc-link']"
    links = [year.find_elements_by_xpath(xpath) for year in years]

    links = [link.get_attribute("href") for s in links for link in s]
    return links


def save_data(url, loadMore=False):
    browser.get(url)
    #  The date can be obtined from the title
    xpath = "//h1[@class='sc-1m8sms1-0 fSRbs cmc-historical-detail__title']"
    title = browser.find_element_by_xpath(xpath).text
    title = title.split("-")
    title = title[1].strip()
    title = title + "\t"
    if loadMore:
        load_more()
    xpath = "//table"
    table = browser.find_element_by_xpath(xpath)

    xpath = "//th"
    headers = table.find_elements_by_xpath(xpath)
    headers = [header.text for header in headers]
    headers = headers[11:-1]  # cleaning the headers
    headers[0] = "Date"

    xpath = "//tr[@class='cmc-table-row']"
    rows = table.find_elements_by_xpath(xpath)
    rows = [title + row.text.replace("\n", "\t") for row in rows]

    for row in rows:
        row = row.split("\t")
        if len(row) == 10:
            row.insert(-3, "")
        for index, item in enumerate(row):
            if index != 0 and index != 2 and index != 3:
                item = item.replace(",", "")
                item = item.replace("$", "")
                item = item.replace("%", "")
                if item.isnumeric():
                    row[index] = float(item)
                elif item.isalpha():
                    row[index] = item
                else:
                    if index == 6:
                        item = item.split(" ")
                        row[index] = float(item[0])
                    else:
                        try:
                            row[index] = float(item)
                        except:
                            row[index] = item
        if "/" in row[2]:
            row[2] = row[2].replace("/", "-")
        try:
            open(
                "./Crypto_history/" + row[2] + ".csv", "x"
            )  # If the file already existis this will give an error
            with open("./Crypto_history/" + row[2] + ".csv", "a", newline="") as f:
                csv_writer = writer(f)
                csv_writer.writerow(headers)
                csv_writer.writerow(row)
        except:
            with open("./Crypto_history/" + row[2] + ".csv", "a", newline="") as f:
                csv_writer = writer(f)
                csv_writer.writerow(row)


def load_more():
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(5)
    button = browser.find_element_by_xpath(
        "//div[@class='cmc-table-listing__loadmore']"
    )

    while True:
        try:
            sleep(5)
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(5)
            button = browser.find_element_by_xpath(
                "//div[@class='cmc-table-listing__loadmore']"
            )
            button.click()
        except:
            break


if __name__ == "__main__":
    firefox_options = Options()
    firefox_options.add_argument("-headless")
    browser = webdriver.Firefox(
        executable_path="./drivers/geckodriver", options=firefox_options
    )
    links = obtain_links()
    for index, link in enumerate(reversed(links)):
        if link:
            try:
                if index % 10 == 0:
                    print(index)
                save_data(link)
            except Exception as e:
                print(e)
                print(link)
                continue
        else:
            break
    browser.close()
