
'''
Function getCharacters
returns a set containing all the characters in a given string
Input: string
Output: set
'''
def getCharacters(s):
    return set(list(s))

'''
Function getAllCharacters
returns a list containing all the unique characters in all 3 strings
Input: string, string, string
Output: list
'''
def getAllCharacters(s1, s2, ans):
    chars1 = getCharacters(s1)
    chars2 = getCharacters(s2)
    charsAns = getCharacters(ans)
    allCharacters = charsAns.union(chars1.union(chars2))
    return list(allCharacters)

'''
Function isAssignmentComplete
returns whether all the variables are assigned or not
Input: list, map
Output: bool
'''
def isAssignmentComplete(allVariables, assigned):
    return len(assigned) == len(allVariables)

'''
Function getStartingLetters
returns a list containing all the unique starting characters in all 3 strings
Input: string, string, string
Output: list
'''
def getStartingLetters(s1, s2, ans):
    return list(set([s1[0], s2[0], ans[0]]))

'''
Function createDomain
returns a map containing the domain of all the unique characters in all 3 strings
Input: string, string, string
Output: dict
'''
def createDomain(s1, s2, ans):
    domain = {}
    allVariables = list(getAllCharacters(s1, s2, ans))
    startingVariables = getStartingLetters(s1, s2, ans)
    nonStartingVariables = list(set(allVariables) - set(startingVariables))
    for variable in startingVariables:
        domain[variable] = list(x for x in range(1, 10))
    for variable in nonStartingVariables:
        domain[variable] = list(x for x in range(0, 10))
    if(len(ans) > len(s1) and len(ans) > len(s2)):
        domain[ans[0]] = [1]
    return domain

'''
Function generateUpdatedDomain
returns the updated domain for the input variable
Input: char, map, string, string, string
Output: list
'''
def generateUpdatedDomain(variable, assignment, s1, s2, ans):
    domain = createDomain(s1, s2, ans)[variable]
    assignedValues = [assignment[x] for x in assignment]
    updatedDomain = [i for i in domain if i not in assignedValues]
    return updatedDomain


'''
Function calcMRV
returns the list of varibles with minimum remaining values
Input: list, map, string, string, string
Output: list
'''
def calcMRV(allVariables, assignedCharacters, s1, s2, ans):
    remChar = [var for var in allVariables if var not in assignedCharacters]

    mrv_variable = min(remChar, key=lambda var: len(generateUpdatedDomain(var, assignedCharacters, s1, s2, ans)))
    min_length = len(generateUpdatedDomain(mrv_variable, assignedCharacters, s1, s2, ans))
    min_length_variables = [var for var in remChar if (current_length := len(generateUpdatedDomain(var, assignedCharacters, s1, s2, ans))) == min_length]
    return min_length_variables

'''
Function degreeHeuristic
returns a map containing the degree heuristic of all the unique characters in all 3 strings
Input: string, string, string
Output: dict
'''
def degreeHeuristic(var, s1, s2, ans):
    charOccurances = {}
    degree = {}
    allVariables = list(getAllCharacters(s1, s2, ans))
    for char in allVariables:
        charOccurances[char] = set()
        degree[char] = 0
    for index, char in enumerate(reversed(s1)):
        charOccurances[char].add(index)
    for index, char in enumerate(reversed(s2)):
        charOccurances[char].add(index)
    for index, char in enumerate(reversed(ans)):
        charOccurances[char].add(index)

    for char in charOccurances:
        degree[char] = len(charOccurances[char])
    
    

    return degree

'''
Function selectUnassigned
returns the variable with after calculating MRV and degree heuristic
Input: list, map, string, string, string
Output: dict
'''
def selectUnassigned(allVariables, assignedCharacters, s1, s2, ans):
    var = calcMRV(allVariables, assignedCharacters, s1, s2, ans)
    degree = degreeHeuristic(var, s1, s2, ans)
    nextVariable = {}
    nextVariableDegree = 0
    for char in var:
        if(degree[char] > nextVariableDegree):
            nextVariableDegree = degree[char]
            nextVariable = char
    return nextVariable

