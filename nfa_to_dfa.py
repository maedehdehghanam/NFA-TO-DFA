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

"""
finding new ways
"""
new_ways = [];
union = set();
new_list = list();

for x in new_states:
	for y in language_alphabets:
		for k in x:
			table_t_variables = tabel_T(k,y);
			for i in table_t_variables:
				if i not in union:
					union.add(i)
		new_list.append(y)
		new_list.append(x)
		new_list.append(union)
		new_ways.append(new_list)
		union = set()
		new_list = list()
"""
determinig DFA ways without e ways
"""
DFA_Ways = list()
for x in new_ways:
	if x[0] != '-' and x[3] !=set():
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
print(DFA_Ways)

