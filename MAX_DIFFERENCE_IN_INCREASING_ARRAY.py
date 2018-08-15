#PROBLEM STATEMENT
#Maximum difference between two elements such that larger element appears after the smaller number
#EXAMPLE INPUT
#A = {5,4,6,10,1} - OUTPUT = 6 (DIFFERENCE BETWEEN 4 AND 10
#A = {-1,-12,-5,7,11,9} - OUTPUT = 23 (DIFFERENCE BETWEEN -12 AND 11)
#CORNER CASE = A = {5,4,3,2,1} - OUTPUT = NOT POSSIBLE SINCE NUMBERS IN increasing order

'''
Time complexity for Solution 1 = O(n). Keep track of left min and MAx difference. If new number in scan of array < left_min, update left_min. If current_number
minus left_min > MAX_DIFF , then update the max_difference
'''

def solution_1(A):
    MAX_DIFF = A[1]-A[0]
    left_min = A[0]
    for i in range(1,len(A)):

        if A[i]< left_min:
            left_min = A[i]
            continue
        if A[i] - left_min > MAX_DIFF:
            MAX_DIFF = A[i] - left_min

    return MAX_DIFF

A = [5,4,3,2,1]
if solution_1(A) < 0:
    print ("Not possible. Array in descending order")
else:
    print ("MAx_diff = {}".format(solution_1(A)))

