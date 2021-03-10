#Latin Program: v1.3

print("Word: ")
word = input()
print
print("Noun:1, Verb:2")
partOfSpeech = input()
print
if partOfSpeech == 1:
    print("Declension (use '#n' for neuter): ")
    declension = input()
    print
    base = ""
    if declension == 1:
        x = ""
        x = word[len(word)-1]
        base = word[0:len(word)-1]
        nom = x
        gen = "ae"
        dat = "ae"
        acc = "am"
        abl = "a"
        voc = x
        nompl = "ae"
        genpl = "arum"
        datpl = "is"
        accpl = "as"
        ablpl = "is"
        vocpl = "ae"
    elif declension == 2:
        x = ""
        x = word[len(word)-2:len(word)]
        base = word[0:len(word)-2]
        nom = x
        gen = "i"
        dat = "o"
        acc = "um"
        abl = "o"
        voc = "e"
        nompl = "i"
        genpl = "orum"
        datpl = "is"
        accpl = "os"
        ablpl = "is"
        vocpl = "i"
    elif declension == '2n':
        base = word[0:len(word)-2]
        nom = "um"
        gen = "i"
        dat = "o"
        acc = "um"
        abl = "o"
        voc = "um"
        nompl = "a"
        genpl = "orum"
        datpl = "is"
        accpl = "a"
        ablpl = "is"
        vocpl = "a"
    elif declension == 3:
        x = ""
        x = word[len(word)-1]
        base = word[0:len(word)-1]
        nom = x
        gen = "is"
        dat = "i"
        acc = "em"
        abl = "e"
        voc = x
        nompl = "es"
        genpl = "um"
        datpl = "ibus"
        accpl = "es"
        ablpl = "ibus"
        voc = "es"
    elif declension == '3n':
        x = ""
        x = word[len(word)-1]
        base = word[0:len(word)-1]
        nom = x
        gen = "is"
        dat = "i"
        acc = x
        abl = "e"
        voc = x
        nompl = "a"
        genpl = "um"
        datpl = "ibus"
        accpl = "a"
        ablpl = "ibus"
        vocpl = "a"
    elif declension == 4:
        base = word[0:len(word)-2]
        nom = "us"
        gen = "um"
        dat = "ui"
        acc = "um"
        abl = "u"
        voc = "us"
        nompl = "us"
        genpl = "uum"
        datpl = "ibus"
        accpl = "us"
        ablpl = "ibus"
        vocpl = "us"
    elif declension == '4n':
        base = word[0:len(word)-1]
        nom = "u"
        gen = "us"
        dat = "u"
        acc = "u"
        abl = "u"
        voc = "a"
        nompl = "ua"
        genpl = "uum"
        datpl = "ibus"
        accpl = "ua"
        ablpl = "ibus"
        vocpl = "ua"
    elif declension == 5:
        base = word[0:len(word)-2]
        nom = "es"
        gen = "ei"
        dat = "ei"
        acc = "em"
        abl = "e"
        voc = "es"
        nompl = "es"
        genpl = "erum"
        datpl = "ebus"
        accpl = "es"
        ablpl = "ebus"
        vocpl = "es"
    else:
        base = word
        nom = ""
        gen = ""
        dat = ""
        acc = ""
        abl = ""
        voc = ""
        nompl = ""
        genpl = ""
        datpl = ""
        accpl = ""
        ablpl = ""
        vocpl = ""
    for i in range(12):
        declined = ""
        if i == 0:
            declined = 'Nominative Singular: ' + base + nom
        if i == 1:
            declined = 'Genitive Singular:   ' + base + gen
        if i == 2:
            declined = 'Dative Singular:     ' +  base + dat
        if i == 3:
            declined = 'Accusative Singular: ' + base + acc
        if i == 4:
            declined = 'Ablative Singular:   ' + base + abl
        if i == 5:
            declined = 'Vocative Singular:   ' + base + voc 
        if i == 6:
            print
            declined = 'Nominative Plural:   ' + base + nompl
        if i == 7:
            declined = 'Genitive Plural:     ' + base + genpl
        if i == 8:
            declined = 'Dative Plural:       ' + base + datpl
        if i == 9:
            declined = 'Accusative Plural:   ' + base + accpl
        if i == 10:
            declined = 'Ablative Plural:     ' + base + ablpl
        if i == 11:
            declined = 'Vocative Plural:     ' + base + vocpl
        print(declined)

        
