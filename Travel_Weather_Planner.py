# Travel Weather Planner
distance_mi = 6 #Storing integer in variable 
is_raining = False #Storing boolean in variable 
has_bike = True #Storing boolean in variable 
has_car = True #Storing boolean in variable 
has_ride_share_app = True #Storing boolean in variable 

if not distance_mi: #Using an if statement to check if distance variable is falsy 
    print('False') #If variable is falsy, output: False 
elif distance_mi <=1 and not is_raining: #Using elseif statement to check if distance_mi variable is 1 mile or less and it is not raining 
   print('True') #If both conditions amount to true, the output: True 
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining: #Using elseif statement to check if distance_mi variable is between 1 and 6 miles. 
#and person has bike and it is not raining  
  print('True')#If all conditions amount to true,output: True 
elif distance_mi > 6 and (has_car or has_ride_share_app):#Using elsif statement to check if distance_mi is grater than 6 miles and the person has_car or has_ride_share_app
    print('True')#If both conditions are satisfied, output:True 
else: #Using else statement 
    print('False')#If any condition returns false, output: False 