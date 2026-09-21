# ============================================================
# DAY 35 - WEB SCRAPING USING PYTHON
# 100 Days of Python
# ============================================================

import requests
from bs4 import BeautifulSoup


URL = "https://codegnan.com"


# ============================================================
# PROGRAM 1: SEND GET REQUEST
# ============================================================

def program_1_get_request():
    response = requests.get(URL)

    print(response)


# ============================================================
# PROGRAM 2: CHECK STATUS CODE
# ============================================================

def program_2_status_code():
    response = requests.get(URL)

    print("Status Code:", response.status_code)


# ============================================================
# PROGRAM 3: CHECK WEBSITE ACCESS
# ============================================================

def program_3_check_website():
    response = requests.get(URL)

    if response.status_code == 200:
        print("Website is accessible.")
    else:
        print("Unable to access the website.")


# ============================================================
# PROGRAM 4: PRINT HTML SOURCE
# ============================================================

def program_4_html_source():
    response = requests.get(URL)

    print(response.text[:1000])


# ============================================================
# PROGRAM 5: PRINT RESPONSE HEADERS
# ============================================================

def program_5_headers():
    response = requests.get(URL)

    print(response.headers)


# ============================================================
# PROGRAM 6: PRINT FINAL URL
# ============================================================

def program_6_final_url():
    response = requests.get(URL)

    print("Final URL:", response.url)


# ============================================================
# PROGRAM 7: PRINT COOKIES
# ============================================================

def program_7_cookies():
    response = requests.get(URL)

    print(response.cookies)


# ============================================================
# PROGRAM 8: PRINT ENCODING
# ============================================================

def program_8_encoding():
    response = requests.get(URL)

    print("Encoding:", response.encoding)


# ============================================================
# PROGRAM 9: PRINT RESPONSE TIME
# ============================================================

def program_9_response_time():
    response = requests.get(URL)

    print("Response Time:", response.elapsed)


# ============================================================
# PROGRAM 10: CREATE BEAUTIFULSOUP OBJECT
# ============================================================

def program_10_create_soup():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.title)


# ============================================================
# PROGRAM 11: EXTRACT WEBSITE TITLE
# ============================================================

def program_11_website_title():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print("Title:", soup.title.text)


# ============================================================
# PROGRAM 12: EXTRACT FIRST HEADING
# ============================================================

def program_12_first_heading():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    heading = soup.find("h1")

    if heading:
        print("Heading:", heading.text.strip())
    else:
        print("No H1 heading found.")


# ============================================================
# PROGRAM 13: EXTRACT FIRST PARAGRAPH
# ============================================================

def program_13_first_paragraph():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraph = soup.find("p")

    if paragraph:
        print("Paragraph:", paragraph.text.strip())
    else:
        print("No paragraph found.")


# ============================================================
# PROGRAM 14: FIND FIRST H1 TAG
# ============================================================

def program_14_find_h1():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    heading = soup.find("h1")

    print(heading)


# ============================================================
# PROGRAM 15: FIND ALL H2 HEADINGS
# ============================================================

def program_15_find_all_h2():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all("h2")

    for heading in headings:
        print(heading.text.strip())


# ============================================================
# PROGRAM 16: EXTRACT ALL HEADINGS
# ============================================================

def program_16_all_headings():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all(["h1", "h2", "h3"])

    for heading in headings:
        print(heading.text.strip())


# ============================================================
# PROGRAM 17: EXTRACT ALL HYPERLINKS
# ============================================================

def program_17_all_links():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    for link in links:
        print(link.get("href"))


# ============================================================
# PROGRAM 18: EXTRACT FIRST LINK
# ============================================================

def program_18_first_link():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a")

    if link:
        print("Link:", link.get("href"))


# ============================================================
# PROGRAM 19: EXTRACT ALL IMAGE URLs
# ============================================================

def program_19_all_images():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    images = soup.find_all("img")

    for image in images:
        print(image.get("src"))


# ============================================================
# PROGRAM 20: EXTRACT ALL TABLES
# ============================================================

def program_20_all_tables():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table")

    print("Number of tables:", len(tables))

    for table in tables:
        print(table)


# ============================================================
# PROGRAM 21: USE get() METHOD
# ============================================================

def program_21_get_attribute():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a")

    if link:
        print(link.get("href"))


# ============================================================
# PROGRAM 22: USE SELECT()
# ============================================================

def program_22_css_select():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a")

    for link in links:
        print(link.get("href"))


# ============================================================
# PROGRAM 23: USE SELECT_ONE()
# ============================================================

def program_23_select_one():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.select_one("title")

    if title:
        print(title.text)


# ============================================================
# PROGRAM 24: SELECT BY CLASS
# ============================================================

def program_24_select_class():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.select(".btn")

    for element in elements:
        print(element.text.strip())


# ============================================================
# PROGRAM 25: SELECT BY ID
# ============================================================

def program_25_select_id():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.select("#header")

    print(element)


# ============================================================
# PROGRAM 26: SELECT NESTED ELEMENTS
# ============================================================

def program_26_nested_selector():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("nav a")

    for link in links:
        print(link.text.strip())


# ============================================================
# PROGRAM 27: FIND PARENT ELEMENT
# ============================================================

def program_27_parent():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title")

    if title:
        print("Parent:", title.parent.name)


# ============================================================
# PROGRAM 28: ACCESS CHILDREN
# ============================================================

def program_28_children():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    body = soup.find("body")

    if body:
        for child in body.children:
            print(child)


# ============================================================
# PROGRAM 29: PRETTIFY HTML
# ============================================================

def program_29_prettify():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify())


# ============================================================
# PROGRAM 30: COUNT HYPERLINKS
# ============================================================

def program_30_count_links():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    print("Total Links:", len(links))


# ============================================================
# PROGRAM 31: COMPLETE SCRAPING EXAMPLE
# ============================================================

def program_31_complete_scraper():
    response = requests.get(URL)

    if response.status_code != 200:
        print("Website could not be accessed.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    print("WEBSITE TITLE")
    print("--------------------")

    if soup.title:
        print(soup.title.text.strip())

    print("\nHEADINGS")
    print("--------------------")

    for heading in soup.find_all(["h1", "h2", "h3"]):
        text = heading.text.strip()

        if text:
            print(text)

    print("\nLINKS")
    print("--------------------")

    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            print(href)

    print("\nIMAGES")
    print("--------------------")

    for image in soup.find_all("img"):
        src = image.get("src")

        if src:
            print(src)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # Run one program at a time.

    program_1_get_request()

    program_2_status_code()
    program_3_check_website()
    program_4_html_source()
    program_5_headers()
    program_6_final_url()
    program_7_cookies()
    program_8_encoding()
    program_9_response_time()
    program_10_create_soup()
    program_11_website_title()
    program_12_first_heading()
    program_13_first_paragraph()
    program_14_find_h1()
    program_15_find_all_h2()
    program_16_all_headings()
    program_17_all_links()
    program_18_first_link()
    program_19_all_images()
    program_20_all_tables()
    program_21_get_attribute()
    program_22_css_select()
    program_23_select_one()
    program_24_select_class()
    program_25_select_id()
    program_26_nested_selector()
    program_27_parent()
    program_28_children()
    program_29_prettify()
    program_30_count_links()
    program_31_complete_scraper()