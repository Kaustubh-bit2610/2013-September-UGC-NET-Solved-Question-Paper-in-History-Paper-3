from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        
        # Create a new page
        page = browser.new_page()
        
        # Open the website
        page.goto('https://www.netugc.com/ugc-net-solved-question-papers-in-history/2013-september-ugc-net-solved-question-paper-in-history-paper-3')

        # Wait for the element to be present
        # page.wait_for_selector('#yDmH0d > div:nth-child(1) > div > div:nth-child(2) > div.QZ3zWd > div > div.UtePc.RCETm.yxgWrb')

        # Get elements by CSS selector
        elements = page.query_selector_all('#yDmH0d > div:nth-child(1) > div > div:nth-child(2) > div.QZ3zWd > div > div.UtePc.RCETm.yxgWrb')
        
        # Print the text content of the found elements
        for element in elements:
            print(element.inner_text())
            print("=======================================")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()