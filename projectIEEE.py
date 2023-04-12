n_sub=int(input("Enter the number of subjects you would like to take: "))
l_sub=[]
#we are obtaining the subjects list
for i in range(n_sub):
    sub=input("Enter the name of the subject: ")
    l_sub.append(sub)
l_slots=[]        #these are all the slots
sub_slots=[]      #these are slots per subject
print("Kindly enter the afternoon slots for the subject first and then the forenoon slots")
#We are obtaining the available slots for each subject
for j in l_sub:
    print("For",j,"how many potential slots would you like to enter?")
    n_slots=int(input())
    for i in range(n_slots):
        slot=input("Enter the slots in caps: ")
        sub_slots.append(slot)
    l_slots.append(sub_slots)
    sub_slots=[]
aft_slots=[]
sub_slotsa=[]
sub_slotsf=[]
for_slots=[]

#We are dividing the given slots in afternoon and forenoon slots
for k in l_slots:
    for m in k:
        if '2' in m:
            sub_slotsa.append(m)
        else:
            sub_slotsf.append(m)
    else:
        aft_slots.append(sub_slotsa)
        sub_slotsa=[]
        for_slots.append(sub_slotsf)
        sub_slotsf=[]
    
#Now we will select one slot and compare

sub_dict=dict()
sub_dict.update({l_sub[0]:aft_slots[0][0]})
temp=[]
temp2=''
for i in range(0,n_sub):
    temp=aft_slots[i]
    for j in temp:
        for key in sub_dict:
            if sub_dict[key]!=j:
                val=j
            else:
                break
        else:
            temp2=l_sub[i]
            if temp2==key:
                break
            else:
                sub_dict.update({temp2:val})
    else:
        temp=for_slots[i]
        for k in temp:
            for key in sub_dict:
                if sub_dict[key]!=k:
                    val=k
                else:
                    break
            else:
                temp2=l_sub[i]
                if temp2==key:
                    break
                else:
                    sub_dict.update({temp2:val})

#to print the subject with slot

for key in sub_dict:
    print(key,end="\t")
    print(sub_dict[key])
