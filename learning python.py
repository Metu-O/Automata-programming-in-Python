string = input("Enter a string of {0,1,'e'}")
state = 'q1'
#I chose to use a dictionary because of the input is not in
#the dictionary, and error arises
#'e' stands for epsilon 
transitions = {
          'q1': {'0':'q3', '1':'q4', 'e':'q3'},
          'q2': {'0':'q2', '1':'q1'},
          'q3': {'0':'q3', '1':'q4'},
          'q4': {'0':'q2', '1':'q1'}}

def dfa(transitions, state, string):
    state = 'q1'
    for i in string:
        state = transitions[state][i]
    return state


final_state = dfa(transitions=transitions, state=state, string=string)
print(final_state)
if final_state == 'q4':
    print('Accepted')
else:
    print('Rejected')
