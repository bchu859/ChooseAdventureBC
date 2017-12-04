import random
from enchant.checker import SpellChecker


def print_repeat(num):
	if num == 1:
		print("Didn't you ask that question already? Anyhow...")
	elif num == 2:
		print("Why are you repeating the same question lol? Geez...")
	elif num == 3:
 		print("Asking the same question again? Alrighty...")


def check_repeat(repeat, index):
	if repeat[index] > 1:
		return True
	else:
		return False


def spell_check(response):
	count = 0
	chkr = SpellChecker("en_US")
	chkr.set_text(response)
	for err in chkr:
		if err:
			count += 1
	return count


# Answers intelligently to the following questions:
# Will I fall in love this year?
# Are any of my friends dating right now?
# Will I ever fall in love?
# Is there such thing as love at first sight?
def rand_love(choice, repeat, index):
    num = int(random.random() * 3) + 1
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)
    rand = int(random.random() * 3) + 1
    if choice == 'i':
        if rand == 1:
            print("Nope, not this year at least.")
        elif rand == 2:
            print("Only if you're really popular and social.")
        else:
            print("Magic 8-Ball would like to inform you that unfortunately you won't.")
    elif choice == 'friends':
        if rand == 1:
            print("Magic 8-Ball knows the latest gossip and says that no one is dating right now.")
        elif rand == 2:
            print("Well, Cosmo and Wanda seem to be getting a lot of attention this week.")
        else:
            print("No, the people in your grade are pretty boring.")
    elif choice == 'ever':
        if rand == 1:
            print("Yes you will, it'll take pretty long though")
        elif rand == 2:
            print("You will fall in love if you stop living in your mom's basement.")
        else:
            print("Magic 8-Ball responds with a definite MAYBE.")
    elif choice == 'sight':
        if rand == 1:
            print("Sure, that doesn't seem far-fetched.")
        elif rand == 2:
            print("Of course! After all, how do people end up falling in love?")
        else:
            print("If people didn't love one another at first sight, how would they even fall in love?")


# Answers questions about the your love life or the love life of your peers
def love_life(response, repeat):
    if 'will' in response and 'i' in response and 'love' in response and 'year' in response:
        rand_love('i', repeat, 4)
    elif 'are' in response and 'friends' in response and 'dating' in response and 'now' in response:
        rand_love('friends', repeat, 5)
    elif 'will' in response and 'i' in response and 'love' in response  or 'ever' in response:
        rand_love('ever', repeat, 6)
    elif 'is' in response and 'love' in response and 'first' in response and 'sight' in response:
        rand_love('sight', repeat, 7)


# Answers intelligently to the following questions:
#   Will i get an 'A' in this class?
#   Will i do good in this class?
#   Is this class hard?
#   Is this class easy?
def rand_grade(choice, repeat, index):
    num = int(random.random() * 3) + 1
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)
    rand = int(random.random() * 3) + 1
    if choice == 'a':
        if rand == 1:
            print("Getting a grade in the excellent range? Magic 8-Ball replies with an absolute YES!")
        elif rand == 2:
            print("A perfect score in the class? Wouldn't that be wonderful. Magic 8-Ball says it's not as hard as you think.")
        else:
            print("Hmmm... getting an 'A'? That's tough, but Magic 8-Ball says it's quite possible!")
    elif choice == 'well':
        if rand == 1:
            print("Based on your mindset this year, the Magic 8-Ball says only if you try your best")
        elif rand == 2:
            print("If you're focused everyday and don't skip class, then definitely!")
        else:
            print("Judging by your performance right now, Magic 8-Ball says its quite possible.")
    elif choice == 'hard':
        if rand == 1:
            print("Is this class very difficult? ")
        elif rand == 2:
            print("Magic 8-Ball says that how hard the class is is different for every individual.")
        else:
            print("Difficulty is in the eye of the beholder.")
    elif choice == 'easy':
        if rand == 1:
            print("Is this class going to be a piece of cake? ")
        elif rand == 2:
            print("Magic 8-Ball cannot assess your academic abilities, so it won't say anything.")
        else:
            print("For some, yes. But most likely not.")


# Answers questions about your grade
def get_a(response, repeat):
	if 'will' in response and 'i' in response and 'get' in response and "an 'a'" in response or 'an a' in response:
		rand_grade('a', repeat, 0)
	elif 'will' in response and 'i' in response and 'do' in response and "good" in response or 'well' in response:
		rand_grade('well', repeat, 1)
	elif 'this' in response and 'class' in response and "hard" in response or "difficult" in response:
		rand_grade('hard', repeat, 2)
	elif 'this' in response and 'class' in response and "easy" in response:
		rand_grade('easy', repeat, 3)


def ai(response, repeat):
    get_a(response, repeat)
    love_life(response, repeat)


def ask():
	roll = int(random.random() * 3) + 1
	if roll == 1:
	    print("Yes!\n")
	elif roll == 2:
	    print("No.\n")
	else:
	    print("Maybe.\n")


def check_input(choice):
    while True:
        response = raw_input().lower()

        if spell_check(response) > 0:
            num = int(random.random() * 3) + 1
            if num == 1:
                print("I didn't understand that. Try again.")
            elif num == 2:
                print("You made a spelling mistake. Please fix your question.")
            else:
                print("You spelled something incorrectly. Please correct your response.")
        else:
            if choice == "again":
                if response == 'yes':
                    return True
                elif response == 'no':
                    return False
                elif response == '':
                    print("You need to enter yes or no!")
                else:
                    print("You need to enter yes or no!")

            elif choice == "question":
                if response == '':
                    print("You need to ask a question!")
                elif '?' not in response:
                    print("Every question ends with a question mark!")
                else:
                    return response


def main():
    repeat = [0] * 7
    print("Welcome to the Magic 8-Ball!")
    answer = True
    while answer:
        print("Ask the 8-Ball a yes or no question and await your response: ")
        ai(check_input("question"), repeat)
        ask()
        print("Would you like to ask another question?")
        answer = check_input("again")

    print("Thanks for coming by!")


main()