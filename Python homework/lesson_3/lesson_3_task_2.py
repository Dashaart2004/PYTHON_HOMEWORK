from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "Iphone 13", "+79009976654")
phone2 = Smartphone("Samsung", "Galaxy A20", "+79009955554")
phone3 = Smartphone("Apple", "Iphone 10", "+79999976654")
phone4 = Smartphone("Apple", "Iphone 7", "+79009976689")
phone5 = Smartphone("Samsung", "IGalaxy A20", "+79009536654")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} . {phone.phone_number}")