if partOfSpeech == 2:
    print("Conjugation (use 5 for 3io): ")
    conjugation = input()
    print
    base = ""
    if conjugation == 1:
        x = ""
        x = word[len(word)-1]
        base = word[0:len(word)-1]
        first = x
        second = "as"
        third = "at"
        firstPl = "amus"
        secondPl = "atis"
        thirdPl = "ant"
        firstPass = "ar"
        secondPass = "aris"
        thirdPass = "atur"
        firstPassPl = "amur"
        secondPassPl = "amini"
        thirdPassPl = "antur"
        infinitive = "are"
    elif conjugation == 2:
        x = ""
        x = word[len(word)-2]
        base = word[0:len(word)-2]
        first = x
        second = "es"
        third = "et"
        firstPl = "emus"
        secondPl = "etis"
        thirdPl = "ent"
        firstPass = "eor"
        secondPass = "eris"
        thirdPass = "etur"
        firstPassPl = "emur"
        secondPassPl = "emini"
        thirdPassPl = "entur"
        infinitive = "ere"
    elif conjugation == 3:
        x = ""
        x = word[len(word)-1]
        base = word[0:len(word)-1]
        first = x
        second = "is"
        third = "it"
        firstPl = "imus"
        secondPl = "itis"
        thirdPl = "unt"
        firstPass = "or"
        secondPass = "eris"
        thirdPass = "itur"
        firstPassPl = "imur"
        secondPassPl = "imini"
        thirdPassPl = "untur"
        infinitive = "ire"
    elif conjugation == 4:
        x = ""
        x = word[len(word)-2]
        base = word[0:len(word)-2]
        first = x
        second = "is"
        third = "it"
        firstPl = "imus"
        secondPl = "itis"
        thirdPl = "iunt"
        firstPass = "ior"
        secondPass = "iris"
        thirdPass = "itur"
        firstPassPl = "imur"
        secondPassPl = "imini"
        thirdPassPl = "iuntur"
        infinitive = "ire"
    elif conjugation == 5:
        x = ""
        x = word[len(word)-2]
        base = word[0:len(word)-2]
        first = x
        second = "is"
        third = "it"
        firstPl = "imus"
        secondPl = "itis"
        thirdPl = "iunt"
        firstPass = "ior"
        secondPass = "eris"
        thirdPass = "itur"
        firstPassPl = "imur"
        secondPassPl = "imini"
        thirdPassPl = "iuntur"
        infinitive = "ire"
    else:
        first = ""
        second = ""
        third = ""
        firstPl = ""
        secondPl = ""
        thirdPl = ""
        firstPass = ""
        secondPass = ""
        thirdPass = ""
        firstPassPl = ""
        secondPassPl = ""
        thirdPassPl = ""
        infinitive = ""
        
    print
    
    for i in range(13):
        declined = ""
        if i == 0:
            declined = '1st Singular Active:  ' + base + first
        if i == 1:
            declined = '2nd Singular Active:  ' + base + second
        if i == 2:
            declined = '3rd Singular Active:  ' +  base + third
        if i == 3:
            declined = '1st Plural Active:    ' + base + firstPl
        if i == 4: 
            declined = '2nd Plural Active:    ' + base + secondPl
        if i == 5:
            declined = '3rd Plural Active:    ' + base + thirdPl
        if i == 6:
            print
            declined = '1st Singular Passive: ' + base + firstPass
        if i == 7:
            declined = '2nd Singular Passive: ' + base + secondPass
        if i == 8:
            declined = '3rd Singular Passive: ' + base + thirdPass
        if i == 9:
            declined = '1st Plural Passive:   ' + base + firstPassPl
        if i == 10:
            declined = '2nd Plural Passive:   ' + base + secondPassPl
        if i == 11:
            declined = '3rd Plural Passive:   ' + base + firstPassPl
        if i == 12:
            print
            declined = 'Infinitive:           ' + base + infinitive
        print(declined)



print("By Jasper Lin")
