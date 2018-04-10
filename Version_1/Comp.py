if __name__ == "__main__":
    try:
        import os
        import sys
        import time
        
        Location = "Input.txt"
        text_file = open(Location, "r")
        InputTxT = text_file.readlines() 
        text_file.close()
	
        def allocmemY():
            global memp
            mez = str(format(memp, '02x'))
            mem.append("0000")
            memp += 1
            return mez

        def setY(variable, what):
            adr = int(variable, 16)
            mem[adr] = what

        def setlns(pocet):
            for i in range(pocet):
                R.append("-")

        R = []
        setlns(256)
        R[0] = "0000"
        mem = []
        memp= 0
        null="00"
        nic="00"        

        #Rx = Univerzalni 16b registr
        #Ry = Interní 16b registr, Nedoporucen pro ukladání hodnot, urcen pro neinteruptorovane pouziti.
        #Pc ma 2 pameti, "x" a "y", adresuji se obe najednou,
        #"x" je sdilena s kodem, "y" je ciste hodnotova
        boot = "00"     #Boot
        wait = "00"     #Ceka
        LDAx = "01"     #Ulozi "x" do A
        Addx = "02"     #Pricte "x" k A a ulozi do Rx
        Subx = "05"     #Odecte "x" od A a ulozi do Rx
        OutR = "03"     #vypis Rx
        Halt = "04"     #vypnout (Spise seknout)
        MvRx = "07"     #presune Rx do "x"
        MvxR = "08"     #presune "x" do Rx
        Jmpx = "09"     #Skoci na adresu ulozenou v "x"
        LDAy = "0a"     #Ulozi "y" do Ra
        MvRy = "0b"     #presune Rx do "y"
        MvyR = "0c"     #presune "y" do Rx
        Jmpy = "0d"     #Skoci na adresu ulozene v "y"
        Addy = "0e"     #Pricte "y" k A a ulozi do Rx
        Suby = "0f"     #Odecte "y" od A a ulozi do Rx
        CmBr = "10"     #ulozi "y" do B registru v comparatoru (Bc)
        CmpC = "11"     #Porovna A s Bc, skoci na Jr pokud A < Bc
        Cmjr = "12"     #ulozi "y" do Jump registru(Jr) komparatoru
        Outy = "16"     #vypise "y"
        Mety = "15"     #zobrazi "y" na displeji
        #----
        #Dead instructions, replaced by GPIx
        Stop = "13"     #Zastavi PC a ceka na vstup
        LdtR = "14"     #Nacte uzivateluv vstup do Rx
        #----
        Prny = "17"     #Zobrazi "y" (Ascii) na displeji
        Clrd = "18"     #Smaze displej
        WDon = "19"     #Zapne Watch dog timer
        WDSy = "1a"     #Vlozi hodnotu z "y" do WD porovnavaciho registru
        WDRs = "1b"     #Nastavi WD timer na 0
        GPOy = "1c"     #Odesle "y" do GPO (4bit output registr)
        CHsy = "1d"     #ODesle "y" do Chip select registru. (3bit)
        Bssy = "1e"     #Save (Input) Bus to "y",
        Bsoy = "1f"     #Save "y" to output Bus
        GPIx = "20"     #Da GPRI do pameti
        MvR2y = "21"    #presune Ry do "y"
        MvyR2 = "22"    #presune "y" do Ry
					            #Vytvareni promenne
        OutAr = ""
        OutSt = ""
	    
        for mpn in range(len(InputTxT)):
            try:
                OutAr = OutAr + str(InputTxT[mpn+1])
            except:
                pass

        exec(str(OutAr), globals())
		
        for g in range(int(256)):
            if len(R[g])==2:
                R[g]=R[g]+"00"

        OutSt = OutSt+"Memory X:\n"
        j=0
        kn=0
        for g in range(int(256/16)):
            for h in range(16):
                if R[j] == "-":
                    kn=1
                if kn == 0:
                    OutSt = OutSt+R[j]+" "
                    j=j+1
            if kn == 0:
                OutSt = OutSt+"\n"

        OutSt = OutSt+"\n\n"
        OutSt = OutSt+"Memory Y: \n"
		
        j=0
        for g in range(len(mem)):
            OutSt = OutSt+mem[j]+" "
            j=j+1
            if j == 16:
                OutSt = OutSt+"\n"
                j=0
       

    except Exception as e:
        OutSt = str(e);
    
    Location = "Output.txt"
    text_file = open(Location, "w")
    text_file.write(OutSt)
    text_file.close()

    sys.exit(1234);
