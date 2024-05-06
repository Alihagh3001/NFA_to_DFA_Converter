from array import *
class NFATransitions:
    def __init__(self, from_state, symbols_array, to_states_array):
        self.from_state = from_state
        self.symbols_array = symbols_array 
        self.to_states_array = to_states_array
        

NFAStatesNumber = input()
arr = []
for x in range (int(NFAStatesNumber)):
    arr.append(str(x))



DFAStates = [[]]
for element in arr:
    for idx in range(len(DFAStates)):
        subset = DFAStates[idx]
        DFAStates.append(subset + [element])
DFAStates.sort()         
DFAStates.sort(key=len)       
#print(DFAStates)

NFAFinalStates = input().split(",")
#print(NFAFinalStates)

r = []
line = input()
while(line != "end"):
    r.append(line)
    line = input()
#print(r)
e = []
for x in r:
    e.append(x.split(":"))

#print(e)

NFATransitionsArray = []
from_state = ""
symbols_array = []
to_states_array = []    
num = 0
p = e[0][0]    
for x in e:     
    if x[0] == p:
        from_state = x[0]
        symbols_array.append(x[1])
        to_states_array.append(x[2])
        num = num + 1
        continue
    NFATransitionsArray.append(NFATransitions(from_state,symbols_array[:],to_states_array[:]))
    p = e[num][0]
    num = num + 1
    symbols_array.clear()
    to_states_array.clear()
    from_state = x[0] 
    symbols_array.append(x[1])
    to_states_array.append(x[2])
NFATransitionsArray.append(NFATransitions(from_state,symbols_array[:],to_states_array[:]))


#for obj in NFATransitionsArray:
    #print (obj.from_state)
    #print (obj.symbols_array)
    #print (obj.to_states_array)

print(len(DFAStates))

num1 = 0
DFAStartState = ['0']
for x in NFATransitionsArray[0].symbols_array:
      if x == "'":
          for y in NFATransitionsArray[0].to_states_array[num1]:
              DFAStartState.append(y)
          break
      num1 = num1 + 1
       
DFAStartState = sorted(list(set(DFAStartState)))
if ',' in DFAStartState:      
    DFAStartState.remove(',')
#print(DFAStartState)
for x in range(len(DFAStates)):
    if  DFAStates[x] == DFAStartState:
        print(x)

         
DFAFinalStates = []      
for x in NFAFinalStates:
    for y in range(len(DFAStates)):
        if x in DFAStates[y]:
            DFAFinalStates.append(y)
DFAFinalStates = sorted(list(set(DFAFinalStates)))            
for x in range(len(DFAFinalStates)):
    print(int(DFAFinalStates[x]), end = '') 
    if x != len(DFAFinalStates) - 1:
        print(",", end = '')         
print()


compare = []
epsilon_a = []
epsilon_b = []
for x in range(len(DFAStates)):
    if x == 0:
        print ("0:a:0")
        print ("0:b:0")
        continue
    for y in DFAStates[x]:
        for m in range(len(NFATransitionsArray[int(y)].symbols_array)):
            if NFATransitionsArray[int(y)].symbols_array[m] == 'a':
                compare = (NFATransitionsArray[int(y)].to_states_array[m]).split(",")
                for n in compare:
                    for t in range(len(NFATransitionsArray[int(n)].symbols_array)):
                        if NFATransitionsArray[int(n)].symbols_array[t] == "'":
                            epsilon_a = (NFATransitionsArray[int(n)].to_states_array[t]).split(",")
                            for u in epsilon_a:
                                compare.append(u)
    compare = sorted(list(set(compare)))
    for pk in range(len(DFAStates)):
        if DFAStates[pk] == compare:
            print(str(x)+":a:"+str(pk))
    compare.clear()                    
    epsilon_a.clear()
          

          
    for z in DFAStates[x]:
        for m in range(len(NFATransitionsArray[int(z)].symbols_array)):
            if NFATransitionsArray[int(z)].symbols_array[m] == 'b':
                compare = (NFATransitionsArray[int(z)].to_states_array[m]).split(",")
                for n in compare:
                    for t in range(len(NFATransitionsArray[int(n)].symbols_array)):
                        if NFATransitionsArray[int(n)].symbols_array[t] == "'":
                            epsilon_b = (NFATransitionsArray[int(n)].to_states_array[t]).split(",")
                            for u in epsilon_b:
                                compare.append(u)
    compare = sorted(list(set(compare)))
    for pk in range(len(DFAStates)):
        if DFAStates[pk] == compare:
            print(str(x)+":b:"+str(pk))
    compare.clear()                    
    epsilon_b.clear()