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



#Dictionary
print("THESE ARE THE FLOWERS AVAILABLE:") 
flowers ={
    "FLOWERS": "Sunflowers, Roses, Tulips, Cloud flower, Daisies",
    "COST": "$250",
    "COLORS": "Yellow, Pink, Red, Blue, Purple, White",
}
#change the variable 2
flowers["COST"] = "$190"

#Variable 2 modified
print(flowers)



#Function
print("THESE ARE THE FUNCTIONS")
#Here the operand and the number one and two are defined
def operation(operating, number1, number2):

    #here it is indicated that if it is + it will be added
    if operating == '+':
        Result = number1 + number2
    #is subtracted
    elif operating == '-':
        Result = number1 - number2
    #it divides    
    elif operating == '/':
        Result = number1 / number2
    #it multiplies    
    elif operating == '*':
        Result = number1 * number2
    else:
        Result = None
    return Result

##you are prompted to enter the operand you want to perform
print("ENTER THE OPERAND + - / * ")
operand = input()

## you are prompted to enter the first number
print("ENTER THE NUMBER1")
number1 =int(input())

## you are prompted to enter the second number
print("ENTER THE NUMBER2")
number2 =int(input())

#here the result is printed with the 2 numbers indicated by the user and the operand
result = operation(operand, number1, number2)
print(result)

