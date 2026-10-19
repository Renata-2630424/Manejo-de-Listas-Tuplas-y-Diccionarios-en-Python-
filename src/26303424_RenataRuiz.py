
# Renata Guadalupe Ruiz de la Cruz
# 2630424
# IM1-1

# executive summary

# Lista es mutable y ordenada, tupla es ordenada pero inmutable.
# Son estructuras de datos para almacenar y organizar información.
# Diccionario es mutable y no ordenada (colecciones donde cada elemento tiene una clave única).
# Mutable: agregar, eliminar o modificar elementos de su creación, e inmutables es una vez creadas no cambian.
# Cada clave en un diccionario identifica su valor, ya que son únicas.
# El documento contendra descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas y 
# uso de listas, tuplas y diccionarios en contextos prácticos (ejercicios).


# Problem 1: Shopping list basics (list operations)

#Description
#Work with a list of products (strings) and their quantities (integers).
#The program should:
#1) Create an initial list of products.
#2) Allow adding a new product at the end.
#3) Show the total number of items in the list.
#4) Check if a specific product is in the list (boolean is_in_list).

#Input 
#initial list of products.
initial_items = ["chocolate bar", "fried chicken", "soda"] 
print("original list:", initial_items) 

#Enter new product
new_items_input = input("enter a new item or several (separated by a comma):")
new_items = new_items_input.split(",") #split by commas

#for
for item in new_items:
    initial_items.append(item.strip()) #add to the list and remove blank spaces

#Product to search
search_item = input("Enter product to search (between the original list and the new item): ") 
#Found item
is_in_list = search_item in initial_items #Check that it's on the list
#count items
len_list = len(initial_items)

#Output 
print("Items list:", initial_items)#final list

print("Found item:", str(is_in_list).upper()) ##true if paso and false if not

print("Total items:", len_list)#total number of items
 
# Casos de prueba

#NORMAL
"""
Terminal:
  original list: ['chocolate bar', 'fried chicken', 'soda']
  enter a new item or several (separated by a comma): lemon
  Enter product to search (between the original list and the new item): lemon
  Items list: ['chocolate bar', 'fried chicken', 'soda', 'lemon']
  Found item: TRUE
  Total items: 4
"""
#BORDE 
"""
original list: ['chocolate bar', 'fried chicken', 'soda']
  enter a new item or several (separated by a comma): lemon,       meat, milk
  Enter product to search (between the original list and the new item): lemon
  Items list: ['chocolate bar', 'fried chicken', 'soda', 'lemon', 'meat', 'milk']
  Found item: TRUE
  Total items: 6
"""
#ERROR
"""
original list: ['chocolate bar', 'fried chicken', 'soda']
  enter a new item or several (separated by a comma): lemon,       meat, milk
  Enter product to search (between the original list and the new item): pizza
  Items list: ['chocolate bar', 'fried chicken', 'soda', 'lemon', 'meat', 'milk']
  Found item: FALSE
  Total items: 6

"""
# Problem 2: Points and distances with tuples
#Description:
#Use tuples to represent two points on a 2D plane: (x1, y1) and (x2, y2). The program should:
#1) Make two tuples, point_a and point_b, from numeric inputs.
#2) Calculate the Euclidean distance between the points.
#3) Make a new tuple, midpoint, with the point right in the middle of them.

# Input
# Create an empty list to store the coordinates
coordinates = []

# List of coordinates names to ask the user
coordinates_names = ["x1", "y1", "x2", "y2"]

# Use a loop to avoid repeating input (╥_╥)
for name in coordinates_names:
    value = float(input(f"Enter {name} coordinate: "))
    coordinates.append(value)

# Assign values from the list to variables
x1 = coordinates[0]
y1 = coordinates[1]
x2 = coordinates[2]
y2 = coordinates[3]

# Create tuples
point_a = (x1, y1) #coordinates point A
point_b = (x2, y2)  #coordinates point B

# Calculate distance with the operation suggested by the teacher
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Calculate midpoint with the operation suggested by the teacher
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

# Output
print("Point A:", point_a) #coordinates point A
print("Point B:", point_b) #coordinates point B
print("Distance:", distance)
print("Midpoint:", midpoint)

# Casos de prueba

