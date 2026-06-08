# Step 1 — Print a welcome header
# Step 2 — Store 5 questions with multiple choice answers
# Step 3 — Loop through each question using a "for" loop
# Step 4 — Check answers and track score
# Step 5 — Display final score with a performance message
# Step 6 — Ask to play again using a while loop

print("=" * 30)
print("         Hi, student,\n   Welcome to my quiz game!")
print("=" * 30)

questions = [
    {
        "question": "1. What is the primary purpose of qualitative research?",
     "choices": [
        "A. To collect numerical data",
        "B. To explore and understand human behavior and experiences",
        "C. To conduct experiments",
        "D. To analyze statistics"
    ],
    "answer": "B"
    },
    
    {
        "question": "2. Which of the following is a common qualitative research method?",
     "choices": [
        "A. Interview",
        "B. Sorting",
        "C. Experiments",
        "D. Measurements" 
    ],
    "answer": "A"
    },

    {
        "question": "3. What type of data does qualitative research primarily collect?",
     "choices": [
        "A. Statistical data",
        "B. Written data",
        "C. Non-numerical data",
        "D. Mobile data"
    ],
    "answer": "C"
    },

    {
        "question": "4. Which approach involves studying people in their natural environment?", 
     "choices": [
        "A. Telegraphy",
        "B. Geography",
        "C. Ethnography",
        "D. Demography"
    ],
    "answer": "C"
    },

    {
        "question": "5. What is the term for the researcher's awareness of their own influence on the research process?",
     "choices": [
        "A. Perplexity",
        "B. Relevance",
        "C. Sensitivity",
        "D. Reflexivity"
    ], 
    "answer": "D"
    },
] 

score = 0
while True:
    for question in questions:
        print(question["question"])
        print("") # cleared
        for choice in question["choices"]:
            print(choice)
        print("")
        print("=" * 40)
        answer = input("What is the right answer: ")
        if answer.upper() == question["answer"]:
            score += 1
            print("That is correct!")
        else:
            print(f"Incorrect, the right answer is {question['answer']}")
            print("")

    print(f"Your final score is {score}/5")
    if score == 5:
        print("Perfect score!")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep studying!")

    
    retry = input("Would you like to try again?\n")
    if retry.upper() == "YES":
            score = 0
            continue
    else:
        break

