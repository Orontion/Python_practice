DimR_1 = int(input("Enter rows matrix 1: "))
DimC_1 = int(input("Enter columns matrix 1: "))

DimR_2 = int(input("Enter rows matrix 2: "))

CorrectInput = False
while not CorrectInput:
    DimC_2 = int(input("Enter columns matrix 2: "))

    if DimC_2 == DimR_1:
        CorrectInput = True
    else:
        print("Incorrect input! Columns count of matrix 2 should be equal to rows count of matrix 1!")

print("Please enter matrix 1 row by row: \r\n")
Matrix1 = []
for Rows in range(DimR_1):

    CorrectInput = False
    while not CorrectInput:
        TempList = list(input("").split(','))

        if len(TempList) == DimC_1:
            CorrectInput = True
        else:
            print("Incorrect input! Columns count in matrix 1 should be equal to {}".format(DimC_1))

    TempRow = []
    for i in range(len(TempList)):
        TempRow.append(int(TempList[i]))

    Matrix1.append(TempRow)

for i in range(len(Matrix1)):
    print(Matrix1[i])

print("Please enter matrix 2 row by row: \r\n")
Matrix2 = []
for Rows in range(DimR_2):

    CorrectInput = False
    while not CorrectInput:
        TempList = list(input("").split(','))

        if len(TempList) == DimC_2:
            CorrectInput = True
        else:
            print("Incorrect input! Columns count in matrix 2 should be equal to {}".format(DimC_2))

    TempRow = []
    for i in range(len(TempList)):
        TempRow.append(int(TempList[i]))

    Matrix2.append(TempRow)

for i in range(len(Matrix2)):
    print(Matrix2[i])

MatrixResult = []

for Rows in range(DimR_1):
    RowResult = []
    for Columns in range (DimC_2):
        Result = 0
        for ProcItem in range(DimC_1):
            Result+=(Matrix1[Rows][ProcItem]*Matrix2[ProcItem][Columns])

        RowResult.append(Result)

    MatrixResult.append(RowResult)

for i in range(len(MatrixResult)):
    print(MatrixResult[i])