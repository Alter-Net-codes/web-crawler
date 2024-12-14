import requests

robotsURL = "https://adw-development.github.io/public/robots.txt"
mainURL = "https://adw-development.github.io/"

try:
    response = requests.get(robotsURL)
    response.raise_for_status()
    robots_content = response.text
    if "User-agent: ADW-bot\nDisallow:" in robots_content:
        print("access allowed for ADW to bot.")
        main_response = requests.get(mainURL)
        if main_response.status_code ==200:
            print("fetched the site sucsessfully.")
            print (main_response)
        else:
            print(f"access allowed but failed to fetch site. https status: {main_response.status_code}")
    elif "Disallow: /" in robots_content:
        print("access error.")
    else:
        main_response = requests.get(mainURL)
        if main_response.status_code:
            print("fetched the site sucsessfully")
        else:
            print(f"access allowed but failed to fetch site. https status: {main_response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"an error occurred {e}")