#NORMAL
"""
Terminal:
  Enter x1 coordinate: 0.0
  Enter y1 coordinate: 0.0
  Enter x2 coordinate: 3.0
  Enter y2 coordinate: 4.0
  Point A: (0.0, 0.0)
  Point B: (3.0, 4.0)
  Distance: 5.0
  Midpoint: (1.5, 2.0)
"""
#BORDE 
"""
Enter x1 coordinate: -1.5
  Enter y1 coordinate: 2.0
  Enter x2 coordinate: 4.5
  Enter y2 coordinate: -2.0
  Point A: (-1.5, 2.0)
  Point B: (4.5, -2.0)
  Distance: 7.211102550927978
  Midpoint: (1.5, 0.0)
"""
#ERROR

"""
Enter x1 coordinate: 1
Enter y1 coordinate: 2
Enter x2 coordinate: 4
Enter y2 coordinate: 1bc

ValueError: could not convert string to float: '1bc'
"""

# Problem 3: Product catalog with dictionary
#Description:
#Manage a small product catalog using a dictionary where:
#- key: product name (string) -value: unit price (float)
#The program should:
#1) Create an initial dictionary with at least 3 products.
#2) Read the name of a product and the quantity to buy.
#3) Calculate the total to pay if the product exists.
#4) If the product doesn't exist, show an error message.

# Initial products dictionary with prices
products_prices = {"chocolate bar": 25.00, "soda": 17.80,"chips": 20.00}
print("initial dictionary:", products_prices)

# Inputs

#It won't let you proceed; you didn't enter the product name and quantity because is empty
product_name = input("Enter product name to buy: ").strip() #remove blank spaces

 #if & else
if product_name == "":
    print("Error: Enter product name (¬_¬)")
else:
    quantity_product = input("Enter quantity: ")
     #if, elif & else
    if quantity_product == "":
        print("Error: Enter quantity (O_O)!")
    elif int(quantity_product) <= 0:
            print("Error: Quantity must be greater than zero.")#it doesn't accept amounts less than 0, only higher
    else:
        quantity = int(quantity_product)  #transform the variable that the user wrote input() always comes out as a string and with int it saves it as a number
        
        #if & else
        if product_name in products_prices: #in to check for the existence of a key.
            unit_price = products_prices[product_name] #look for its associated product value
            total_price = unit_price * quantity ## If the product is in stock, calculate the price.
            
            # Outputs 
            
            print("Unit price:", unit_price) #shows the price per unit.
            print("Total:", total_price)#shows the total price.
        else: # It will be shown when you enter a product that is not in the dictionary, 
            print("Error: product not found") #after putting the item and the quantity

# nested conditionals: you have an if (or else) structure nested inside another one
# to evaluate secondary or dependent conditions.

# CASE NORMAL
"""
Enter product name to buy: soda
Enter quantity: 5
Unit price: 15
Quantity: 5
Total: 75
"""

# CASE BORDE 
"""
Enter product name to buy: soda
Enter quantity: 1
Unit price: 15
Quantity: 1
Total: 15
"""

# CASE ERROR 
"""
Enter product name to buy: hamburguesa
Enter quantity: 2
Error: product not found
"""                                        

# Problem 4: Student grades with dict and list
# Manages student grades using a dictionary:
# - key: student name (string) - value: list of grades (list of float)
# The program must:
# 1) Create a dictionary with at least 3 students, each with a list of grades.
# 2) Read the name of a student.
# 3) Calculate the average of their grades.
# 4) Indicate if the student passed (average >= 70.0) using a boolean is_passed.

#Initial dictionary with students names and their list of grades of three units
grades = {"Daniela": [90.0, 85.0, 95.0], "Fatima": [70.0, 100.0, 90.0],"Luis": [50.0, 85.0, 70.0]}
print("initial dictionary:", grades)

#Input
## enter the name of the student we want to look up
student_name = input("Enter student name: ").strip()#remove blank spaces

if student_name == "":
    print("Error: Student name cannot be empty")
elif student_name not in grades: # not in: check if an item is not in the list
    print("Error: student not found")
else:
    student_grades = grades[student_name] 
    average = sum(student_grades) / len(student_grades) # to calculate the average.
    passed = average >= 70.0 ##Comparison of average equal to or greater than 70

#Outputs
    print("minimum average to pass: 70")
    print("Average:", average)# #show the average
    print("Passed:", str(passed).title()) #true if paso and false if not
# Due to an indentation error, that's why in the else I put everything that follows with indentation, 
# otherwise it throws a NameError because the variables are not defined since they are read directly 
#and not in order through the if, elif, and else.


