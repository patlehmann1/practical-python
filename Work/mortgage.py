# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

#
# Exercise 1.8
#
principal = 500000.0
months = 0
rate = 0.05
payment = 2684.11
extra_payment = 1000
total_paid = 0.0
modified_payment = payment + extra_payment
  

while principal > 0:
  if months < 12:
    principal = principal * (1+rate/12) - modified_payment
    total_paid = total_paid + modified_payment
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
  months += 1

print('Total paid', total_paid)
print('months', months)

#
# Exercise 1.9
#
principal = 500000.0
months = 0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
modified_payment = payment + extra_payment
  

while principal > payment:
  if months > extra_payment_start_month and months < extra_payment_end_month:
    principal = principal * (1+rate/12) - modified_payment
    total_paid = total_paid + modified_payment
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
  months += 1

print('Total paid', total_paid)
print('months', months)

#
# Exercise 1.10
#
principal = 500000.0
months = 0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
modified_payment = payment + extra_payment

while principal > 0:
  principal = principal * (1+rate/12) - payment
  total_paid = total_paid + payment
  months += 1

  if months > extra_payment_start_month and months < extra_payment_end_month:
    principal = principal * (1+rate/12) - modified_payment
    total_paid = total_paid + modified_payment

  print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', total_paid)
print('months', months)

#
# Exercise 1.11
#
principal = 500000.0
months = 0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
modified_payment = payment + extra_payment

while principal > payment:
  principal = principal * (1+rate/12) - payment
  total_paid = total_paid + payment
  months += 1

  if months > extra_payment_start_month and months < extra_payment_end_month:
    principal = principal * (1+rate/12) - modified_payment
    total_paid = total_paid + modified_payment

  print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', total_paid)
print('months', months)