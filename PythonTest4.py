#!python3
import smbus
import time
 
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x23 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01 # Pin direction register
OLATA  = 0x14 # Register for outputs
OLATB  = 0x15 # Register for outputs
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # Register for inputs

correctNANDList=[['1','1','1','0'],['1','1','1','0'],['1','1','1','0'],['1','1','1','0']]
correctNORList=[['1','0','0','0'],['1','0','0','0'],['1','0','0','0'],['1','0','0','0']]
correctNOTList=[['1','0'],['1','0'],['1','0'],['1','0'],['1','0'],['1','0']]
correctANDList=[['0','0','0','1'],['0','0','0','1'],['0','0','0','1'],['0','0','0','1']]
correctORList=[['0','1','1','1'],['0','1','1','1'],['0','1','1','1'],['0','1','1','1']]
correctXORList=[['0','1','1','0'],['0','1','1','0'],['0','1','1','0'],['0','1','1','0']]

row4List=[['0','0','1','1'],['0','0','1','1'],['0','0','1','1'],['0','0','1','1']]
column4List=[['0','1','0','1'],['0','1','0','1'],['0','1','0','1'],['0','1','0','1']]
row2List=[['0','1'],['0','1'],['0','1'],['0','1'],['0','1'],['0','1']]

def getTextSegment(bitValue):
    returnValue = [0 for i in range (0,8)]
    for i in range (0,8):
        returnValue[7-i] = int(bitValue % 2)
        bitValue /= 2;
    return returnValue

#NAND
def NANDTest():
    bus.write_byte_data(DEVICE,IODIRA,0x24) #00100100
    bus.write_byte_data(DEVICE,IODIRB,0x09) #00001001
    NANDList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NANDList[0][0]=stringA[5]
    NANDList[1][0]=stringA[2]
    NANDList[2][0]=stringB[4]
    NANDList[3][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NANDList[0][1]=stringA[5]
    NANDList[1][1]=stringA[2]
    NANDList[2][1]=stringB[4]
    NANDList[3][1]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x09) #00001001
    bus.write_byte_data(DEVICE,OLATB,0x24) #00100100
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NANDList[0][2]=stringA[5]
    NANDList[1][2]=stringA[2]
    NANDList[2][2]=stringB[4]
    NANDList[3][2]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x1B) #00011011
    bus.write_byte_data(DEVICE,OLATB,0x36) #00110110
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NANDList[0][3]=stringA[5]
    NANDList[1][3]=stringA[2]
    NANDList[2][3]=stringB[4]
    NANDList[3][3]=stringB[7]
    
    match = True
    gateWorks = True
    for i in range(0,4):
        for j in range(0,4):
            if NANDList[i][j] != correctNANDList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("NAND Gate " + str(i+1) + " of 74LS00 outputs " + NANDList[i][j] + " when " + row4List[i][j] + " and " + column4List[i][j] + " are inputted.")
                    match = True
    if gateWorks == True:
        print("74LS00 is functioning properly.")

#NOR                    
def NORTest():
    bus.write_byte_data(DEVICE,IODIRA,0x09) #00001001
    bus.write_byte_data(DEVICE,IODIRB,0x24) #00100100
    NORList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NORList[0][0]=stringA[7]
    NORList[1][0]=stringA[4]
    NORList[2][0]=stringB[2]
    NORList[3][0]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x24) #00100100
    bus.write_byte_data(DEVICE,OLATB,0x09) #00001001
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NORList[0][1]=stringA[7]
    NORList[1][1]=stringA[4]
    NORList[2][1]=stringB[2]
    NORList[3][1]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NORList[0][2]=stringA[7]
    NORList[1][2]=stringA[4]
    NORList[2][2]=stringB[2]
    NORList[3][2]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x36) #00110110
    bus.write_byte_data(DEVICE,OLATB,0x1B) #00011011
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NORList[0][3]=stringA[7]
    NORList[1][3]=stringA[4]
    NORList[2][3]=stringB[2]
    NORList[3][3]=stringB[5]

    match = True
    gateWorks = True
    for i in range(0,4):
        for j in range(0,4):
            if NORList[i][j] != correctNORList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("NOR Gate " + str(i+1) + " of 74LS02 outputs " + NORList[i][j] + " when " + row4List[i][j] + " and " + column4List[i][j] + " are inputted.")
                    match = True
    if gateWorks == True:
        print("74LS02 is functioning properly.")

