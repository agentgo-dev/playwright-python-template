import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    options = {
        "args": [
            f"--datascaler-apikey={os.environ.get('AGENTGO_API_KEY')}",
        ]
    }

    # Encode options for the connection URL
    import json
    import urllib.parse
    url_option_value = urllib.parse.quote(json.dumps(options))

    # Connect to AgentGo's distributed browser network
    server_url = f"ws://any.browsers.live:3000?launch-options={url_option_value}"
    browser = p.chromium.connect(server_url)

    # Create a new page
    page = browser.new_page()

    # Navigate to a website
    page.goto("https://news.ycombinator.com/", wait_until="load")

    # Perform some actions(example: get the title)
    title = page.title()
    print(f"Page title: {title}")

    # Close the browser
    page.close()
    browser.close()
    print("Browser session completed successfully!")
