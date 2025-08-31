#26
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
