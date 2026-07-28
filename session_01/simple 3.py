import json

dic ={"مدرسه": "استعدادهای درخشان سعدی",
       "کلاس":"پایتون",
       "سال": "۱۴۰۵",
       "معلمان": ["سمانه پهلوانی", "فاطمه شامحمدی"]
}

with open("class.json", "w", encoding='UTF-8') as file:
    json.dump(dic, file, ensure_ascii=False)

with open("class.json") as file:
    data = json.load(file)

print("نام مدرسه:", data["مدرسه"])
print("سال:", data["سال"])
print("اولین معلم:", data["معلمان"][0])
print("تعداد معلمان", len(data["معلمان"]))
