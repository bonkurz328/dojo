import random

# 1. Display the Game Introduction:
print("\nWelcome to the Dojo Math Quiz!\n")
print("================================================================================")
print("\nThe Game Designed to Keep Your Mind 🧠 Sharp with Engaging Math Problems.\n")

# 2. Take and Validate the User Input for Name and Surname:
while True:
    full_name = input("Enter Your Full Name (More than 8 Characters): ")
    if full_name and len(full_name) > 8:
        print(f"\nWelcome, {full_name}!")
        break
    else:
        print("Please Enter a Valid Name.")

# 3. Explain the Game Rules and Prompt User to Start:
print("\nThe rules are simple:\n")
print("- You get 3 attempts for the entire level")
print("- Solve 10 math problems correctly to advance")
print("- Each level gets progressively harder\n")
print("Are you ready to get started? (yes/no)\n")

while True:
    start_game = input().strip().lower()
    if start_game in ('yes', 'y'):
        print("\nGreat... Let's Go! 🚀")
        break
    elif start_game in ('no', 'n'):
        print("\nSee you next time! ✌️\n")
        exit()
    else:
        print("Please enter 'yes' or 'no'.")

# 4. Main Game Function with Level Progression
def math_quiz():
    level = 1
    total_attempts = 3  # Total attempts per level (not per question)
    
    while True:  # Level progression loop
        correct_answers = 0
        max_number = 20 + (level * 10)  # Progressive difficulty
        attempts_remaining = total_attempts
        
        print(f"\n⭐ LEVEL {level} (Numbers up to {max_number}) ⭐\n")
        print(f"You have {attempts_remaining} attempts for this level")

        for question_num in range(1, 11):  # 10 questions per level
            # Generate valid math problem
            a = random.randint(1, max_number)
            b = random.randint(1, max_number)
            operator = random.choice(['+', '-', '*', '/'])
            
            # Ensure division problems are clean and valid
            if operator == '/':
                b = max(1, b)  # Prevent division by zero
                a = a * b      # Ensure integer results
            
            # Calculate correct answer
            if operator == '+': correct = a + b
            elif operator == '-': correct = a - b
            elif operator == '*': correct = a * b
            else: correct = a // b
            
            # Present question
            print(f"\nQuestion {question_num}: {a} {operator} {b} = ?")
            
            # Get and validate user answer
            while attempts_remaining > 0:
                try:
                    answer = int(input("Your answer: "))
                    if answer == correct:
                        print("✅ Correct!")
                        correct_answers += 1
                        break
                    else:
                        attempts_remaining -= 1
                        if attempts_remaining > 0:
                            print(f"❌ Incorrect. Attempts left: {attempts_remaining}")
                        else:
                            print("❌ Incorrect. No attempts remaining.")
                except ValueError:
                    print("Please enter a valid integer!")
            
            # Check if level attempts exhausted
            if attempts_remaining == 0:
                print(f"\nThe correct answer was: {correct}")
                break
        
        # Level completion handling
        print(f"\nLevel {level} Results:")
        print(f"Correct Answers: {correct_answers}/10")
        print(f"Attempts Remaining: {attempts_remaining}")
        
        if correct_answers >= 7:
            level += 1
            print("\n🎉 Level Up! The next level will be harder!\n")
            input("Press Enter to continue...")
        else:
            print("\n😟 You need at least 7 correct answers to advance.\n")
            retry = input("Try again? (yes/no): ").lower()
            if retry not in ('yes', 'y'):
                print(f"\nGame Over. You reached Level {level}.\n")
                break

# 5. Start the Game
math_quiz()


