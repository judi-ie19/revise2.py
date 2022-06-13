Dog={"name":"Bruno","color":"black","breed":"german shepherd","legs":4,"age":"10yrs"}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={"first_name":"Judy","last_name":"Akinyi","gender":"female","age":"21","marital status":"married","skills":"coding","country":"kenya","city":"Nairobi","address":"616 korongo road"}
# Get the length of the student dictionary
print(len(student))
print(student["skills"])
print(type(["skills"]))

# Modify the skills values by adding one or two skills
student["skills"]="art","communication"
print(student["skills"])
print(list(student))
print(student.keys())
print(student.values())
print(list(student.items()))
print(student.pop("first_name"))
print(student)

