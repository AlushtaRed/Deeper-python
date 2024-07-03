# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True


def deposit(amount):
    global bank_account
    global operations
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        # return bank_account
    else:
        print('Сумма должна быть кратной 50 у.е.')


def withdraw(amount):
    global bank_account
    global operations
    if amount*PERCENT_REMOVAL < MIN_REMOVAL:
        percent = MIN_REMOVAL
    elif amount*PERCENT_REMOVAL > MAX_REMOVAL:
        percent = MAX_REMOVAL
    else:
        percent = amount*PERCENT_REMOVAL
    if check_multiplicity(amount):
        amount_with_persent = amount+percent
        if amount_with_persent>bank_account:
            operations.append(f'Недостаточно средств. Сумма с комиссией {int(amount_with_persent)} у.е. На карте {bank_account} у.е.')
        else:
            bank_account = bank_account - amount_with_persent
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е.')
            # return bank_account, percent
        
    else:
        print('Сумма должна быть кратной 50 у.е.')
        amount_with_persent = amount+percent
        if amount_with_persent>bank_account:
            operations.append(f'Недостаточно средств. Сумма с комиссией {int(amount_with_persent)} у.е. На карте {bank_account} у.е.')
        else:
            bank_account = bank_account - amount_with_persent
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {percent} у.е.. Итого {bank_account} у.е.')
            # return bank_account, percent


def exit():
    global operations
    global bank_account
    if bank_account > RICHNESS_SUM:
        percent = bank_account*RICHNESS_PERCENT
        bank_account = bank_account - percent
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {percent} у.е. {bank_account} у.е.')
        operations.append(f'Возьмите карту на которой {bank_account} у.е.')
    else:
        operations.append(f'Возьмите карту на которой {bank_account} у.е.')



if __name__ == '__main__':
    deposit(173)
    withdraw(21)
    exit()

print(operations)
# print(bank_account)
