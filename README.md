# Travel Weather Planner

## 📌 Project Overview

This project determines whether commuting is possible based on:

- Distance to travel  
- Weather conditions  
- Available transport options  

The goal was to fulfil all user stories and pass 24 automated tests validating the logic and structure of the program.

---

## 🧪 Steps Required to Complete the Lab

### 1. Create Variables
The following variables were required:

- `distance_mi` — number  
- `is_raining` — boolean  
- `has_bike` — boolean  
- `has_car` — boolean  
- `has_ride_share_app` — boolean  

### 2. Use Conditional Logic
The program needed to:

- Use `if`, `elif`, and `else`  
- Evaluate distance categories in ascending order  
- Use at least one boolean operator (`and`, `or`, `not`)  
- Print `True` or `False`  

### 3. Commuting Rules
The logic had to follow these rules:

- **Falsy distance** → print `False`  
- **< 1 mile** → print `True` only if **not raining**  
- **> 1 and < 6 miles** → print `True` only if **has bike AND not raining**  
- **> 6 miles** → print `True` if **has car OR has ride-share app**  

### 4. Pass All 24 Tests
The tests validated:

- Variable creation  
- Correct data types  
- Correct conditional structure  
- Correct boolean logic  
- Correct printed output for every scenario  

---

## 💻 Final Code Solution

```python
# Travel Weather Planner
distance_mi = 6  # Storing integer in variable 
is_raining = False  # Storing boolean in variable 
has_bike = True  # Storing boolean in variable 
has_car = True  # Storing boolean in variable 
has_ride_share_app = True  # Storing boolean in variable 

if not distance_mi:  # Using an if statement to check if distance variable is falsy 
    print('False')  # If variable is falsy, output: False 
elif distance_mi <= 1 and not is_raining:  # Check if distance is 1 mile or less and it is not raining 
    print('True')  # If both conditions are true, output: True 
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:  
    # Check if distance is between 1 and 6 miles, person has bike, and it is not raining  
    print('True')  # If all conditions are true, output: True 
elif distance_mi > 6 and (has_car or has_ride_share_app):  
    # Check if distance is greater than 6 miles and the person has a car or ride-share app
    print('True')  # If either condition is true, output: True 
else:  
    print('False')  # If none of the conditions are met, output: False

## Test Results 
Passed: 1. You should have a variable named distance_mi.
Passed: 2. You should assign a number to your distance_mi variable.
Passed: 3. You should have a variable named is_raining.
Passed: 4. You should assign a boolean to your is_raining variable.
Passed: 5. You should have a variable named has_bike.
Passed: 6. You should assign a boolean to your has_bike variable.
Passed: 7. You should have a variable named has_car.
Passed: 8. You should assign a boolean to your has_car variable.
Passed: 9. You should have a variable named has_ride_share_app.
Passed: 10. You should assign a boolean to your has_ride_share_app variable.
Passed: 11. You should use at least one if statement.
Passed: 12. You should use at least one elif branch in your program.
Passed: 13. You should use at least one boolean operator (and, or, or not) in your code.
Passed: 14. You should use the print() function to display the result.
Passed: 15. When distance_mi is a falsy value, the program should print False.
Passed: 16. When the distance is 1 mile or less and it is not raining, the program should print True.
Passed: 17. When the distance is 1 mile or less and it is raining, the program should print False.
Passed: 18. When the distance is between 1 mile (excluded) and 6 miles (included), and it is raining with no bike, the program should print False.
Passed: 19. When the distance is between 1 mile (excluded) and 6 miles (included), it is not raining but no bike is available, the program should print False.
Passed: 20. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is not raining, the program should print True.
Passed: 21. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is raining, the program should print False.
Passed: 22. When the distance is greater than 6 miles and a ride share app is available, the program should print True.
Passed: 23. When the distance is greater than 6 miles and a car is available, the program should print True.
Passed: 24. When the distance is greater than 6 miles and neither a car nor a ride-share app is available, the program should print False.
