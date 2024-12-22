import requests
proxy='101.109.220.38:8080'
response = requests.get("https://httpbin.org/ip", proxies={'http':proxy,'https':proxy}, timeout=15)
print(response.status_code)
print(response.json())
