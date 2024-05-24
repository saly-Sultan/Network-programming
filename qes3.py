import csv

try:
    with open('my_qes.csv') as file:
        reader = csv.reader(file)
        questions = []
        answers = []
        for row in reader:
            questions.append(row[0])
            answers.append(row[1])
except FileNotFoundError:
    print("The file 'my_qes.csv' was not found.")
    exit()
except IndexError:
    print("There was an error reading the 'my_qes.csv'. Please check the file format.")
    exit()

name = input("Write Your name: ")

count = 0

for i in range(len(questions)):
    answer = input(questions[i] + " ")
    if answer.lower() == answers[i].lower():
        print("correct")
        count += 1
    else:
        print("Incorrect answer !")

print("YOU got :", count)

try:
    with open('my_ans.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([name, count])
except Exception as e:
    print(f"An error occurred while writing to 'my_ans.csv': {e}")