# CASE NORMAL
"""
initial dictionary: {'Daniela': [90.0, 85.0, 95.0], 'Fatima': [70.0, 100.0, 90.0], 'Luis': [50.0, 85.0, 70.0]}
Enter student name: Daniela
minimum average to pass: 70
Average: 90.0
Passed: True
"""

# CASE BORDE 
"""
initial dictionary: {'Daniela': [90.0, 85.0, 95.0], 'Fatima': [70.0, 100.0, 90.0], 'Luis': [50.0, 85.0, 70.0]}
Enter student name: Luis
promedio mínimo para aprobar:70
Average: 68.33333333333333
Passed: False
"""

# CASE ERROR 
"""
initial dictionary: {'Daniela': [90.0, 85.0, 95.0], 'Fatima': [70.0, 100.0, 90.0], 'Luis': [50.0, 85.0, 70.0]}
Enter student name:
Error: Student name cannot be empty
"""                                  


# Problem 5: Word frequency counter (list + dict)
# Description:
# Counts the frequency of each word in a sentence using:
# - A list of words. - A dictionary where: - key: word (string) - value: frequency (int)
# The program must:
# 1) Read a sentence.
# 2) Convert it to lowercase and split it into a list of words.
# 3) Build a frequency dictionary.
# 4) Display the complete dictionary and the most frequent word.

#Enter a sentence to later be able to read it
sentence = input("Enter sentence: ")

# Lowercase it and split into a list of words
words_list = sentence.lower().split()

#if & else
if len(sentence) == 0:
    print("Error: Sentence cannot be empty ₍^. .^₎⟆") ##If this sentence is empty it shows an error message
else:
    words_list = sentence.lower().split() #Convert it to lowercase and split it into a list of words.
    print(sentence)

#Build the dictionary of word frequencies in the sentence
frequencies_dictionary = {} #empty dictionary
for word in words_list: ##Use of for loop #Go through the list and update the dictionary
    if word in frequencies_dictionary:
        frequencies_dictionary[word] += 1
    else:
        frequencies_dictionary[word] = 1

maximum_frequency = -1 #the minimum frequency any word can have is 1 (once)
# #we make sure that the first word the loop evaluates beats -1 and gets counted

#Loop to find the most frequent word
for word, frequency in frequencies_dictionary.items():
    if frequency > maximum_frequency: # Compare frequency (actual word) with the highest frequency
        maximum_frequency = frequency ## if it's the same, the frequency becomes higher
        most_common_word = word # save the name of the word

#Outputs
        print("Words list:", words_list) # List of the sentence by words separated by commas
        print("Frequencies:", frequencies_dictionary) # Number of times each word is repeated
        print("Most common word:", most_common_word) # Word that appears the most (if there's a tie, any one is valid)

# CASE NORMAL
"""
Enter sentence:  My name is Renata and my dog
 My name is Renata and my dog
Frequencies: {'my': 2, 'name': 1, 'is': 1, 'renata': 1, 'and': 1, 'dog': 1}
Most common word: my
"""

# CASE BORDE 
"""
     rent   is   high
    rent   is   high
Words list: ['rent', 'is', 'high']
Frequencies: {'rent': 1, 'is': 1, 'high': 1}
Most common word: rent
"""
"""
Enter sentence: coooool
coooool
Words list: ['coooool']
Frequencies: {'coooool': 1}
"""
# CASE ERROR 
"""
Enter sentence:
Error: Sentence cannot be empty ₍^. .^₎⟆
"""  
# Problem 6: Simple contact book (dictionary CRUD)
# Description:
# Implement a mini "contact book" using a dictionary where:
# - key: contact name (string) - value: phone number (string)
# The program must:
# 1) Create an initial dictionary with some contacts.
# 2) Read an action action_text ("ADD", "SEARCH" or "DELETE").
# 3) Depending on the action:
#    - "ADD": reads name and phone, adds or updates the contact.
#    - "SEARCH": reads name and displays the phone if it exists.
#    - "DELETE": reads name and deletes the contact if it exists.
# 4) Display a message indicating the result of the operation.

#Create an initial dictionary with some contacts
contacts = {"Joana": "6207710549","Fatima": "5538529017", "Diego": "3019855562"}
print(contacts) # initial dictionary
action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper() #Uppercase and without blank spaces
if action_text not in ["ADD", "SEARCH", "DELETE"]: ##Make sure they choose one of the specified actions, otherwise print an error message
    print("Error: Invalid action (–⌓–)")
