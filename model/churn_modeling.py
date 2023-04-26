#first you need to install keras in your machine
# pip install keras

from keras.models import Sequential, load_model

# Load the saved model back into memory
loaded_model = load_model('churn_modeling.h5')

# Get input values
customer_id = input("Enter customer ID: ")
surname = input("Enter surname: ")
credit_score = int(input("Enter credit score: "))
geography = input("Enter geography (France, Spain, Germany):")
gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))
tenure = int(input("Enter tenure: "))
balance = float(input("Enter balance: "))
num_of_products = int(input("Enter number of products: "))
has_cr_card = int(input("Enter has credit card (1 for yes, 0 for no): "))
is_active_member = int(input("Enter is active member (1 for yes, 0 for no): "))
estimated_salary = float(input("Enter estimated salary: "))

#covert to the numbers.
if gender == 'M':
    gender_model = 0

else:
    gender_model = 1

#convert the geography
if geography == 'France':
    geography_model = 0
elif geography == 'Spain':
    geography_model = 1
else:
    geography_model = 2


# Use the loaded model to make predictions on new data
pred = [[credit_score,geography_model,gender_model,age,tenure,balance,num_of_products,has_cr_card,is_active_member,estimated_salary]]
predictions = loaded_model.predict(pred)

print("\n")

if predictions < 0.5:
    print(f"{surname} won't cancel his or her account in the near future.")
else:
    print(f"{surname} will cancel his or her account in the near future.")



