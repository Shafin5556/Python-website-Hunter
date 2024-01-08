import json


with open('chrome_cookies.json', 'r') as file:
    imported_cookies = json.load(file)

formatted_cookies = []

for cookie in imported_cookies:
    formatted_cookie = {
        "name": cookie["name"],
        "value": cookie["value"],
        "domain": cookie["domain"],
        "path": cookie["path"],
        "expires": cookie["expires"],
        "secure": bool(cookie["secure"]),  
        "httpOnly": bool(cookie["_rest"].get("HTTPOnly")) if "_rest" in cookie else False
    }

    formatted_cookies.append(formatted_cookie)

# Save the modified cookies to a new JSON file
with open('modified_cookies.json', 'w') as file:
    json.dump(formatted_cookies, file, indent=4)

print("Cookies modified and saved as 'modified_cookies.json'.")
