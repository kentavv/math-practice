#!/usr/bin/python3

import random
import time
from datetime import datetime
import os
import sys
import pickle
import readline


fn = 'math_practice.pkl'
# delay = 2
ntries = 3
n_problems = 64
with_replacement = False


def clear_screen():
    os.system('clear')


def gen_problems(n):
    all_probs = []
    for a in range(15):
        for b in range(15):
            op = '+'
            c = a + b
            all_probs += [(a, op, b, c)]

    if with_replacement:
        probs = random.choices(all_probs, k=n)
    else:
        n = min(n, len(all_probs))
        probs = random.sample(all_probs, k=n)

    return probs


def present_problem(i, prob, lst2, dt0):
    clear_screen()

    a, op, b, c = prob

    # print(f'{i+1:3d} of {n:3d}   {str(datetime.now() - dt0).rsplit(".", 1)[0]}\n\n')
    # print(f'{i+1:3d} of {n:3d}\n\n')

    tally_len = 4
    s = f'  {a:2d}\n{op} {b:2d}\n{"-" * tally_len}'

    print(s)

    c2 = -1

    attempts = []
    dt1 = datetime.now()
    t0 = time.time()
    correct = False
    i2 = 0
    for i2 in range(ntries):
        while True:
            try:
                c2 = input(' ' * (tally_len - len(str(c)))).strip()
                c2 = int(c2)
            except ValueError:
                print('Please enter an integer')
            except EOFError:
                print()
                sys.exit(1)
            else:
                break

        attempts += [c2]

        if c == c2:
            correct = True
            break
        else:
            if i2 < ntries - 1:
                print('Try again...')
            else:
                print()
                print(f'Correct answer is: {a} + {b} = {c}')
                print('\nWill do better next time!')
                break

    t1 = time.time()

    row = {'test_start':    dt0,
           'problem_start': dt1,
           'problem_index': i,
           'problem_count': n_problems,
           'n_attempts':    i2,
           'problem':       prob,
           'correct':       correct,
           'attempts':      attempts,
           'problem_time':  t1 - t0}
    lst2 += [row]

    if correct:
        ct = row['problem_time']
        m = [x['problem_time'] for x in lst2 if x['test_start'] == dt0]
        avg = sum(m) / len(m)
        print()
        print(f'Correct!\n\nTime: {(ct):.3f}\nAvg:  {avg:.3f}')
        try:
            if ct < min(m[:-1]):
                print('\nNew best time!')
        except ValueError:
            pass
        

    readline.clear_history()
    print()
    print(f'  {i+1} of {n_problems} Done!\n')
    print('Press Enter to continue...')
    s2 = input()
    #time.sleep(delay)
    readline.clear_history()


def get_quote():
    lst = [
            'Try and fail, but never fail to try! - Jared Leto',
            'The only failure is not trying. — Robin S. Sharma',
            'If I fail, I try again, and again, and again. — Nick Vujicic',
            'Set your target and keep trying until you reach it. — Napoleon Hill',
            'Do or do not. There is no try. Only do. — Frank Oz',
            'Most people can learn a lot more than they think they can. They sell themselves short without trying. — Elon Musk',
            'Don’t be afraid to fail. Be afraid not to try. — Michael Jordan',
            'Don’t bother people for help without first trying to solve the problem yourself. — Colin Powell',
            'Before you react, think. Before you spend, earn. Before you criticize, wait. Before you quit, try. — William Arthur Ward',

            # 'Don’t bother just to be better than others. Try to be better than yourself. — William Faulkner',
            # 'Don’t waste your energy trying to convince people to understand you. Your time is too valuable to try to prove yourself to people. — Joel Osteen',
            # 'The less you try to impress, the more impressive you are. — Denis Waitley',
            # 'I’ve always been a fighter. If you tell me I can’t, I’ll die trying to prove you wrong. — R.A. Salvatore',
            # 'Trying to get everyone to like you is a sign of mediocrity. — Colin Powell',
            # 'What I’m trying to do is to maximise the probability of the future being better. - Elon Musk',
            # 'We will all fail in life, but nobody has to be a failure. Failing at a thing doesn’t make you a failure. You are only a failure when you quit trying. — Joyce Meyer',
            # 'I know fear is an obstacle for some people, but it is an illusion to me. Failure always made me try harder next time. — Michael Jordan',
            # 'Try not to resist the changes that come your way. Instead let life live through you. And do not worry that your life is turning upside down. How do you know that the side you are used to is better than the one to come? — Rumi',
            # 'Until we have met the monsters in ourselves, we keep trying to slay them in the outer world. And we find that we cannot. For all darkness in the world stems from darkness in the heart. And it is there that we must do our work. — Marianne Williamson',
            # 'Remember, don’t try to build the greatest wall that’s ever been built. Focus on laying a single, expertly-placed brick. Then keep doing that, every day. — Will Smith',
            # 'You’ve got to start with the customer experience and work backwards to the technology. You can’t start with the technology and try to figure out where you’re going to sell it. — Steve Jobs',
            # 'Life is about trying things to see if they work. — Ray Bradbury',
            # 'Hurrying and delaying are alike ways of trying to resist the present. — Alan Watts',
            # 'If you’re going to try, go all the way. Otherwise, don’t even start. — Charles Bukowski',
            # 'Take the probability of loss times the amount of possible loss from the probability of gain times the amount of possible gain. That is what we’re trying to do. It’s imperfect, but that’s what it’s all about. — Warren Buffett',
            # 'Breathe and don’t try to be perfect. — Nicole Kidman',
            # 'Just don’t give up trying to do what you really want to do. — Ella Fitzgerald',
            # 'The more you are like yourself, the less you are like anyone else which makes you unique. The problem with most people is that they spend their lives trying to emulate others and so we have lots of copies but few originals. — Walt Disney',
            # 'If you are going to try, go all the way or don’t even start. If you follow it you will be alive with the gods. It is the only good fight there is. — Charles Bukowski',
            # 'All too often, the security of a mediocre present is more comfortable than the adventure of trying to be more in the future. — Tony Robbins',
            # 'Try to imagine what it will be like to go to sleep and never wake up. Now try to imagine what it was like to wake up having never gone to sleep. — Alan Watts',
            # 'I try to buy stock in businesses that are so wonderful that an idiot can run them. Because sooner or later, one will. — Warren Buffett',
            # 'Most people try to get rich by being cheap and the price for that is that you live cheap and there is so much money out there; why would you want to live cheap? — Robert T. Kiyosaki',
            # 'Now I know who you are U got nothin’ on me, I see I should’ve known it from the start You can’t tell me lies Don’t even try cuz This is goodbye Goodbye. — Demi Lovato',
            # 'We are not an endangered species ourselves yet, but this is not for lack of trying. — Douglas Adams',
            # 'Writers aren’t people exactly. Or, if they’re any good, they’re a whole lot of people trying so hard to be one person. — F. Scott Fitzgerald',
            # 'Prosperity tries the fortunate, adversity the great. — Rose Kennedy',
            # 'We can do all things through Christ who strengthens us, but frankly we won’t if we’re too afraid to try. — Beth Moore',
            # 'Here I am alive, and it’s not my fault, so I have to try and get by as best I can without hurting anybody until death takes over. — Leo Tolstoy',
            # 'We should try to hold on to the Christmas spirit, not just one day a year, but all 365. — Mary Martin'
            ]
    return lst[random.randrange(len(lst))]


