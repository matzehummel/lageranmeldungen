from os import walk

path = "C:/Projects/Automation/Lageranmeldungen/exports"

files = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

signUps = open("Lageranmeldungen.csv", "a")



def parseFile(filename):
    file = open(path + "/" + filename)
    content = file.read()
    content = content.split("Nachname")
    print(content)
    signUpEntries = content[1].split("<br/>")
    if(signUpEntries[-1].strip() == ""):
        signUpEntries.pop(-1)

    counter = 0
    surname = (signUpEntries[counter].split(":"))[1].strip()
    print(surname)

    counter += 1
    name = signUpEntries[counter].split(":")[1].strip()
    print(name)

    counter += 1    # 1
    type = (signUpEntries[counter].split(":"))[1].strip()
    if(type.strip() == "XXL (14-16 Jahre)"):
        type = "XXL"
    else:
        type = "Kinderlager"
    print(type)

    counter += 1    # 2
    birthdate = (signUpEntries[counter].split(":"))[1].strip()
    birthdate = birthdate.replace(" / ", ".")
    print(birthdate)

    counter += 1    # 3
    email = (signUpEntries[counter].split(":"))[1].strip()
    print(email)

    counter += 1    # 4
    phoneEntry = signUpEntries[counter].split(":")
    phone = "no Phone"
    if(phoneEntry[0].strip() == "Telefonnummer"):
        phone = phoneEntry[1].strip()
        counter += 1    # 5
    print(phone)

    address = signUpEntries[counter].split(":")[1].strip()
    print(address)

    counter += 1    # 6 or 7
    postalCode = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 7 or 8
    city = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 8 or 9
    memberOf = signUpEntries[counter].split(":")[1].strip()
    print(memberOf)

    counter += 1    # 9 or 10
    experience = signUpEntries[counter].split(":")[1].strip()
    if(experience.strip() == "schon einmal auf dem Zeltlager dabei"):
        experience = "ja"
    else:
        experience = "nein"
    print(experience)

    counter += 1    # 10 or 11
    supervisors = "no supervisors"
    if(len(signUpEntries) > counter ):
        print(len(signUpEntries))
        print(counter)
        supervisors = signUpEntries[counter].split(":")[2].strip()
    print(supervisors)

    return surname + "\t" + name  + "\t" + type + "\t" + birthdate + "\t" + email + "\t" + phone + "\t" + address + "\t" + postalCode + "\t" + city + "\t" + memberOf + "\t" + experience + "\t" + supervisors

for file in files:
    newline = parseFile(file)
    signUps.write(newline + "\n")

signUps.close()
