from selenium import webdriver
from bs4 import BeautifulSoup

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Replace 'Your Search Key' with the actual search key
search_key = "SAEE09900B"

# Construct the search results URL
search_url = f"https://cercalatuascuola.istruzione.it/cercalatuascuola/ricerca/risultati?rapida={search_key}&tipoRicerca=RAPIDA&gidf=1"

# Navigate to the search results page
driver.get(search_url)

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Locate the relevant HTML element that contains the school name and extract the text
school_name_element = soup.find("td", class_="sc-tab-plesso")
school_name = school_name_element.find("a").text.strip()
school_name = school_name.lower().replace(" ", "-")
print(f"School Name: {school_name}")

string2 = "https://cercalatuascuola.istruzione.it/cercalatuascuola/istituti/" + search_key.replace('"', '') + "/"  + school_name.replace('"', '') + "/" + "personale/"
print(string2)

driver.get(string2)

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")










# Close the browser
#driver.quit()
