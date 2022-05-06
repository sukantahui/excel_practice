import secrets
import string
import pandas as pd
from faker import Faker
Faker.seed(42)

fake = Faker(locale='en_IN')
students = [
    {'student_id': '',
     'first_name': fake.first_name(),
     'last_name': fake.last_name(),
     'dob': fake.date_between(start_date='-16y', end_date='-15y'),
     'phone': fake.phone_number(),
     'state': fake.random_element(elements=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh (UT)','Chhattisgarh','Dadra and Nagar Haveli (UT)','Daman and Diu (UT)','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep (UT)','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Puducherry (UT)','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']),
     'region': fake.random_element(elements=['North', 'East','South','West','North East','South East']),
     'beng': fake.random_number(digits=2, fix_len=2),
     'eng': fake.random_number(digits=2, fix_len=2),
     'math': fake.random_number(digits=2, fix_len=2),
     'phy': fake.random_number(digits=2, fix_len=2),
     'chem': fake.random_number(digits=2, fix_len=2),
     'comp': fake.random_number(digits=2, fix_len=2)
    }
    for x in range(5000)]

df = pd.DataFrame(students)
df['student_id'] = range(1001,6001)
df.to_csv('student_marksheet.csv', index=False)
