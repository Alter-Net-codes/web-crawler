import requests

robots_url = "https://adw-development.github.io/public/robots.txt"
main_url = "https://adw-development.github.io"

try:
    response = requests.get(robots_url)
    response.raise_for_status()
    robots_content = response.text

    if "User-agent: ADW-bot\nDisallow:" in robots_content:
        print("access allowed for ADW-bot.")
        main_response = requests.get(main_url)
        if main_response.status_code == 200:
            print("fetched the site successfully.")
        else:
            print(f"access allowed, but failed to fetch site. http status: {main_response.status_code}")
    elif "Disallow: /" in robots_content:
        print("access error: entire site is disallowed for all bots.")
    else:
        print("no specific rules for ADW-bot. proceeding to fetch site.")
        main_response = requests.get(main_url)
        if main_response.status_code == 200:
            print("fetched the site successfully.")
        else:
            print(f"failed to fetch site. http status: {main_response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"an error occurred: {e}")
