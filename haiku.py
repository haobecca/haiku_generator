from count_syllables import count_syllables

# Load a training-corpus text file
with open('train.txt', 'r') as f:
    train = f.read()

#Process the training corpus for spaces, newline breaks, and so on
train_list = train.split()


# TODO try default dict?

# Map each word in corpus to the word after (Markov model order 1)
train_dict_o1 = dict()
# Map each word pair in corpus to the word after (Markov model order 2)
train_dict_o2 = dict()

for first, second, third in zip(train_list, train_list[1:], train_list[2:]):
    if first in train_dict_o1:
        train_dict_o1[first].append(second)
    else:
        train_dict_o1[first] = [second]
    if (first, second) in train_dict_o2:
        train_dict_o2[first, second].append(third)
    else:
        train_dict_o2[first, second] = [third]

# Give user choice of generating full haiku, redoing lines 2 or 3, or exiting
full_haiku = [['1'], ['2'], ['3']]
line_1 = full_haiku[0]
line_2 = full_haiku[1]
line_3 = full_haiku[2]

s = input('Enter "full" to generate full haiku. Enter "redo 2" to regenerate line 2. Enter "redo 3" to regenerate line 3:  ')

print(full_haiku)

"""
If first line:
    Target syllables = 5
    Get random word from corpus <= 4 syllables (no 1-word lines)
    Add word to line
    Set random word = prefix variable
    Get mapped words after prefix
    If mapped words have too many syllables
        Choose new prefix word at random & repeat
    Choose new word at random from mapped words
    Add the new word to the line
    Count syllables in word and calculate total in line
    If syllables in line equal target syllables
        Return line and last word pair in line
Else if second or third line:
    Target = 7 or 5
    Line equals last word pair in previous line
    While syllable target not reached:
        Prefix = last word pair in line
        Get mapped words after word-pair prefix
        If mapped words have too many syllables
            Choose new word-pair prefix at random and repeat
        Choose new word at random from mapped words
        Add the new word to the line
        Count syllables in word and calculate total in line
        If total is greater than target
            Discard word, reset total, and repeat
        Else if total is less than target
            Add word to line, keep total, and repeat
        Else if total is equal to target
           Add word to line
    Return line and last word pair in line
Display results and choice menu
"""