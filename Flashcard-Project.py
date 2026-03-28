def enumeration():

    # Input Number of Questions
    maxQA = int(input("Number of Questions to be inputted: "))

    # Input the Question and Answers
    questions = [] 
    answers = []
    for i in range(maxQA):
        questions.append(input("\nState the Definition: "))
        answers.append(input("State the Answer: "))

    # Flashcard Game
    while True:
        score = 0
        for i in range(maxQA):
            print("\n" + questions[i])
            answer = input("Answer: ")
            if answer == answers[i]:
                score += 1
    
        print("Score:", str(score) + "/" + str(maxQA))
        restart = input("Try Again? (Y/N) ")
        if restart.upper() == "N":
            break

def multipleChoice():

    # Input Number of Questions
    maxQA = int(input("Number of Questions to be inputted: "))

    # Input the Question and Answers
    questions = [] 
    A = []
    B = []
    C = []
    D = []
    answers = []
    for i in range(maxQA):
        questions.append(input("\nState the Definition: "))
        A.append(input("A: "))
        B.append(input("B: "))
        C.append(input("C: "))
        D.append(input("D: "))
    
        while True:
            correctAnswer = input("State the Answer: ")
            if correctAnswer == "A" or correctAnswer == "B" or correctAnswer == "C" or correctAnswer == "D":
                answers.append(correctAnswer)
                break
            else: 
                print("Invalid Answer!")

    # Flashcard Game
    while True:
        score = 0
        for i in range(maxQA):
            print("\n" + questions[i])
            print("A.", A[i])
            print("B.", B[i])
            print("C.", C[i])
            print("D.", D[i])
        
            answer = input("Answer: ").upper()
            if answer == answers[i]:
                score += 1
    
        print("Score:", str(score) + "/" + str(maxQA))
        restart = input("Try Again? (Y/N) ")
        if restart.upper() == "N":
             break

# Main code
while True:
    print("1. Enumeration")
    print("2. Multiple Choice")
    print("3. Exit")
    option = int(input("\nSelect an Option (1,2,3): "))

    match option:   # swtich case
        case 1:
            enumeration()
            break
        case 2:
            multipleChoice()
            break
        case 3:
            break
        case _:     # default
            print("Invalid Option!\n")