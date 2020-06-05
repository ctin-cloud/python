# Project: Purchasing Information and Receipts for Lovely Loveseats 


## Begin inventory ##  

#Item 1 - Love seat 
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood.. 32 inches high x 40 inches wide x 30 inches deep. Red or white' 

# Love seat price 
lovely_loveseat_price = 254.00

#Item 2 - Settee
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

# Settee price 
stylish_settee_price = 180.50
 
 #Item 3 - Lamp 
luxurious_lamp_description = 'Luxurious Lamp. glass and iron. 36 inches tall. Brown with cream shade.'

#Lamp price 
luxrious_lamp_price = 52.12 

#sales tax 
sales_tax = .088 

## End inventory list  ##  

## Customer 1 ## 
 
customer_one_total = 0 
customer_one_itemization = ""
 
#Customer1 buying love seat. 
customer_one_total = lovely_loveseat_price
 
customer_one_itemization= lovely_loveseat_description 
 
#adding 2nd item 

customer_one_total +=stylish_settee_price

customer_one_itemization += stylish_settee_description  

##adding 3rd item 
 
customer_one_total += luxrious_lamp_price  

customer_one_itemization += luxurious_lamp_description

## Calculate sales tax 
customer_one_tax = customer_one_total * sales_tax

## Printing out receipt! 
## Heading  
 
print ("Customer One Items:") 
print(customer_one_itemization) 

## Heading for title 
print ("Customer One Total:")
print(customer_one_total)

  
