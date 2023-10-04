# # NAMES: JUAN GARCIA, MIA JUAREZ, DIEGO FONSECA
question1 = input("Please insert a text: ")
fixedq1 = question1.lower()
print(f"Please enter a random lowercase letter for each of the following questions")
q1 = input("Please insert a random letter ")
q2 = input("Please insert another random letter ")
q3 = input("Please insert another random letter ")

instanceq1 = fixedq1.count(str(q1))
instanceq2 = fixedq1.count(str(q2))
instanceq3 = fixedq1.count(str(q3))
print(f"The letter {q1} has appeared {instanceq1} times")
print(f"The letter {q2} has appeared {instanceq2} times")
print(f"The letter {q3} has appeared {instanceq3} times")

letCount = len(fixedq1)
print(f"There are {letCount} letters in your text")

li = list(fixedq1.split(" "))
numWords = len(li)
print(f"There are {numWords} words in your text.")



first = fixedq1[0]
last = fixedq1[-1]
print(f"The first letter in your text is {first}")
print(f"The last letter in your text is {last}")


reverse1 = fixedq1.split()
reverse1.reverse()
final = " ".join(reverse1)
convertFinal = str(final)

print(f"Your text in reverse is {convertFinal}")

istherep = "python" in fixedq1
print(f"Is python in the text: {istherep}")
# print(f"Is python in the text: {boolean goes here}")

























