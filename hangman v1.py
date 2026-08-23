import random as r
choices = ['japan', 'iraq', 'iran', 'russia']
answer = r.choice(choices)
hidden_answer = ['_'] * len(answer)
str_answer = ' '.join(hidden_answer)
attempts = 3
print('<=S=(GUESS)=S=>\n')
print(f'=S=( {str_answer} )=S=({attempts})=>')
guess = None
recent_guesses = []
while attempts > 0 and '_' in hidden_answer:
    guess = input('Guess a character: ').lower().strip()
    if not guess.isalpha():
        print('characters please.')
        continue

    if len(guess) != 1:
        print('ONE character at a time.')
        continue

    if guess in recent_guesses:
        print('do not repeat a character.')
        continue
    else:
        recent_guesses.append(guess)

    if guess in answer:
        print('TRUE!')
    else:
        attempts -= 1
        print(f'FALSE!\nYou lost 1 attempt')
        if attempts == 1:
            print('YOU HAVE 1 ATTEMPT REMAINING!\n')

    for i in range(len(answer)):
        if guess == answer[i]:
            hidden_answer[i] = guess
            str_javab = ' '.join(hidden_answer)
            print(f'<=S=( {str_javab} )=S=({attempts})=>\n')


if not attempts > 0:
    print(f'your attempts: {attempts}\nYOU LOST!')

if not '_' in hidden_answer:
    print('Congrajulations, you win!')
    print(f'Answer is: {answer}')
