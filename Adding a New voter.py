#Excersice no 18 -Adding a New voter
Voters_Detail = [
    {
        "Name":"Hariharan",
        'Roll_no':1007,
        'Age':22,
        'Voting_Place':"Nondimedu"
    },
    {
        "Name":"Aswin",
        'Roll_no': 121,
        'Age':23,
        'Voting_place':"Kaandhal",
        'Phone_no':[63791,98765]
    }
]
def Add_New_Voter(Name,Roll_no,Age,Voting_Place):
    New_Voter = {}
    New_Voter["Name"] = Name
    New_Voter["Roll_no"] = Roll_no
    New_Voter["Age"] = Age
    New_Voter["Voting_place"] = Voting_Place
    Voters_Detail.append(New_Voter)
    
Add_New_Voter("Caleb",124,24,"Marry's Hill")
print(Voters_Detail)