def final_screen(lst2, dt0, n):
    clear_screen()
    print('Be proud of your work!\n')

    lst2 = [x for x in lst2 if x['test_start'] == dt0]

    ncorrect = len([x for x in lst2 if x['correct']])
    print(f'  {ncorrect} of {n} correct!')
    print()
    print(f'Total time: {str(datetime.now() - dt0).split(".")[0]}')
    print()
    m = [x['problem_time'] for x in lst2 if x['correct']]
    if m:
        print(f'Fastest correct: {min(m):.3f}')
        print(f'Average correct: {sum(m) / len(m):.3f}')
        print(f'Slowest correct: {max(m):.3f}')
        print()
    m = [x['problem_time'] for x in lst2]
    if m:
        print(f'Fastest overall: {min(m):.3f}')
        print(f'Average overall: {sum(m) / len(m):.3f}')
        print(f'Slowest overall: {max(m):.3f}')
        print()

    # Problems requiring more than one attempt
    a = [x['problem'] for x in lst2 if len(x['attempts']) > 1][:5]

    # Incorrect problems
    b = [x['problem'] for x in lst2 if not x['correct']][:5]

    # The top X problems requiring the most time.
    c = [x['problem'] for x in sorted(lst2, key=lambda x:x['problem_time'], reverse=True)][:5]

    # Like the previous, but only for correct problems
    # [(x['problem'], x['problem_time']) for x in sorted([x for x in lst if x['correct']], key=lambda x:x['problem_time'], reverse=True)][:5]

    # The top X problems requiring the least time.
    # [(x['problem'], x['problem_time']) for x in sorted(lst, key=lambda x:x['problem_time'], reverse=False)][:5]

    d = []
    for x in a + b + c:
        if x not in d:
            d += [x]

    if d:
        print()
        print('Please review:')
        for x in d:
            a, op, b, c = x
            print(f'{a:3d} {op} {b:3d} = ................. {c:3d}')


    # for row in lst2:
    #     print(row)

    print()
    print(get_quote())
    print()


def restore_state():
    try:
        lst2 = pickle.load(open(fn, 'rb'))
    except (FileNotFoundError, EOFError):
        lst2 = []
    return lst2


def save_state():
    pickle.dump(lst2, open(fn, 'wb'))


def repeat_hard_problems(probs, lst):
    # Problems requiring more than one attempt
    a = [x['problem'] for x in lst if len(x['attempts']) > 1][:5]

    # The top X problems requiring the most time.
    b = [x['problem'] for x in sorted(lst, key=lambda x:x['problem_time'], reverse=True)][:5]

    # Like the previous, but only for correct problems
    # c = [x['problem'] for x in sorted([x for x in lst if x['correct']], key=lambda x:x['problem_time'], reverse=True)][:5]

    # The top X problems requiring the least time.
    d = [x['problem'] for x in sorted(lst, key=lambda x:x['problem_time'], reverse=False)][:5]

    np = a + b + d
    np = [x for x in np if x not in probs]
    print(f'Restored {len(np)} problems')
    probs = np + probs
    probs = probs[:n_problems]

    random.shuffle(probs)
    # print(f'Total {len(probs)} problems')

    return probs


if __name__ == '__main__':
    clear_screen()

    lst2 = restore_state()

    probs = gen_problems(n_problems)

    probs = repeat_hard_problems(probs, lst2)

    print(f'{len(probs)} problems generated!')
    # print('Get ready!')
    print('You\'re going to do great!')
    print('Press Enter to start!')
    input()
    readline.clear_history()

    dt0 = datetime.now()

    for i, prob in enumerate(probs):
        present_problem(i, prob, lst2, dt0)
        save_state()

    final_screen(lst2, dt0, n_problems)

