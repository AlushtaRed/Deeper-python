# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
class Animals():
    def __init__(self,name, predator) -> None:
        self.name = name
        self.predator = predator

class Fish(Animals):
    def __init__(self, num_of_fins, area, *ags,**kwargs):
        self.num_of_fins = num_of_fins
        self.area = area
        super().__init__(*ags,**kwargs)

class Birds(Animals):
    def __init__(self, migratory, *ags,**kwargs):
        self.migratory = migratory
        super().__init__(*ags,**kwargs)
        
fish1 = Fish(5, 'sea', 'shark', True)
print(fish1.__dict__)
# print(fish1)