from bs4 import BeautifulSoup
import requests

def scrape_text(url: str):
  # Send a GET request to the webpage
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # parse the contents of the webpage with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # extract all text from the webpage
    text = soup.get_text(separator=" ", strip=True)

    # return the text
    return text
  else:
    # Print error message
    print("Error: Could not retrieve webpage")
    return f"Error: Could not retrieve webpage at {url}"