import pickle

lst = pickle.load(open('math_practice.pkl', 'rb'))

# >>> lst[0]
# {'test_start': datetime.datetime(2023, 8, 26, 17, 31, 44, 187424), 'problem_start': datetime.datetime(2023, 8, 26, 17, 31, 44, 189884), 'problem_index': 0, 'problem_count': 64, 'n_attempts': 0, 'problem': (11, '+', 10, 21), 'correct': True, 'attempts': [21], 'problem_time': 1.6339824199676514}

# Problems requiring more than one attempt
[x['problem'] for x in lst if len(x['attempts']) > 1]

# Incorrect problems
[x for x in lst if not x['correct']]

# The top X problems requiring the most time.
[(x['problem'], x['problem_time']) for x in sorted(lst, key=lambda x:x['problem_time'], reverse=True)][:5]

# Like the previous, but only for correct problems
[(x['problem'], x['problem_time']) for x in sorted([x for x in lst if x['correct']], key=lambda x:x['problem_time'], reverse=True)][:5]

# The top X problems requiring the least time.
[(x['problem'], x['problem_time']) for x in sorted(lst, key=lambda x:x['problem_time'], reverse=False)][:5]



# Find range and histogram of times
import numpy as np
tms = sorted([x['problem_time'] for x in lst])
np.min(tms), np.mean(tms), np.median(tms), np.max(tms)
np.histogram(tms)

