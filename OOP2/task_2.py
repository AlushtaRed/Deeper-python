# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Документация к архиву
    """
    archive = []
    
    def __init__(self,num,text):
        
        self.num = num
        self.text = text
        self.new_archive = Archive.archive
        self.new_archive.append((num,text))

    
a = Archive(1,'a')
print(a.new_archive)
b = Archive(2, 'b')
print(b.new_archive)
c = Archive(2, 'c')
print(c.new_archive)
print(Archive.archive)
