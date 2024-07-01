import requests
from django.utils import timezone

resp = requests.get("https://www.google.com.tw/")
print(resp, "************")

print(timezone.now(), "******************")