import sys
import os
from time import sleep
if __name__ == "__main__":
    try:
        #register Definition
        Final = []
        DISP = 0x7FF
        Input1 = 0x7FE
        Input2 = 0x7FD
        Input3 = 0x7FC
        AluA = 0x7FB
        AluB = 0x7FA
        Ro1 = 0x7F9
        Ro2 = 0x7F8
        Ro3 = 0x7F7
        Ro4 = 0x7F6
        IfCR = 0x7F5
        IfRR = 0x7F4
        Clocks1 = 0x7F3
        Clocks2 = 0x7F2
        Clocks3 = 0x7F1
        OneR = 0x7F0
        GSR = 0x7EF
        IntR2 = 0x7EE
        Decd = 0x7ED

        RomSize = 256
        WD = 1

        try:
            f = open("Input.txt", "r")
            G = f.readline()
            if "RomSize" in G:
                exec(G ,globals())
            f.close()
        except:
            pass


        #Compiler definition
        Final = []
        WA = []
        Whiles = []

        for i in range(RomSize*2):
            Final.append(0)

        StatePO = RomSize-1
        StatePA = RomSize
        StateI = 0x000

        def DecD(A, Y):
            MV(A, AluA)
            MV(Decd, Y)

        def Derf(Val, Addr):
            MV(Addr, IntR2)
            GI(1, Val)
            GI(16, 0)
            
        def DO():
            WA.append(GetJumpPos())
            Whiles.append(len(WA)-1)

        def WhilE(A, B, Conf):
            If(A, B, WA[Whiles.pop()], Conf)

        def start():
            return GetROM(0)

        def Halt():
            GI(4, 0)

        def GetROM(Pres = None):
            global StatePO
            MP = StatePO
            StatePO -= 1
            if Pres != None:
                setVar(MP, Pres)
            return MP

        def GetRAM(Pres = None):
            global StatePA
            MP = StatePA
            StatePA += 1
            if Pres != None:
                setVar(MP, Pres)
            return MP

        def GetJumpPos():
            global StateI
            return GetROM(StateI)

        def setVar(ADDR, what):
            global Final
            Final[ADDR] = format(what, '04x')

        def CalcIns(INS, ADDR):
            return hex((INS<<11)|ADDR)

        def Neg(A, ADDR):
            GI(9, ADDR)

        def Add(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(5, ADDR)

        def Sub(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(6, ADDR)

        def Mul(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(8, ADDR)

        def Div(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(7, ADDR)

        def And(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(10, ADDR)

        def Or(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(11, ADDR)

        def Not(A, ADDR):
            MV(A, AluA)
            GI(12, ADDR)

        def Xor(A, B, ADDR):
            MV(A, AluA)
            MV(B, AluB)
            GI(13, ADDR)

        def Goto(ADDR):
            return GI(3, ADDR)

        def GI(INS, ADDR):
            global Final, StateI
            if WD == 1:
                if INS == 15:
                    Final[StateI] = CalcIns(INS, ADDR)
                    StateI += 1
                else:
                    Final[StateI] = CalcIns(INS, ADDR)
                    StateI += 1
                    if StateI % 5 == 0:
                        GI(15, 0)
            else:
                Final[StateI] = CalcIns(INS, ADDR)
                StateI += 1

        def MV(A, B):
            global Final
            GI(1, A)
            GI(2, B)

        def OneP(X):
            MV(X, AluA)
            MV(0x7F0, X)

        def If(A, B, Gotop, Conf):
            if type(Conf) == type(""):
                Intp = MkIC(Conf)
                MV(Intp, IfCR)
            else:
                MV(Conf, IfCR)
            MV(A, AluA)
            MV(B, AluB)
            if Gotop != "":
                GI(14, Gotop)

        def MkIC(Inp):
            if Inp == ">2":
                G = 1
            if Inp == "=2":
                G = 2
            if Inp == "<2":
                G = 4
            if Inp == ">u":
                G = 8
            if Inp == "=u":
                G = 16
            if Inp == "<u":
                G = 32
            return GetROM(G)

        #Code
        f = open("Input.txt", "r")
        G = f.read()
        #print(G)
        exec(G ,globals())
        f.close()

        #print('\n\n\n\n', end='')

        #Render
        f =  open("Output.txt", "w")
        f.write("ROM: \n")

        #print("ROM: \n", end='')
        for i in range(RomSize):
            if i%16 == 0 and i != 0:
                f.write('\n')
                #print('\n', end='')
            G = format(int(str(Final[i]), 16), '04x').upper()
            f.write(G+' ')
            
        #f.write("\n\nSize: "+str(StateI+(RomSize-StatePO))+"W")
        f.write("\n\nSize: "+str(round(((StateI+(RomSize-StatePO))/RomSize)*100,2))+"%")

        f.flush()
        f.close()

    except Exception as e:
        OutSt = str(e);
        Location = "Output.txt"
        text_file = open(Location, "w")
        text_file.write(OutSt)
        text_file.close()

    sys.exit(1234)
