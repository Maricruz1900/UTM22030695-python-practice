#list
#list of food in the restaurant
print("THESE ARE THE RESTAURANT MEALS:")
foods = ["Pizza", "Hamburguer", "Chiness food", "Hotdog", "Tacos"]

#add element 
New_element = "wings"
foods.append("wings")

#print the element
for food in foods:
    print(food)




#Tuple
#tuple of the months of the year that never change
print("THESE ARE THE MONTHS OF THE YEAR:")

#the names of the months of the year are saved
month_of_the_year = ("January" , "February" , "March" , "April" , "May" , "June" , "July")
index = 0

while index < len(month_of_the_year):
 print(month_of_the_year[index])
 index += 1

