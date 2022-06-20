#Q3
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
no_Call_add_rebill =0
no_web_add_rebill =0
for  index, user in df.iterrows():
    rebill_count = 0
    if user[1] == 1:
        no_callin_user += 1
        
        
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
                
                no_callin_rebill += 1
                rebill_count += 1
        if rebill_count > 1:
             no_Call_add_rebill += 1  
    elif user[1] == 0:
        no_webform_user += 1
        
        
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
                # print("true"+"-", user[0])
                # result.append("true")
                no_callin_rebill += 1
                rebill_count += 1
        if rebill_count > 1:
             no_web_add_rebill += 1


def compare_add_rebill (noCallAddreBill,noCallinUser,noWebAddRebill,noWebformUser) :
    if noCallAddreBill/noCallinUser > noWebAddRebill/noWebformUser :
        print(noCallAddreBill/noCallinUser)
        print(noWebAddRebill/noWebformUser)
        print ("There is a higher probability of a call-in user to generate an additional REBILL")
compare_add_rebill (no_Call_add_rebill,no_callin_user,no_web_add_rebill,no_webform_user)
