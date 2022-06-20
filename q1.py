#Q1
from numpy import genfromtxt
user_data = genfromtxt('testSamples.csv', delimiter=',')
control_group = 0
test_group = 0
total_outcome = len(user_data)

for data in user_data :
    if data[1] == 0 :
        control_group += 1
        
    elif data[1] == 1:
        test_group += 1



def approx_prob(testgroup, controlgroup, totaloutcome) :
    prob_control_group = controlgroup/totaloutcome
    prob_test_group = testgroup/totaloutcome
    total_prob = prob_control_group * prob_test_group
    print(round(total_prob,4))
    print(prob_control_group)

approx_prob(test_group,control_group,total_outcome)
    





