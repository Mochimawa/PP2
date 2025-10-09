import json

# читаем файл
with open('sample-data.json') as f:
    data = json.load(f)

# вывод заголовков
print("Interface Status")
print("=" * 80)
print("DN".ljust(50), "Description".ljust(20), "Speed".ljust(8), "MTU")
print("-" * 80)

# проходим по данным и выводим значения
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    descr = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn.ljust(50)} {descr.ljust(20)} {speed.ljust(8)} {mtu}")
