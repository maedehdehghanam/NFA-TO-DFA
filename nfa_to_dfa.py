from tabulate import tabulate
m,n,s,q= input().split();
final_states =[];
i =1;
for x in range(0,int(n)):
	k = input()
	if k=='1':
		final_states.append(i);
	i = i+1;


initial_states = []
for x in range(0,int(s)):
	k = input()
	initial_states.append(k)

language_alphabets=[];
ways = []
for x in range(0,int(m)):
	alphabet, s1, s2 = input().split()
	if alphabet not in language_alphabets:
		language_alphabets.append(alphabet);
	ways.append(alphabet + " "+ s1+ " "+ s2);

"""
calculating epsilon closure
"""
def epsilon_closureـrecursive(state):
	ec = set();
	for x in range(0,len(ways)):
		if ways[x].split()[0] == '-' and ways[x].split()[1] == state:
			ec.add(ways[x].split()[2]);
	ecr= set();
	if len(ec)>0:
		for x in ec:
			ecr = ecr.union(epsilon_closureـrecursive(x));
	return ecr.union(ec);
def epsilon_closure(state):
	ec = (epsilon_closureـrecursive(state))
	ec.add(state)
	return ec;
"""
calculating delta
"""
def delta_calculator(state, alphabet):
	delta = set()
	for x in ways:
		if x.split()[0] == alphabet and x.split()[1] == state:
			delta.add(x.split()[2])
	return delta;
"""
calculating table T
"""
def tabel_T(qi, alphabet):
	ec = epsilon_closure(qi)
	delta = set()
	for q in ec:
		delta = delta.union(delta_calculator(q,alphabet))
	t = set()
	for w in delta:
		t= t.union(epsilon_closure(w))
	return t;

"""
possible states
"""
new_states = list()
for x in language_alphabets:
	for y in range(1,int(n)+1):
		bc = (tabel_T(str(y),x))
		if bc not in new_states and bc !=set():
			new_states.append(bc)
print(new_states[1])


