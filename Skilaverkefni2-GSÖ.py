#Elmar Ólafsson
#GSÖ
#Skilaverkefni 2

elmar = ["Elmar Ólafsson", "1010972509", "8640643"]
jon = ["Jón Arnarsson", "2509972509", "8635698"]
helgi = ["Helgi í Góu", "0905627829", "7845690"]
gunnar = ["Gunnar sigurðsson", "0510972509", "7846009"]
fannar = ["Fannar Haraldsson", "0806972569", "4831847"]
anton = ["Anton Richter", "1506972569", "7728949"]
odinn = ["Óðinn gíslason", "0509972509", "8640643"]
t1, t2, t3, t4, t5, t6, t7 = [], [], [], [], [], [], []
t = [t1, t2, t3, t4, t5, t6, t7]
skra = [elmar, jon, helgi, gunnar, fannar, anton, odinn]#bý til símaskrá, með ákveðnum nöfnum

svar = True
while svar is True:#bý til valmynd
    print("\nNafn                   Kennitala       Símanúmer")
    print("................................................")
    for i in skra:
        for x in range(10):
            if x + len(i[0]) == 19:
                print(i[0], (" " * x), ":", i[1], " :  ", i[2], end="\n")#Byrja á að prenta símaskránna
    print("\n1.	Bæta við nýjum í símaskránna."
          "\n2.	Breyta upplýsingum í símaskránni."
          "\n3.	Eyða upplýsingum / eyða línu úr símaskránni."
          "\n4.	Prenta út alla símaskránna ein lína per notanda"
          "\n5.	Leita að ákveðnu nafni og prenta upplýsingar um það nafn, sima og kennitölu"
          "\n6.	Hætta í forritinu.")
    val = int(input("\nSláðu inn þitt val:  "))#notandi velur lið
    if val == 1:#Liður 1 er valinn
        #Liður 1
        nafn = input("\nSláðu inn nafn og ýttu á enter: ")
        kt = input("\nSláðu inn kennitölu og ýttu á enter: ")
        nr = input("\nsláðu inn símanúmer og ýtir á enter: ")#bið um nafn simanumer og kennitölu til aö bæta við
        for i in range(7):#fer í gegnum listann með for lykkju
            if not t[i]:
                t[i] = [nafn, kt, nr]
                skra.append(t[i])#bæti í listann
                del t[i]
                break
    elif val == 2:#liður 2 er valinn
        #Liður 2
        breyting = input("\nSláðu inn nafnið á einstaklingi til að breyta (verður að skrifa orðrétt): ")#bið um orðrétt nafn einstaklings
        for i in skra:#forlykkja í gegnum listann
            if breyting == i[0]:#finn nafnið sem var slegið inn
                nafn = input("\nSláðu inn breytt nafn og ýttu á enter: ")
                kt = input("\nSláðu nú inn breytta kennitölu og ýttu á enter: ")
                nr = input("\nsláðu inn breytt símanúmer og ýtir á enter: ")#bið um upplýsingar til að breyta
                i = [nafn, kt, nr]#breyti listanum
    elif val == 3:#liður 3 er valinn
        #Liður 3
        breyting = input("\nSláðu inn orðrétt nafn sem þú villt eyða: ")#bið um orðrétt nafn sem notandi vill eyða
        for i in skra:#for lykkja í gegn um listann
            if breyting == i[0]:#finn nafnið sem notandinn sló inn
                del i#eyði því
    elif val == 4:#liður 4 valinn
        #Liður 4
        print("\nNafn                   Kennitala       Símanúmer")
        print("..................................................")
        for i in skra:
            for x in range(10):
                if x + len(i[0]) == 19:
                    print(i[0], (" " * x), ":", i[1], " :  ", i[2], end="\n")#prenta í símaskránna eina línu per notanda
    elif val == 5:#liður 5 er valinn
        #Liður 5
        breyting = input("\nSláðu inn orðrétt nafn á einstakling sem þú villt finna: ")#bið um orðrétt nafn sem notandi vill finna
        for i in skra:#forlykkja í gegn um listann
            if breyting == i[0]:#finn nafnið sem notandi só inn
                print("\nNafn                   Kennitala       Símanúmer")
                print(".................................................")
                for x in range(10):
                    if x + len(i[0]) == 19:
                        print(i[0], (" " * x), ":", i[1], " :  ", i[2], end="\n")#prenta nafnið, kennitölu og símanúmer
    elif val == 6:#liður 6 er valinn
        svar = False#while lykkja endar
        file = open("simaskra.txt", "w+")
        file.write("\nNafn                   Kennitala       Símanúmer\n")
        file.write(".................................................\n")
        for i in skra:
            file.write("%s\n" % str(i))#vista upplýsingar sem voru breyttar