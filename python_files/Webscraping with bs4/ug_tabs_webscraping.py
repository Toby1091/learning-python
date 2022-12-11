import requests
from bs4 import BeautifulSoup

url = "https://www.ultimate-guitar.com/explore"
result = requests.get(url).text
html_doc = BeautifulSoup(result, "html.parser")

tag = html_doc.find("div", class_="js-store")
mumblejumble = tag["data-content"]
mumblejumble_split = mumblejumble.split(",")

start_string = "tab_url"

uncleaned_link_list = []

# Produce a list where each element in the list is a string à la "tab_url":"https://tabs.ultimate-guitar.com/..."
def extract_unfiltered_link_elements(string_to_be_cleaned):
    for element in mumblejumble_split:
        if element.startswith('"tab_url"'):
            uncleaned_link_list.append(element)
    return uncleaned_link_list

uncleaned_link_list = extract_unfiltered_link_elements(mumblejumble_split)

# Clean the list by stripping away the "tab_url":

cleaned_link_list = []

for element in uncleaned_link_list:
    element_split = element.split(':')
    element_split[2] = element_split[2].strip('"')
    element_split[2] = element_split[2].strip('"//')
    cleaned_link_list.append(element_split[2])

for element in cleaned_link_list:
    print(element)