#NOT    
def NOTTest():
    bus.write_byte_data(DEVICE,IODIRA,0x2A) #00101010
    bus.write_byte_data(DEVICE,IODIRB,0x15) #00010101
    NOTList=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NOTList[0][0]=stringA[6]
    NOTList[1][0]=stringA[4]
    NOTList[2][0]=stringA[2]
    NOTList[3][0]=stringB[3]
    NOTList[4][0]=stringB[5]
    NOTList[5][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x15) #00010101
    bus.write_byte_data(DEVICE,OLATB,0x2A) #00101010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    NOTList[0][1]=stringA[6]
    NOTList[1][1]=stringA[4]
    NOTList[2][1]=stringA[2]
    NOTList[3][1]=stringB[3]
    NOTList[4][1]=stringB[5]
    NOTList[5][1]=stringB[7]
    
    match = True
    gateWorks = True
    for i in range(0,6):
        for j in range(0,2):
            if NOTList[i][j] != correctNOTList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("NOT Gate " + str(i+1) + " of 74LS04 outputs " + NOTList[i][j] + " when " + row2List[i][j] + " is inputted.")
                    match = True
    if gateWorks == True:
        print("74LS04 is functioning properly.")
        
#AND
def ANDTest():
    bus.write_byte_data(DEVICE,IODIRA,0x24) #00100100
    bus.write_byte_data(DEVICE,IODIRB,0x09) #00001001
    ANDList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ANDList[0][0]=stringA[5]
    ANDList[1][0]=stringA[2]
    ANDList[2][0]=stringB[4]
    ANDList[3][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ANDList[0][1]=stringA[5]
    ANDList[1][1]=stringA[2]
    ANDList[2][1]=stringB[4]
    ANDList[3][1]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x09) #00001001
    bus.write_byte_data(DEVICE,OLATB,0x24) #00100100
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ANDList[0][2]=stringA[5]
    ANDList[1][2]=stringA[2]
    ANDList[2][2]=stringB[4]
    ANDList[3][2]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x1B) #00011011
    bus.write_byte_data(DEVICE,OLATB,0x36) #00110110
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ANDList[0][3]=stringA[5]
    ANDList[1][3]=stringA[2]
    ANDList[2][3]=stringB[4]
    ANDList[3][3]=stringB[7]
    
    match = True
    gateWorks = True
    for i in range(0,4):
        for j in range(0,4):
            if ANDList[i][j] != correctANDList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("AND Gate " + str(i+1) + " of 74LS08 outputs " + ANDList[i][j] + " when " + row4List[i][j] + " and " + column4List[i][j] + " are inputted.")
                    match = True
    if gateWorks == True:
        print("74LS08 is functioning properly.")
        
#OR              
def ORTest():
    bus.write_byte_data(DEVICE,IODIRA,0x24) #00100100
    bus.write_byte_data(DEVICE,IODIRB,0x09) #00001001
    ORList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ORList[0][0]=stringA[5]
    ORList[1][0]=stringA[2]
    ORList[2][0]=stringB[4]
    ORList[3][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ORList[0][1]=stringA[5]
    ORList[1][1]=stringA[2]
    ORList[2][1]=stringB[4]
    ORList[3][1]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x09) #00001001
    bus.write_byte_data(DEVICE,OLATB,0x24) #00100100
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ORList[0][2]=stringA[5]
    ORList[1][2]=stringA[2]
    ORList[2][2]=stringB[4]
    ORList[3][2]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x1B) #00011011
    bus.write_byte_data(DEVICE,OLATB,0x36) #00110110
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    ORList[0][3]=stringA[5]
    ORList[1][3]=stringA[2]
    ORList[2][3]=stringB[4]
    ORList[3][3]=stringB[7]
    
    match = True
    gateWorks = True
    for i in range(0,4):
        for j in range(0,4):
            if ORList[i][j] != correctORList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("OR Gate " + str(i+1) + " of 74LS32 outputs " + ORList[i][j] + " when " + row4List[i][j] + " and " + column4List[i][j] + " are inputted.")
                    match = True
    if gateWorks == True:
        print("74LS32 is functioning properly.")
        
