items = {
    "ключи": 0.1,
    "кошелек": 0.4,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
backpack = {}
current_weight = 0
for key,value in items.items():
    if current_weight+ value < max_weight:
        backpack[key]=value
        current_weight = current_weight+value
    

print(backpack)
