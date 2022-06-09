from tabulate import tabulate
m,n,s,q= input().split();
final_states =[];
i =1;
for x in range(0,int(n)):
	k = input()
	if k=='1':
		final_states.append(i);
	i = i+1;
print(final_states);

initial_states = []
for x in range(0,int(s)):
	k = input()
	initial_states.append(k)

language_alphabets=[];
for x in range(0,int(m)):
	alphabet, s1, s2 = input().split()