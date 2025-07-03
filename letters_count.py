
#user_input = "numentica ui internship"
user_input = input("Enter the sentence: ")
sentence = user_input.split()
count = 0

for i in sentence:      #numentica
    for j in i: 
        count += 1
print("There are ", count, "letters")