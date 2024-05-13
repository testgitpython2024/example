import random

print("Добро пожаловать в игру 'Камень, ножницы, бумага, спок, змея'")
playerScore = 0
botScore = 0
for i in range(3):
    answer = input("Что выберешь?\n").lower()
    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"
    elif answer.find("спок") != -1:
        answer = "с"
    elif answer.find("змея") != -1 or answer.find("змею") != -1:
        answer = "з"
    print(answer)
    botAnswer = random.choice(["камень", "ножницы", "бумага", "спок", "змея"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    print(botAnswer)
    if answer == botAnswer:
        print("Ничья")
    elif (answer == "к" and (botAnswer == "н" or botAnswer == "з")) or \
            (answer == "н" and (botAnswer == "б" or botAnswer == "з")) or \
            (answer == "б" and (botAnswer == "к" or botAnswer == "с")) or \
            (answer == "с" and (botAnswer == "к" or botAnswer == "н")) or \
            (answer == "з" and (botAnswer == "с" or botAnswer == "б")):
        print("Ты победил")
        playerScore += 1
    else:
        print("Я победил")
        botScore += 1
if playerScore == botScore:
    print("ничья по итогам трёх раундов")
elif botScore < playerScore:
    print("я проиграл по итогам трёх раундов")
else:
    print("я победил по итогам трёх раундов")