#XOR    
def XORTest():
    bus.write_byte_data(DEVICE,IODIRA,0x24) #00100100
    bus.write_byte_data(DEVICE,IODIRB,0x09) #00001001
    XORList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    XORList[0][0]=stringA[5]
    XORList[1][0]=stringA[2]
    XORList[2][0]=stringB[4]
    XORList[3][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    XORList[0][1]=stringA[5]
    XORList[1][1]=stringA[2]
    XORList[2][1]=stringB[4]
    XORList[3][1]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x09) #00001001
    bus.write_byte_data(DEVICE,OLATB,0x24) #00100100
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    XORList[0][2]=stringA[5]
    XORList[1][2]=stringA[2]
    XORList[2][2]=stringB[4]
    XORList[3][2]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x1B) #00011011
    bus.write_byte_data(DEVICE,OLATB,0x36) #00110110
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    XORList[0][3]=stringA[5]
    XORList[1][3]=stringA[2]
    XORList[2][3]=stringB[4]
    XORList[3][3]=stringB[7]
    
    match = True
    gateWorks = True
    for i in range(0,4):
        for j in range(0,4):
            if XORList[i][j] != correctXORList[i][j]:
                match = False
                gateWorks = False    
            if match == False:
                    print("XOR Gate " + str(i+1) + " of 74LS86 outputs " + XORList[i][j] + " when " + row4List[i][j] + " and " + column4List[i][j] + " are inputted.")
                    match = True
    if gateWorks == True:
        print("74LS86 is functioning properly.")
        
