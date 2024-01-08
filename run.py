import json
import psutil
from browser_cookie3 import chrome
import tldextract

def close_chrome():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chrome' in proc.info['name'].lower():
            print(f"Closing Chrome (PID: {proc.info['pid']})")
            proc.kill()


close_chrome()


target_domain = ".facebook.com"  



chrome_cookies = chrome(domain_name=target_domain)


formatted_cookies = []
for cookie in chrome_cookies:
    domain_extract = tldextract.extract(cookie.domain)
    domain_subdomain = domain_extract.subdomain


    host_only = False if domain_subdomain else True

    secure = True if cookie.secure else False


    http_only = False if 'HttpOnly' not in cookie._rest else True




    cookie_dict = {
        "domain": cookie.domain,
        "expirationDate": cookie.expires,
        "hostOnly": host_only,
        "httpOnly": http_only,
        "name": cookie.name,
        "path": cookie.path,
        "sameSite": "no_restriction",
        "secure": secure,
        "storeId": "null",  
        "session": cookie.expires == 0, 
        "value": cookie.value
    }


    cookie_dict = {
        k: cookie_dict[k] for k in sorted(cookie_dict.keys() - {"value"})}  
    cookie_dict["value"] = cookie.value

    formatted_cookies.append(cookie_dict)

file_path = f"{target_domain}_cookies.json"
with open(file_path, 'w') as file:
    json.dump(formatted_cookies, file, indent=4, default=str)  

print(f"Cookies for {target_domain} domain scraped and saved in {file_path}")
