# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого ктласса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайе метод, выводящий
# информацию специфичную для данного класса.
class Fish():
    weight = 10
    def __init__(self, name,num_of_fins, area):
        self.num_of_fins = num_of_fins
        self.area = area
class Birds():
    weight = 2
    def __init__(self, name, migratory):
        self.migratory = migratory
        