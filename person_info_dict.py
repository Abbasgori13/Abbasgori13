info = {"name": "Abbas", "gender": "male", "age": 24, "address": "1/49, main road, pandaravadai", "phone": 1956023562}

need = input("What info do you want to know about this person? ").lower()

print(info.get(need, "invalid information, try again"))