'''
Function isValidAssignment
returns whether all the variables are assigned are not conflicting
Input: map, string, string, string
Output: bool
'''
def isValidAssignment(assignment, s1, s2, ans):
	for item in assignment.items():
		if s1[3] in assignment and s2[3] in assignment and ans[4] in assignment:
			if (assignment[s1[3]] + assignment[s2[3]]) % 10 != assignment[ans[4]]:
				return False
		if s1[2] in assignment and s2[2] in assignment and ans[3] in assignment and s1[3] in assignment and s2[3] in assignment:
			if (assignment[s1[2]] + assignment[s2[2]] + (assignment[s1[3]] + assignment[s2[3]])//10) % 10 != assignment[ans[3]]:
				return False
		if s1[1] in assignment and s2[1] in assignment and ans[2] in assignment and s1[2] in assignment and s2[2] in assignment:
			if (assignment[s1[1]] + assignment[s2[1]] + (assignment[s1[2]] + assignment[s2[2]])//10) % 10 != assignment[ans[2]]:
				return False
		if s1[0] in assignment and s2[0] in assignment and ans[1] in assignment and s1[1] in assignment and s2[1] in assignment:
			if (assignment[s1[0]] + assignment[s2[0]] + (assignment[s1[1]] + assignment[s2[1]])//10) % 10 != assignment[ans[1]]:
				return False
		if s1[0] in assignment and s2[0] in assignment:
			if (assignment[s1[0]] + assignment[s2[0]] + 1) // 10 != 1:
				return False

		if (s1[0] in assignment and s2[0] in assignment and ans[1] in assignment and s1[1] in assignment and s2[1] in assignment
		    and s1[2] in assignment and s2[2] in assignment and s1[3] in assignment and s2[3] in assignment and ans[2] in assignment
				  and ans[3] in assignment and ans[4] in assignment):
			if (assignment[s1[0]] * 1000 + assignment[s1[1]] * 100 + assignment[s1[2]] * 10 + assignment[s1[3]] +
			    assignment[s2[0]] * 1000 + assignment[s2[1]] * 100 + assignment[s2[2]] * 10 + assignment[s2[3]]) != (
								 assignment[ans[0]] * 10000 + assignment[ans[1]] * 1000 + assignment[ans[2]] * 100 + assignment[ans[3]] * 10 + assignment[ans[4]]):
				return False
	return True

'''
Function backtrack
returns the assignment of varibles
Input: map
Output: list
'''
def backtrack(assignment, s1, s2, ans):
    allVariables = getAllCharacters(s1, s2, ans)
    if(isAssignmentComplete(allVariables, assignment)):
        return assignment
    var = selectUnassigned(allVariables, assignment, s1, s2, ans)
    for value in generateUpdatedDomain(var, assignment, s1, s2, ans):
        
        
        assignment[var] = value
        if isValidAssignment(assignment, s1, s2, ans):
            result = backtrack(assignment, s1, s2, ans)
            if result:
                return result
            
        assignment.popitem()
    
    return None

def backtracking_search(s1, s2, ans):
    return backtrack({}, s1, s2, ans)


def main():
    # Read input
    with open("AI/finalsubmission/input4.txt", 'r') as file:
        lines = file.readlines()
        s1 = lines[0].strip()
        s2 = lines[1].strip()
        ans = lines[2].strip()
    
    print(s1)
    print(s2)
    print(ans)
    
    final_assignment = backtracking_search(s1, s2, ans)
    
    solution_s1 = ''.join(str(final_assignment[x]) for x in s1)
    solution_s2 = ''.join(str(final_assignment[x]) for x in s2)
    solution_ans = ''.join(str(final_assignment[x]) for x in ans)
    print(solution_s1)
    print(solution_s2)
    print(solution_ans)

    # Write output
    with open("AI/finalsubmission/output4.txt", 'w+') as file:
        file.write(solution_s1 + '\n' + solution_s2 + '\n' + solution_ans)
    print("Final Answer", final_assignment)


if __name__ == "__main__":
     main()