else: #action ADD
    if action_text == "ADD":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()#add or update the contact
        if name == "" or phone == "": #Do not leave the enter name or phone blank
            print("Error: Name and phone cannot be empty (╹ -╹)")
        else: contacts[name] = phone  
        print("Contact saved:", name, phone) #Ouput Name and phone

    #action SEARCH:
    elif action_text == "SEARCH":
        name = input("Enter name to search: ").strip() #read name and search contact

        if name in contacts:
            print("Phone:", contacts[name]) #Ouput #Number if we find the contact in the dictionary
        else:
            print("Error: contact not found (◞ _◟)") #Ouput #if we don’t find the contact in the dictionary, send an error message
    
     #action DELETE:
    elif action_text == "DELETE":
        name = input("Enter name to delete: ").strip() #read name and delete contact
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name) #Ouput #shows the name of the contact that was deleted
        else:
            print("Error: contact not found (>﹏<)") #Ouput #if we don’t find the contact in the dictionary, send an error message
print("Updated contacts dictionary:", contacts) ##Shows how the dictionary looked after the action

#Nested conditionals are very useful and easy to use once
#you make sense of them, but if you make mistakes with the 
#indentation, you break all the coherence.

# NORMAL CASE: Successful contact search (SEARCH)
"""
Enter action (ADD, SEARCH, DELETE): SEARCH
Enter name to search: Diego
Phone: 3019855562
"""

# ERROR CASE: Searching for a non-existent contact (SEARCH)
"""
Enter action (ADD, SEARCH, DELETE): SEARCH
Enter name to search: Maria
Error: contact not found (◞ _◟)
"""

# ERROR CASE: Attempting to delete a non-existent contact (DELETE)
"""
Enter action (ADD, SEARCH, DELETE): DELETE
Enter name to delete: victor
Error: contact not found (>﹏<)
"""

# NORMAL CASE: Successful contact deletion (DELETE)
"""
Enter action (ADD, SEARCH, DELETE): DELETE
Enter name to delete: Fatima
Contact deleted: Fatima
Updated contacts dictionary: {'Joana': '6207710549', 'Diego': '3019855562'}
"""

# NORMAL CASE: Adding a new contact (ADD)
"""
Enter action (ADD, SEARCH, DELETE): ADD
Enter name: Renata
Enter phone: 1234567890
Contact saved: Renata 1234567890
Updated contacts dictionary: {'Joana': '6207710549', 'Fatima': '5538529017', 'Diego': '3019855562', 'Renata': '1234567890'}
"""

# Updating an existing contact's phone number (ADD)
"""
Enter action (ADD, SEARCH, DELETE): ADD
Enter name: Fatima
Enter phone: 1234567890
Contact saved: Fatima 1234567890
Updated contacts dictionary: {'Joana': '6207710549', 'Fatima': '1234567890', 'Diego': '3019855562'}
"""
# 8. CONCLUSIONS
# In conclusion, use lists when you need a collection that can be changed and ordered, associating its value to the key.
# In lists, you can add, remove, and replace without needing to create another structure.
# Tuples tuples for fixed constants. They are useful for data that must remain constant in a loop.
# Dictionaries for named data. Dictionaries make searches by key easier since you don’t need to go through the entire
# collection; you have direct access instead of numerical indices, avoiding performance 
# hurdles with large lists. Combining these data structures—such as using a list of 
# dictionaries—proves to be extremely powerful for organizing complex datasets.
"""
Rreferences:
1.De la Cruz, R. (2026). Python Class Repository and Notes. GitHub.
   https://github.com/Renata-2630424/Python_class
2. Python Software Foundation. (2026). More on Lists — Python Documentation. 
   https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

3. Python Software Foundation. (2026). Tuples and Sequences — Python Documentation. 
   https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

4. Python Software Foundation. (2026). Dictionaries — Python Documentation. 
   https://docs.python.org/3/tutorial/datastructures.html#dictionaries

5.BitBoss. (2021, junio 1). Estructuras de datos con Python en 8 minutos: Listas, Tuplas, Conjuntos y Diccionarios [Video]. 
  YouTube. http://www.youtube.com/watch?v=v25-m1LOUiU
"""