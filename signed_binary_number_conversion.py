#Made by Mike_Zhang
def signedMagnitude(numd):
    outnum = ""
    absnumd = abs(int(numd))
    numb = bin(absnumd)
    bnumb = numb[2:]
    fixed = '{:0>7}'.format(bnumb)
    if numd[0:1] == "-":
        outnum = "1" + fixed
    else:
        outnum = "0" + fixed
    print(outnum)

def onesComplement(numd):
    outnum = ""
    if numd[0:1] == "-":
        numd = 256 - 1 - abs(int(numd))
    print(numd)
    absnumd = abs(int(numd))
    numb = bin(absnumd)
    bnumb = numb[2:]
    outnum = '{:0>8}'.format(bnumb)
    print(outnum)

def twosComplement(numd):
    outnum = ""
    if numd[0:1] == "-":
        numd = 256 - abs(int(numd))
    print(numd)
    absnumd = abs(int(numd))
    numb = bin(absnumd)
    bnumb = numb[2:]
    outnum = '{:0>8}'.format(bnumb)
    print(outnum)

def excessEightbits(numd):
    outnum = ""
    biasednum = int(numd) + 128
    numb = bin(biasednum)
    bnumb = numb[2:]
    outnum = '{:0>8}'.format(bnumb)
    print(outnum)

def signedMagnitude_re(numb):
    if numb[0] == "0":
        print(int(numb, 2))
    elif numb[0] == "1":
        print("-", int(str(numb[1:]), 2),sep="")

def onesComplement_re(numb):
    if numb[0] == "0":
        print(int(numb, 2))
    elif numb[0] == "1":
        numd = 256 - 1 - int(str(numb), 2)
        print("-" , numd, sep="")

def twosComplement_re(numb):
    if numb[0] == "0":
        print(int(numb, 2))
    elif numb[0] == "1":
        numd = 256  - int(str(numb), 2)
        print("-" , numd, sep="")

def excessEightbits_re(numb):
    numd = int(str(numb), 2)
    print(numd - 128)

def main():
    con = True
    while con == True:
        choice1 = input("Enter(d = D to B; b = B to D):")
        choice2 = input("Enter(s = Signed Magnitude; 1 = 1s Complement; 2 = 2sComplement; e = excess):")
        if choice1 == "d":
            if choice2 == "s":
                signedMagnitude(input("Enter(-127to127):"))
            elif choice2 == "1":
                onesComplement(input("Enter(-127to127):"))
            elif choice2 == "2":
                twosComplement(input("Enter(-127to128):"))
            elif choice2 == "e":
                excessEightbits(input("Enter(-127to128):"))
        elif choice1 == "b":
            if choice2 == "s":
                signedMagnitude_re(input("Enter(8bit binary):"))
            elif choice2 == "1":
                onesComplement_re(input("Enter(8_bit binary):"))
            elif choice2 == "2":
                twosComplement_re(input("Enter(8bit binary):"))
            elif choice2 == "e":
                excessEightbits_re(input("Enter(8_bit binary):"))
        cont = input("continue?(y/n)")
        if cont == "n":
            con = False

main()
#Made by Mike_Zhang