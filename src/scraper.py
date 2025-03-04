from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


links_by_cuisine = [
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=punjabi",
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=american",
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=indo-chinese",
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=italian",
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=hyderabadi",
    "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=mexican"
    ]


def get_driver():
    options = Options()
    service = Service(r"C:/Program Files/Microsoft/EdgeDriver/msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    return driver


def get_recipe_links(driver, url):
    recipe_links = []
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    while True:
        links = driver.find_elements(By.CLASS_NAME, "post-summary__image")
        for link in links:
            recipe_links.append(link.get_attribute("href"))

        try:
            # Wait for the 'Next' button
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".facetwp-page.next")))
            
            # Scroll to it
            ActionChains(driver).move_to_element(next_button).perform()
            
            # Click using JavaScript
            driver.execute_script("arguments[0].click();", next_button)
            
            # Wait for page load
            time.sleep(2)  

        except:
            print("No more pages available.")
            break  # Stop if no more 'Next' button

    return recipe_links


# Function to collect data from all the collected links
def collect_recipe_data(driver, recipe_links):
    recipe_data = {}
    for link in recipe_links:
        driver.get(link)
        wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds

        # Wait until the recipe card is loaded
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wprm-recipe-container")))

        # Extract data
        cuisine = driver.find_element(By.CSS_SELECTOR, ".wprm-recipe-cuisine.wprm-block-text-bold").text
        course = driver.find_element(By.CSS_SELECTOR, ".wprm-recipe-course.wprm-block-text-bold").text
        keywords = driver.find_element(By.CSS_SELECTOR, ".wprm-recipe-suitablefordiet.wprm-block-text-bold").text
        name = driver.find_element(By.CSS_SELECTOR, ".wprm-recipe-name.wprm-block-text-normal").text
        img_element = driver.find_element(By.CSS_SELECTOR, "img[data-lazy-src]")

        # Get the image URL from 'data-lazy-src' or 'src'
        imgurl = img_element.get_attribute("data-lazy-src")

        # If 'data-lazy-src' is missing, fallback to 'src'
        if not imgurl:
            imgurl = img_element.get_attribute("src")

        # Store data in a dictionary
        recipe_data[name] = {
            "imgurl": imgurl,
            "course": course,
            "cuisine": cuisine,
            "keywords": keywords
        }

    return recipe_data


driver = get_driver()

all_recipe_links = []  # List to store results

# Loop through each URL and scrape data
for url in links_by_cuisine:
    print(f"Scraping: {url}")
    all_recipe_links.extend(get_recipe_links(driver, url))

time.sleep(10)

# # Print all collected links
# for key, value in all_recipe_links.items():
#     print(f"\nRecipes from {key}:")
#     for v in value:
#         print(v)

# Print the first 5 links
print(all_recipe_links[:5])

# Print the last 5 links
print(all_recipe_links[-5:])

# Print the number of recipes collected
print("\nTotal number of recipes collected:", len(all_recipe_links))

try:
    # Collect data from all the collected links
    recipe_data = collect_recipe_data(driver, all_recipe_links)

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(recipe_data)
    df = df.to_csv("../data/scraped_recipes_vegrecipesofindia.csv", index=False)
finally:
    # Close the browser
    driver.quit()
