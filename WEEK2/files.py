with open("emails.txt", "r") as emails: #file methods
    results = emails.read()
    list_of_emails = results.split() #string methods

    for i in range(len(list_of_emails)): ##for loops
        if list_of_emails[i] == "walobwadan@gmail.com": #if condition
            print("Found Walobwa at position", i + 1)