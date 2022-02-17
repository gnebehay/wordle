import random
import string


def check_incorrect_characters(candidate, incorrect_characters):

    for incorrect_character in incorrect_characters:
        if incorrect_character in candidate:
            return False

    return True


def check_correct_position(candidate, word, correct_positions):

    for i, correct_position in enumerate(correct_positions):
        if correct_position and candidate[i] != word[i]:
            return False

    return True


def check_incorrect_position(candidate, incorrect_positions):

    for i, c in enumerate(candidate):
        if i in incorrect_positions[c]:
            return False

    return True


def check_correct_characters(candidate, correct_characters):

    for correct_character in correct_characters:
        if correct_character not in candidate:
            return False

    return True


with open('words.txt') as f:
    words = f.read().splitlines()

with open('tests.txt') as f:
    candidates = f.read().splitlines()

candidates = words + candidates

# pick a random word
i = random.randint(0, len(words))
word = words[i]

correct_characters = set()
incorrect_characters = set()
correct_positions = [False]*5
incorrect_positions = {c: set() for c in string.ascii_lowercase}
used_tests = set()

for attempt in range(6):

    i = random.randint(0, len(candidates)-1)
    test = candidates[i]
    used_tests.add(test)

    print(f'Test word: {test}')

    if test == word:
        print(f'Found the wordle on try #{attempt}')
        break

    # Compare the two
    correct_characters = correct_characters.union(set(word).intersection(set(test)))
    print(f'Correct characters: {correct_characters}')

    incorrect_characters = incorrect_characters.union(set(test).difference(set(word)))
    print(f'Incorrect characters: {incorrect_characters}')

    correct_positions = [w == t or correct_position for w, t, correct_position in zip(word, test, correct_positions)]
    print(f'Correct positions: {correct_positions}')

    for i, correct_position in enumerate(correct_positions):
        if test[i] in correct_characters and not correct_position:
            incorrect_positions[test[i]].add(i)

    print(f'Incorrect positions: {incorrect_positions}')

    # To select the next word, we retrieve all words that satisfy all conditions
    old_candidates = candidates
    candidates = []
    for candidate in old_candidates:

        if candidate in used_tests:
            continue

        if not check_incorrect_characters(candidate, incorrect_characters):
            continue

        if not check_correct_position(candidate, word, correct_positions):
            continue

        if not check_incorrect_position(candidate, incorrect_positions):
            continue

        if not check_correct_characters(candidate, correct_characters):
            continue

        candidates.append(candidate)

    print(f'candidates: {len(candidates)}')
    print()
else:
    print("Couldn't find the wordle")



