import pickle

lst = pickle.load(open('math_practice.pkl', 'rb'))

# >>> lst[0]
# {'test_start': datetime.datetime(2023, 8, 26, 17, 31, 44, 187424), 'problem_start': datetime.datetime(2023, 8, 26, 17, 31, 44, 189884), 'problem_index': 0, 'problem_count': 64, 'n_attempts': 0, 'problem': (11, '+', 10, 21), 'correct': True, 'attempts': [21], 'problem_time': 1.6339824199676514}

# Problems requiring more than one attempt
[x['problem'] for x in lst if len(x['attempts']) > 1]

for x in [x for x in lst if len(x['attempts']) > 1]:
    print(x['test_start'].date(), '%.1f' % x['problem_time'], x['correct'], x['attempts'], '%s %s %s = %s' % x['problem'])


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
# np.histogram(tms)
np.histogram(tms, bins=[0, 5, 10, 15, 20, 40, 60, 120, int(np.ceil(np.max(tms)))])


for x in [x for x in sorted(lst, key=lambda x:x['problem_time'], reverse=True)][:40]:
    print(x['test_start'].date(), '%.1f' % x['problem_time'], x['correct'], x['attempts'], '%s %s %s = %s' % x['problem'])



d = {}
for x in lst:
    p = x['problem']
    if p not in d:
        d[p] = []
    d[p] += [x['problem_time']]
ll = []
for k,v in d.items():
    ll += [('%3d %s %3d = %3d' % k, len(v), np.min(v), np.max(v), np.max(v) - np.min(v), np.mean(v), np.median(v))]

import pandas as pd
df = pd.DataFrame(ll, columns=['problem', 'n_seen', 'min', 'max', 'range', 'mean', 'median'])

pd.set_option('display.max_rows', None)
pd.set_options('display.float_format', '{:.2f}'.format)

df2 = df.sort_values(by=['n_seen', 'median'], ascending=[False, False])
print(df2.to_string(index=False))

df2 = df[df['n_seen'] > 1].sort_values(by=['median'], ascending=[False])
print(df2.to_string(index=False))

