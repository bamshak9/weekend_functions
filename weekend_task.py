def task1_sum_of_two_numbers(a, b):
"""Accepts two numbers and returns their sum."""
   return a + b
print("Task 1:", task1_sum_of_two_numbers(3, 7))
def task2_square_number(n):
"""Accepts a number and returns its square."""
    return n * n
print("Task 2:", task2_square_number(5))
def task3_greet_user(name):
"""Accepts a name and prints a greeting."""
print("Hello,", name + "!")
task3_greet_user("John")
def task4_area_of_rectangle(length, width):
    """Accepts length & width and returns area."""
    return length * width
print("Task 4:", task4_area_of_rectangle(5, 10))
def task5_perimeter_of_square(side):
    """Accepts side of a square and returns perimeter."""
    return 4 * side
print("Task 5:", task5_perimeter_of_square(6))
def task6_celsius_to_fahrenheit(celsius):
"""Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
print("Task 6:", task6_celsius_to_fahrenheit(0))
def task7_find_max(a, b, c):
     """Returns the largest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
   else:
       return c
print("Task 7:", task7_find_max(5, 9, 3))
def task8_even_or_odd(n):
"""Returns 'Even' if number is even, else 'Odd'."""
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("Task 8:", task8_even_or_odd(7))
def task9_count_vowels(word):
"""Returns number of vowels in a word."""
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
            return count                                                                                                                                            
print("Task 9:", task9_count_vowels("Apple"))    
def task10_multiply_list(numbers):
"""Returns the product of all numbers in a list."""                   
    product = 1        
    for num in numbers:
        product *= num               
        return product                      
print("Task 10:", task10_multiply_list([1, 2, 3, 4]))
def task11_reverse_string(text):
"""Returns the reverse of a string."""                                                                                                                                      return text[::-1]
print("Task 11:", task11_reverse_string("hello"))                                                                                                                       
def task12_factorial(n):                        
"""Returns factorial of n using loop."""
result = 1    
    for i in range(1, n+1):                   
        result *= i                    
       return result                    
print("Task 12:", task12_factorial(5))                                      
def task13_fibonacci(n):                                      
"""Returns first n Fibonacci numbers in a list."""                                              
    seq = []                                              
    a, b = 0, 1                  
    for _ in range(n):                  
    seq.append(a)                  
    a, b = b, a + b               
    return seq              
print("Task 13:", task13_fibonacci(6))
def task14_palindrome(word):                            
"""Checks if word is a palindrome (same forward & backward)."""                                                           
    return word == word[::-1]                             
print("Task 14:", task14_palindrome("madam"))                                             
def task15_simple_interest(principal, rate, time):                                                
"""Calculates simple interest."""                                              
    return (principal * rate * time) / 100                                        
print("Task 15:", task15_simple_interest(1000, 5, 2))                                                                                                          
def task16_compound_interest(principal, rate, time):                                                     
"""Calculates compound interest."""                                                    
    amount = principal * (1 + rate/100) ** time                               
    return amount - principal                             
print("Task 16:", task16_compound_interest(1000, 5, 2))                                                       
def task17_prime_check(n):                                                       
"""Checks if number is prime."""                      
    if n <= 1:
        return False                
    for i in range(2, n):
        if n % i == 0:             
            return False
        else:
            return True
print("Task 17:", task17_prime_check(7))            
def task18_sum_of_list(numbers):                                                                                                                                        """Returns sum of all numbers in a list."""
    total = 0
   for num in numbers:      
       total += num               
       return total                  
print("Task 18:", task18_sum_of_list([1,2,3,4,5]))                                                  
def task19_find_min(numbers):                                                
"""Returns the smallest number in a list."""                        
    smallest = numbers[0]                                        
    for num in numbers:                    
        if num < smallest:              
            smallest = num              
            return smallest                           
print("Task 19:", task19_find_min([4, 7, 1, 9]))                
def task20_multiplication_table(n):                                                
"""Prints multiplication table of n up to 10."""                               
    for i in range(1, 11):                                        
        print(n, "x", i, "=", n*i)                          
        task20_multiplication_table(5)                                      
def task21_average_of_list(numbers):                                      
"""Returns the average of a list of numbers."""                                           
    total = 0                                           
    for num in numbers:
        total += num
        return total / len(numbers)                                   
print("Task 21:", task21_average_of_list([2, 4, 6, 8]))                                            
def task22_count_words(sentence):                                                       
"""Returns the number of words in a sentence."""                
    words = sentence.split()                                            
    return len(words)                     
