"""
you may forgive me for my dirty code!
"""

"""
inputs
"""
n,m,s,q= input().split();
final_states =[];
fs = input().split();
for i in range(0,len(fs)):
	if fs[i]=='1':
		final_states.append(str(i+1))


initial_states = input().split();

language_alphabets=[];
ways = []
for x in range(0,int(m)):
	alphabet, s1, s2 = input().split()
	if alphabet not in language_alphabets:
		language_alphabets.append(alphabet);
	ways.append(alphabet + " "+ s1+ " "+ s2);

words =list()
for i in range(0,int(q)):
	nw= input()
	words.append(nw)
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
reading  astring with a dfa
"""
def string_reader(final_s, initial_s, ways, word):
	
	pointer = initial_s
	temp = word;
	passed= list()
	if word =='':
		if initial_s in final_s:
			print('Yes')
	else:
		for i in range(0, len(word)):
			flagDone = True;
			for x in DFA_Ways:
				flag = False;
				if x[0]==word[i] and pointer == x[1]:
					pointer = x[2]
					passed.append(x[2])
					flag = True
					break;
			if flag==False:
				flagDone=False;
				if len(passed)==0:
					print("No")
				else:
					print("No", end = " ")
					for j in range(0,len(passed)):
						if j!= len(passed)-1:
							print(passed[j], end =" ")
						else:
							print(passed[j])
				break;
		if pointer in final_s and flagDone!=False:
			if len(passed)==0:
					print("Yes")
			else:
				print('Yes', end = " ")
				for j in range(0,len(passed)):
						if j!= len(passed)-1:
							print(passed[j], end =" ")
						else:
							print(passed[j])
		if pointer not in final_s and flagDone!=False:
			if len(passed)==0:
					print("No")
			else:
				print("No", end = " " )
				for j in range(0,len(passed)):
					if j!= len(passed)-1:
						print(passed[j], end =" ")
					else:
						print(passed[j])

"""
finding new states
"""

new_states = list()
for x in language_alphabets:
	for y in range(1,int(n)+1):
		bc = (tabel_T(str(y),x))
		print(bc)
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
new_states_2 = list();
while new_states_2 != new_states:
	new_states_2 = new_states
	for x in new_states_2:
		for y in language_alphabets:
			for k in x:
				table_t_variables = tabel_T(k,y);
				for i in table_t_variables:
					if i not in union:
						union.append(i)

			for i in range(0,len(new_states)):
				new_states[i]=set(new_states[i])
			if set(union) not in new_states and union != list():
				new_states.append(set(union))
			for i in range(0,len(new_states)):
				new_states[i]=list(new_states[i])
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
print(DFA_Ways)
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
	#print(x)
	flag1 = False;
	flag2 = False ;
	for i in range(0,len(new_states)):
		#print(x[1] , new_states[i])
		if set(x[1])== set(new_states[i]) and flag1==False:
			flag1=True
			x[1] = str(i+1)
		if set(x[2])== set(new_states[i]) and flag2==False:
			flag2 = True
			x[2] = str(i+1)
	#print(x)
"""
the new initial state
"""

for x in range(0,len(new_states)):
	if set(new_initial_states) == set(new_states[i]):
		new_initial_states = list()
		new_initial_states.append(str(i+1))
"""
the new final states
""" 
newـfinalـstates = list()
for i in range(0,len(new_states)):
	for y in final_states:
		if str(y) in new_states[i]:
			if str(i+1) not in newـfinalـstates:
				newـfinalـstates.append(str(i+1))
"""
end
"""
print(len(new_states), len(DFA_Ways), new_initial_states[0])
for i in range(0,len(new_states)):
	if str(i+1) in newـfinalـstates:
		if i != len(new_states)-1:
			print('1', end = " ")
		else:
			print('1')
	else:
		if i != len(new_states)-1:
			print('0', end = " ")
		else:
			print('0')
for x in DFA_Ways:
	print(x[0],x[1],x[2])
for x in words:
	x = x.replace("-", "")
	string_reader(newـfinalـstates, new_initial_states[0], DFA_Ways, x)
print(new_states)