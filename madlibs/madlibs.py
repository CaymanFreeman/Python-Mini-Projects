import re

print('''\nWelcome to Mad Libs!

Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price. 
It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud.
The game is frequently played as a party game or as a pastime.
The current story templates are AI generated.

Story Templates:
[1] Monster in the Woods (Short)
[2] Animal Comedy (Short)
[3] Quest for the Kingdom (Long)
[4] An Unexpected Friend (Short)
[5] Rival Gangsters (Short)
''')

story = -1
while True:
    story = input("Choose a story (1 to 5): ")
    if story.isdigit():
        story = int(story)
        if 1 <= story <= 5:
            break
        else:
            print("\nYou must choose a number from 1 to 5")
    else:
        print("\nInvalid input, please enter a whole positive number.")


def switch(num):
    if num == 1:
        return "monster_in_the_woods"
    elif num == 2:
        return "animal_comedy"
    elif num == 3:
        return "quest_for_the_kingdom"
    elif num == 4:
        return "unexpected_friend"
    elif num == 5:
        return "rival_gangsters"


print()

with open(switch(story) + ".txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    word_formatted = re.sub(r'\d+', '', word).strip('<>')

    if '/s' in word:
        plurality = 'singular'
        word_formatted = word_formatted.replace('/s', '')
    elif '/p' in word:
        plurality = 'plural'
        word_formatted = word_formatted.replace('/p', '')
    else:
        plurality = ''

    if '/ing' in word:
        tense = '(ing)'
        word_formatted = word_formatted.replace('/ing', '')
    elif '/ed' in word:
        tense = '(ed)'
        word_formatted = word_formatted.replace('/ed', '')
    else:
        tense = ''

    if word_formatted[0].lower() in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    if plurality and tense:
        article = 'a'
        prompt = f"Enter {article} {plurality} {word_formatted} {tense}: "
    elif plurality and not tense:
        article = 'a'
        prompt = f"Enter {article} {plurality} {word_formatted}: "
    elif tense and not plurality:
        prompt = f"Enter {article} {word_formatted} {tense}: "
    else:
        prompt = f"Enter {article} {word_formatted}: "
    answer = input(prompt)
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("\nHere is your story:\n\n" + story)
