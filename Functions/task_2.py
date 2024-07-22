# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
text = 'тек   ст'

def unicode_text(text:str):
    
    result = [ord(i) for i in text]
    print(sorted(set(result), reverse=True))

unicode_text(text)