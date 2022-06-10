"""
inputs
"""
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
finding new states
"""
new_states = list()
for x in language_alphabets:
	for y in range(1,int(n)+1):
		bc = (tabel_T(str(y),x))
		if bc not in new_states and bc !=set():
			new_states.append(bc)
for i in range(0,len(new_states)):
	new_states[i]=list(new_states[i])
"""
finding new ways
"""
new_ways = [];
union = list();
new_list = list();

for x in new_states:
	for y in language_alphabets:
		for k in x:
			table_t_variables = tabel_T(k,y);
			for i in table_t_variables:
				if i not in union:
					union.append(i)
		new_list.append(y)
		new_list.append(list(x))
		new_list.append(union)
		new_ways.append(new_list)
		union = list()
		new_list = list()
"""
determinig DFA ways without e ways
"""
DFA_Ways = list()
for x in new_ways:
	if x[0] != '-' and x[2] !=list():
		DFA_Ways.append(x);
"""
finding the new initial satates 
"""
new_initial_states = list()
for x in initial_states:
	ns = epsilon_closure(x)
	for y in ns:
		if y not in new_initial_states:
			new_initial_states.append(y)
"""
renaming new states
"""

for x in DFA_Ways:
	for i in range(0,len(new_states)):

		if x[1]== new_states[i]:
			x[1] = str(i+1)
		if x[2]== new_states[i]:
			x[2] = str(i+1)
"""
the new initial state
"""

for x in range(0,len(new_states)):
	if new_initial_states == new_states[i]:
		new_initial_states = list()
		new_initial_states.append(str(i+1))
"""
the new final states
""" 
newـfinalـstates = list()
for i in range(0,len(new_states)):
	for y in final_states:
		print(new_states[i])
		if str(y) in new_states[i]:
			if str(i+1) not in newـfinalـstates:
				newـfinalـstates.append(str(i+1))

