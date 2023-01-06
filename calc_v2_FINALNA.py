#Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
# Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def calculateList(arguments):
    if action == 1:
        result = 0
        for i in range (len(arguments)):
            result = result + arguments[i]
    elif action == 2:
        result = arguments[0] - arguments[1]            
    elif action == 3:
            result = 1
            for argument in arguments:
                result = result * argument
    elif action == 4:
        if arguments[1] != 0:
            result = arguments[0]/arguments[1]            
        else:
            logging.debug("b = 0. Division by 0 is not allowed")    
    else:
        logging.debug("Zły wybór działania. wpisz liczbę 1,2,3 lub 4")
    logging.info(f"Wynik to {result}")
#print(dir(arguments))


if __name__ == "__main__": #część pobierania argumentów do działania
    action =int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    if action ==1:
        action_name ="Dodaję"; max_arg = int(input("Ile chcesz dodać liczb?"))
    elif action == 2:
        action_name ="Odejmuję"; max_arg =2
    elif action == 3:
        action_name ="Mnożę";max_arg = int(input("Ile chcesz dodać liczb?"))
    elif action == 4:
        action_name ="Dzielę";max_arg =2 
    
    arguments = []; #sprawdzam czy argumenty są liczbami (int lub float)
    for i in range (max_arg): 
        argument = (input(f"Podaj składnik {i+1}."))
        try:
            argument = int(argument)
            arguments.append(argument)
        except ValueError:
            try: 
                argument = float(argument)
                arguments.append(argument)
            except ValueError:
                print("Wprowadziłeś niepoprawną zmienną, spróbuj jeszcze raz wprowadzić liczbę")

    logging.info(f"{action_name} {arguments}")
    calculateList(arguments)


    





