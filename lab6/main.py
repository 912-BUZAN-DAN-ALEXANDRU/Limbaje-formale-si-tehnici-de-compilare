fa_file = open("FA.in", "r")

content = fa_file.readlines()
FA = content[0].split('=')[1][:-1].split(',')
states = content[1].split('=')[1][:-1].split(',')
initial_state = content[2].split('=')[1][:-1]
alphabet = content[3].split('=')[1][:-1].split(',')
final_states = content[4].split('=')[1][:-1].split(',')
transitions = dict()
for st in content[5:]:
    [f, result] = st.split("=")
    result = result[:-1]
    [instate, inval] = f[2:-1].split(',')
    if instate in transitions.keys():
        transitions[instate][inval] = result
    else:
        transitions[instate] = dict()
        transitions[instate][inval] = result

print("States: ")
for s in states:
    print(s, sep=' ')

print("Alphabet: ")
for a in alphabet:
    print (a, sep=' ')

print("Transitions: ")
for k in transitions.keys():
    for k2 in transitions[k].keys():
        print ("F(" + k + "," + k2 + ")=" + transitions[k][k2], sep=' ')

print("Initial State = " + initial_state)
print("Final States: ")
for a in final_states:
    print (a, sep=' ')
print('\n')


test_input = input()[:-1]
current_state = initial_state
for i in test_input:
    current_state = transitions[current_state][i]
print(current_state)
if current_state in final_states:
    print("Pattern Found")
else:
    print("Pattern not Found")