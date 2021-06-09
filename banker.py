with open('account.txt','r') as f:
    for line in f:
        iban=line
        iban=iban.rstrip()
        bank=iban
        iban=int(iban[2:]+"2521"+iban[:2])

        if iban % 97 == 1:
            check=( int(bank[2])*3 + int(bank[3])*9 + int(bank[4])*7 + int(bank[5])*1 + int(bank[6])*3 + int(bank[7])*9 + int(bank[8])*7 )
            check8=int(bank[9])
            check= 10 - check%10
            if check == check8:
                print(line.rstrip(), ";TRUE", sep="")
            else:
                print(line.rstrip(), ";FALSE !bank", sep="")
        elif iban % 97 > 1:
            print(line.rstrip(), ";FALSE >1", sep="")
        elif iban % 97 == 0:
            print(line.rstrip(), ";FALSE =0", sep="")
        else:
            print(line.rstrip(), ";ERROR", sep="")
