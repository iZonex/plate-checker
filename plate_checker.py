import requests
import re
from dataclasses import dataclass
from typing import List

@dataclass
class LicensePlateData:
    number: str
    price: str
    location: str

class LicensePlateChecker:
    def __init__(self, url: str = None, headers: dict = None):
        self.url = url or "https://opendata.hsc.gov.ua/check-leisure-license-plates/"
        self.headers = headers or {}

    def get_csrf_token(self) -> str:
        response = requests.get(self.url, headers=self.headers, verify=False)
        html = response.text
        csrf_token = re.findall(r'<input type="hidden" name="csrfmiddlewaretoken" value="(.+?)">', html)[0]
        return csrf_token

    def get_plate_data(self, region: str, tsc: str, type_venichle: str, number: str) -> List[LicensePlateData]:
        data = {
            'region': region,
            'tsc': tsc,
            'type_venichle': type_venichle,
            'number': number,
            'csrfmiddlewaretoken': self.get_csrf_token()
        }

        response = requests.post(self.url, headers=self.headers, data=data, verify=False)

        pattern = r'<table class="display" style="width:100%" id="example">(.*?)</table>'
        table_match = re.search(pattern, response.text, re.DOTALL)

        if table_match:
            row_pattern = r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>'
            row_matches = re.findall(row_pattern, table_match.group(1), re.DOTALL)
            
            return [LicensePlateData(number=row[0], price=row[1], location=row[2]) for row in row_matches[1:]]

        return []


if __name__ == "__main__":
    checker = LicensePlateChecker()
    data = checker.get_plate_data('26', 'Весь регіон', 'electric_car', '5267')
    for d in data:
        print(f"Номерний знак: {d.number}")
        print(f"Ціна за комбінацію: {d.price}")
        print(f"Місце знаходження: {d.location}\n")
