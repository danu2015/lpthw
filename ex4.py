cars = 100 #se atribuie variabilei cars valoarea 100
space_in_a_car = 4 #se atribuie variabilei space_in_a_car valoarea 4
drivers = 30 #se atribuie variabilei drivers valoarea 30
passengers = 90 #se atribuie variabilei passengers valoarea 90
cars_not_driven = cars - drivers #se calculeaza diferenta dintre valoarea cars si valoarea drivers si se atribuie variabilei cars_not_driven
cars_driven = drivers #se atribuie valoarea variabilei drivers variabilei cars_driven
carpool_capacity = cars_driven * space_in_a_car #se atribuie valoarea produs intre valorile variabilelor cars_driven si space_in_a_car varibilei carpool_capacity
average_passengers_per_car = passengers / cars_driven #se atribuie valoarea impartirii valorii passengers la valorea cars_driven varibilei average_passengers_per_car


print("There are", cars, "cars available.") #se afiseaza "There are" valoarea variabilei cars "cars available."
print("There are only", drivers, "drivers available.") #s
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")
