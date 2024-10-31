# To extract testing questions 

file_names = ["./test1.txt", "./test2.txt", "./test3.txt"]

''' Test 1 (Week 3)'''

test1_prompts = []
test1_answers = []
test1_file = "./test1.txt"
with open(test1_file, "r") as file:
    content = file.readlines()
    prompts = ""
    answers = ""
    for sentence in content:
        if sentence.startswith("Q") or sentence.startswith("S"):
            if answers != "":
                test1_prompts.append(prompts)
                prompts = ""
                test1_answers.append(answers)
                answers = ""
            prompts += (sentence[2:] + "\n")
        elif sentence.startswith("A"):
            answers += (sentence[2:] + "\n")
    if answers and sentence: 
        test1_prompts.append(prompts)
        test1_answers.append(answers)

# print(len(test1_prompts))
# print(len(test1_answers))

# for i in range(len(test1_prompts)):
#     print("Prompts: ", test1_prompts[i])
#     print("Answers: ", test1_answers[i])
#     print("----------------------------------------------------")

''' Test 2 (Week 4) '''

test2_prompts = []
test2_answers = []
test2_file = "./test2.txt"
with open(test2_file, "r") as file:
    content = file.readlines()
    prompts = ""
    answers = ""
    for sentence in content:
        if sentence.startswith("Q") or sentence.startswith("S"):
            if answers != "":
                test2_prompts.append(prompts)
                prompts = ""
                test2_answers.append(answers)
                answers = ""
            prompts += (sentence[2:] + "\n")
        elif sentence.startswith("A"):
            answers += (sentence[2:] + "\n")
    if answers and sentence: 
        test2_prompts.append(prompts)
        test2_answers.append(answers)

# for i in range(len(test2_prompts)):
#     print("Prompts: ", test2_prompts[i])
#     print("Answers: ", test2_answers[i])
#     print("----------------------------------------------------")

''' Test 3  (Week 5) '''
test3_prompts = []
test3_answers = []
test3_file = "./test3.txt"
with open(test3_file, "r") as file:
    content = file.readlines()
    prompts = ""
    answers = ""
    for sentence in content:
        if sentence.startswith("Q") or sentence.startswith("S"):
            if answers != "":
                test3_prompts.append(prompts)
                prompts = ""
                test3_answers.append(answers)
                answers = ""
            prompts += (sentence[2:] + "\n")
        elif sentence.startswith("A"):
            answers += (sentence[2:] + "\n")
    if answers and sentence: 
        test3_prompts.append(prompts)
        test3_answers.append(answers)

for i in range(len(test3_prompts)):
    print("Prompts: ", test3_prompts[i])
    print("Answers: ", test3_answers[i])
    print("----------------------------------------------------")