def gateDetector():
    bus.write_byte_data(DEVICE,IODIRA,0x24) #00100100
    bus.write_byte_data(DEVICE,IODIRB,0x09) #00001001
    detectList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][0]=stringA[5]
    detectList[1][0]=stringA[2]
    detectList[2][0]=stringB[4]
    detectList[3][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][1]=stringA[5]
    detectList[1][1]=stringA[2]
    detectList[2][1]=stringB[4]
    detectList[3][1]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x09) #00001001
    bus.write_byte_data(DEVICE,OLATB,0x24) #00100100
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][2]=stringA[5]
    detectList[1][2]=stringA[2]
    detectList[2][2]=stringB[4]
    detectList[3][2]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x1B) #00011011
    bus.write_byte_data(DEVICE,OLATB,0x36) #00110110
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][3]=stringA[5]
    detectList[1][3]=stringA[2]
    detectList[2][3]=stringB[4]
    detectList[3][3]=stringB[7]
    
    matchNAND = True
    for i in range(0,4):
        for j in range(0,4):
            if detectList[i][j] != correctNANDList[i][j]:
                matchNAND = False 
            if matchNAND == False:
                break
        if matchNAND == False:
            break
    if matchNAND == True:
        print('The IC should be 74LS00.')
        return
    
    matchAND = True
    for i in range(0,4):
        for j in range(0,4):
            if detectList[i][j] != correctANDList[i][j]:
                matchAND = False 
            if matchAND == False:
                break
        if matchAND == False:
            break
    if matchAND == True:
        print('The IC should be 74LS08.')
        return
        
    matchOR = True
    for i in range(0,4):
        for j in range(0,4):
            if detectList[i][j] != correctORList[i][j]:
                matchOR = False 
            if matchOR == False:
                break
        if matchOR == False:
            break
    if matchOR == True:
        print('The IC should be 74LS32.')
        return
            
    matchXOR = True
    for i in range(0,4):
        for j in range(0,4):
            if detectList[i][j] != correctXORList[i][j]:
                matchXOR = False 
            if matchXOR == False:
                break
        if matchXOR == False:
            break
    if matchXOR == True:
        print('The IC should be 74LS86.')
        return

    bus.write_byte_data(DEVICE,IODIRA,0x09) #00001001
    bus.write_byte_data(DEVICE,IODIRB,0x24) #00100100
    detectList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][0]=stringA[7]
    detectList[1][0]=stringA[4]
    detectList[2][0]=stringB[2]
    detectList[3][0]=stringB[6]
    
    bus.write_byte_data(DEVICE,IODIRA,0x09) #00001001
    bus.write_byte_data(DEVICE,IODIRB,0x24) #00100100
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][0]=stringA[7]
    detectList[1][0]=stringA[4]
    detectList[2][0]=stringB[2]
    detectList[3][0]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x24) #00100100
    bus.write_byte_data(DEVICE,OLATB,0x09) #00001001
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][1]=stringA[7]
    detectList[1][1]=stringA[4]
    detectList[2][1]=stringB[2]
    detectList[3][1]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x12) #00010010
    bus.write_byte_data(DEVICE,OLATB,0x12) #00010010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][2]=stringA[7]
    detectList[1][2]=stringA[4]
    detectList[2][2]=stringB[2]
    detectList[3][2]=stringB[5]
    
    bus.write_byte_data(DEVICE,OLATA,0x36) #00110110
    bus.write_byte_data(DEVICE,OLATB,0x1B) #00011011
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][3]=stringA[7]
    detectList[1][3]=stringA[4]
    detectList[2][3]=stringB[2]
    detectList[3][3]=stringB[5]

    matchNOR = True
    for i in range(0,4):
        for j in range(0,4):
            if detectList[i][j] != correctNORList[i][j]:
                matchNOR = False 
            if matchNOR == False:
                break
        if matchNOR == False:
            break
    if matchNOR == True:
        print('The IC should be 74LS02.')
        return 

    bus.write_byte_data(DEVICE,IODIRA,0x2A) #00101010
    bus.write_byte_data(DEVICE,IODIRB,0x15) #00010101
    detectList=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    
    bus.write_byte_data(DEVICE,OLATA,0x00) #00000000
    bus.write_byte_data(DEVICE,OLATB,0x00) #00000000
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][0]=stringA[6]
    detectList[1][0]=stringA[4]
    detectList[2][0]=stringA[2]
    detectList[3][0]=stringB[3]
    detectList[4][0]=stringB[5]
    detectList[5][0]=stringB[7]
    
    bus.write_byte_data(DEVICE,OLATA,0x15) #00010101
    bus.write_byte_data(DEVICE,OLATB,0x2A) #00101010
    longA = bus.read_byte_data(DEVICE,GPIOA)
    longB = bus.read_byte_data(DEVICE,GPIOB)
    stringA=""
    stringB=""
    for i in range(8):
        stringA += str(getTextSegment(longA)[i])
    for i in range(8):
        stringB += str(getTextSegment(longB)[i])
    detectList[0][1]=stringA[6]
    detectList[1][1]=stringA[4]
    detectList[2][1]=stringA[2]
    detectList[3][1]=stringB[3]
    detectList[4][1]=stringB[5]
    detectList[5][1]=stringB[7]

    matchNOT = True
    for i in range(0,6):
        for j in range(0,2):
            if detectList[i][j] != correctNOTList[i][j]:
                matchNOT = False 
            if matchNOT == False:
                break
        if matchNOT == False:
            break
    if matchNOT == True:
        print('The IC should be 74LS04.')
        return
        
    print('IC not recognized.')
        
while True:
    detectarOrTest = raw_input("Do you want to TEST or DETECT an IC?\n")
    if detectarOrTest.lower() == "end":
        break
    elif detectarOrTest.lower() == "detect":
        gateDetector()
    elif detectarOrTest.lower() == "test":
        while True:
            gateName = raw_input("Which IC do you want to test? (NAND, NOR, NOT, AND, OR, XOR, end)\n")
            if gateName.lower() == "end":
                break
            elif gateName.lower() == "nand":
                NANDTest()
            elif gateName.lower() == "nor":
                NORTest()
            elif gateName.lower() == "not":
                NOTTest()
            elif gateName.lower() == "and":
                ANDTest()
            elif gateName.lower() == "or":
                ORTest()
            elif gateName.lower() == "xor":
                XORTest()
            else:
                print("Invalid input.")
    else:
        print("Invalid input. Please enter \"detect\", \"test\", or \"end\".")