print("Task 22:", task22_count_words("Python is very easy to learn"))                                                                     
def task23_find_gcd(a, b):                                                                     
"""Returns the greatest common divisor (GCD) of two numbers."""                                                           
    while b != 0:                                                       
        a, b = b, a % b
        return a        
print("Task 23:", task23_find_gcd(36, 60))                                                                                                                                                                                                                                                                                                      def task24_find_lcm(a, b):
"""Returns the least common multiple (LCM) of two numbers."""                                                 
def gcd(x, y)                                                                                                                                                                                                                                                                                                                                      while y != 0:  
   x, y = y, x % y
    return x
  return (a * b) // gcd(a, b)                    
print("Task 24:", task24_find_lcm(4, 6))                                        
def task25_check_anagram(word1, word2):                                        
"""Checks if two words are anagrams of each other."""                                             
   return sorted(word1) == sorted(word2)
def task26_calculate_bmi(weight, height):
    BMI=weight/(height **2)
    return BMI
def task27_discounted_price(price, discount_percent):
    final_price =(100-discount_percent) *price
    return final_price
def task28_movie_ticket_price(age):
    if age<12:
        price =500
    elif age>=12 and age<18:
        price=700
    elif age>=18 and age<60:
        price =1000
    else:
        price =600
    return price
def task29_shopping_total(prices):
    total=0
    for price in prices:
        total+=price
    return total
def task30_convert_to_seconds(hours, minutes, seconds):
    hours *=3600
    minutes *=60
    total=hours +minutes +seconds
    return total
def task31_find_median(numbers):
    if len(numbers)%2==0:
        find=len(numbers)
        output=numbers[find/2]
    else:
        find=len(numbers)
        output=numbers[(find/2)+1]
    return output
def task32_parking_fee(hours):
    if hours<=2:
        fee=200
    else:
        fee= 200+(hours-2)*100
    return fee
def task33_word_count(sentence):
    word_count = len(sentence.split())
    return (word_count)
def task34_capitalize_names(names):
    for name in names:
        name=name.capitalize()
    return name
def task35_student_pass_fail(score):
    if score>=50:
        output="Pass"
    else:
        output="Fail"
    return output
def task36_calculate_fine(days_late):
    if days_late<=5:
        fine=20*days_late
    elif days_late<=10 and days_late>5:
        fine=100+(days_late-5)*50
    else:
        fine=100+250+(days_late-10)*100
    return fine
def task37_convert_currency(amount, rate):
    currency=amount*rate
    return currency
def task38_gas_station_bill(liters, price_per_liter):
    cost = liters*price_per_liter
    return cost
def task39_is_leap_year(year):
    if year%4!=0:
        result=True
    else:
        result=False
    return result
def task40_password_strength(password):
    if len(password)>8 and any(char.isupper() for char in password)==True and any(char.isdigit() for char in password)==True:
        verify= "Strong"
    else:
        verify ="Weak"
    return verify
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    if quantity>=discount_threshold:
        cost=quantity*price_per_shirt*(1-discount_rate)
    else:
        cost=quantity*price_per_shirt
    return cost
def task42_find_mode(numbers):
    import statistics
    value=statistics.mode(numbers)
    return value
def task43_student_average(scores):
    result=sum(scores.values())
    number_results=len(scores.values())
    out=result/number_results
    return out
def task44_calculate_age(current_year, birth_year):
    age=current_year-birth_year
    return age
def task45_salary_after_tax(salary, tax_rate=0.15):
    net=salary*(1-tax_rate)
    return net
def task46_water_bill(units):
    if units<=30:
        bill=50*units
    elif units>30 and units<=50:
        bill=1500+75*(units-50)
    else:
        bill=3000+100*(units-50)
    return bill
def task47_find_longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
def task48_banking_withdraw(balance, withdraw_amount):
    if withdraw_amount<=balance:
        new_balance=balance-withdraw_amount
        final=f"The new balance is {new_balance}"
    else:
        final="Insufficient funds"
    return final
def task49_calculate_grade_point(score):
    if score>=70 and score<=100:
        score=5
    elif score>=60 and score<70:
        score=4
    elif score>=50 and score<60:
        score=3
    elif score>=40 and score<50:
        score=2
    elif score>=30 and score<40:
        score=1
    else:
        score=0
    return score
def task50_weather_advice(temperature, raining):
    if raining:
        send="Take an umbrella"
    elif temperature > 30:
        send= "Wear light clothes"
    elif  temperature < 15:
        send= "Wear a jacket"
    else:
        send="Weather is Fine"
    return send
