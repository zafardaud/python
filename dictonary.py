import json
from difflib import get_close_matches

data= json.load(open("dicdata/data.json"))

def dic(w):
    w=w.casefold()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:

        userinput= input("Did you mean %s instead? Enter Y if yes, or N of no." % get_close_matches(w,data.keys())[0])
        userinput=userinput.casefold()
        if userinput=="y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            if len(data[get_close_matches(w,data.keys())[1]])>0:
                userinput= input("Did you mean %s instead? Enter Y if yes, or N of no." % get_close_matches(w,data.keys())[1])
            else:
                return "This program ends now"
        if userinput=="y":
                        return data[get_close_matches(w,data.keys())[1]]
        elif userinput=="n":
            return w + " : " + "The word does not exist, please check what you have entered."
        else:
            return "Invalid entry"
    else:
        return w + " : " + "The word does not exist, please check what you have entered."

manjudas=input("Enter word: ")

output=dic(manjudas)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
