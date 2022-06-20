#Q2

import pandas as pd 
data1 = pd.read_csv('testSamples.csv')
data2 = pd.read_csv('transData.csv')
result = []
df = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df.reset_index()

no_callin_user = 0
no_webform_user = 0
no_callin_rebill = 0
no_webform_rebill = 0

for  index, user in df.iterrows():
    if user[1] == 1:
        no_callin_user += 1
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
   
                no_callin_rebill += 1
    elif user[1] == 0:
        no_webform_user += 1
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
                
                no_webform_rebill += 1

print(no_callin_rebill)
print(no_webform_rebill)
print(no_callin_user)
print(no_webform_user)

def compare_prob (cal_rebill,cal_user,form_rebill,from_user) :
    if cal_rebill/cal_user > form_rebill/from_user  :
        print("Yes Call-in user are more likely to create a rebill")
    else:
        print("No Call-in user are not more likely to create a rebill")


compare_prob(no_callin_rebill,no_callin_user,no_webform_rebill,no_webform_user) 
                 

          



