# Модуль перевірки номерних знаків

Цей модуль містить інструменти для взаємодії з сайтом `https://opendata.hsc.gov.ua/check-leisure-license-plates/` для перевірки інформації про номерні знаки.

Він використовує бібліотеку `requests` для відправки HTTP-запитів та регулярні вирази для аналізу HTML-відповідей.

## Залежності
- Python 3.7 або вище
- requests

## Встановлення

Для встановлення всіх необхідних залежностей вам знадобиться Python 3.7 або вище.

Якщо у вас вже встановлений Python, ви можете встановити `requests` за допомогою наступної команди:

```bash
pip install requests
```

Якщо ви ще не встановили Python, відвідайте [офіційний сайт Python](https://www.python.org/) та дотримуйтесь інструкцій по встановленню для вашої операційної системи.

Після встановлення Python, ви можете встановити `requests` за допомогою команди, вказаної вище.

## Використання

```python
from plate_checker import LicensePlateChecker

url = "https://opendata.hsc.gov.ua/check-leisure-license-plates/"
headers = {
    # headers go here
}
checker = LicensePlateChecker(url, headers)
data = checker.get_plate_data('26', 'Весь регіон', 'electric_car', '2412')
for d in data:
    print(f"Номерний знак: {d.number}")
    print(f"Ціна за комбінацію: {d.price}")
    print(f"Місце знаходження: {d.location}\n")
```

У цьому прикладі створюється об'єкт `LicensePlateChecker` з вказаними URL-адресою та заголовками. Потім викликається метод `get_plate_data`, який повертає список об'єктів `LicensePlateData`, кожен з яких містить інформацію про конкретний номерний знак. Ця інформація потім виводиться на екран.
