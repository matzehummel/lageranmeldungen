from os import walk


print("Lageranmeldungen-Parser started...")
path = "C:/Projects/Automation/Lageranmeldungen/exportsXXL"
print("Path: " + path)

files = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break
print(str(len(files)) + " Documents found.")

signUps = open("AnmeldungenXXL.csv", "a")


def parseFile(filename):
    print("Parsing " + filename + " ...")
    file = open(path + "/" + filename, 'r')
    content = file.read()
    content = content.split("Nachname des/der")
    signUpEntries = content[1].split("<br/>")
    if(signUpEntries[-1].strip() == ""):
        signUpEntries.pop(-1)

    counter = 0
    surnameChild = (signUpEntries[counter].split(":"))[1].strip()

    counter += 1
    nameChild = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 2
    birthdate = (signUpEntries[counter].split(":"))[1].strip()
    birthdate = birthdate.replace(" / ", ".")

    counter += 1    # 3
    email = (signUpEntries[counter].split(":"))[1].strip()

    counter += 1    # 4
    phoneEntry = signUpEntries[counter].split(":")
    phone = "no Phone"
    if(phoneEntry[0].strip() == "Telefonnummer"):
        phone = phoneEntry[1].strip()
        counter += 1    # 5

    address = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 6 or 7
    postalCode = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 7 or 8
    city = signUpEntries[counter].split(":")[1].strip()

    counter += 1
    normalCamp = signUpEntries[counter].split(":")[1].strip()
    if(normalCamp == "true"):
        normalCamp = "1"
    else:
        normalCamp = "0"
    
    counter += 1
    longerCamp = signUpEntries[counter].split(":")[1].strip()
    if(longerCamp == "true"):
        longerCamp = "1"
    else:
        longerCamp = "0"

    counter += 1
    hikingCamp = signUpEntries[counter].split(":")[1].strip()
    if(hikingCamp == "true"):
        hikingCamp = "1"
    else:
        hikingCamp = "0"

    counter += 1    # 8 or 9
    memberOf = signUpEntries[counter].split(":")[1].strip()

    counter += 1    # 9 or 10
    experienceKL = signUpEntries[counter].split(":")[1].strip()
    experienceKL = parseExperienceKL(experienceKL)

    counter += 1    # 9 or 10
    experienceXXL = signUpEntries[counter].split(":")[1].strip()
    experienceXXL = parseExperienceXXL(experienceXXL)

    counter += 1    # 9 or 10
    notes = "none"
    if(len(signUpEntries) > counter ):
        notes = signUpEntries[counter].split(":")[1].strip()

    return surnameChild + "\t" + nameChild  + "\t" + birthdate + "\t" + email + "\t" + phone + "\t" + address + "\t" + postalCode + "\t" + city + "\t" + normalCamp + "\t" + longerCamp + "\t" + hikingCamp + "\t" +  memberOf + "\t" + experienceKL + "\t" + experienceXXL + "\t" + notes

def parseExperienceKL(exp):
    if(exp == "nie dabei"):
        return "0"
    else:
        return exp[0]

def parseExperienceXXL(exp):
    if(exp == "noch nie dabei"):
        return "0"
    else:
        return exp[0]


for file in files:
    newline = parseFile(file)
    signUps.write(newline + "\n")


print("Done")

signUps.close()
