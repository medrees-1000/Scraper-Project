from playwright.sync_api import sync_playwright


# Define a function to scrape the desired section of the website
def scrape_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # You can modify this selector to match the specific section you want to scrape
        section_content = page.inner_html()
        browser.close()
    return section_content

# Call the function and store the scraped content
scraped_content = scrape_website('https://www.fotmob.com/players/737066/erling-haaland')

# Print or process the scraped content as needed
print(scraped_content)
