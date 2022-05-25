base = {"A": "U", "U": "A", "G": "C", "C": "G"}
wobbel = {"U": "G", "G": "U"}

def checker(pair):

    if pair in base.items():
        return 1
    if pair in wobbel.items():
        return 1

    return 0


def traceback(paired, sequence, sequence_Matrix, i, lenghtseq):
    j = lenghtseq
    if i >= j:
        pass
    elif sequence_Matrix[i][j] == sequence_Matrix[i + 1][j]:
        traceback(paired, sequence, sequence_Matrix, i + 1, j)
    elif sequence_Matrix[i][j] == sequence_Matrix[i][j - 1]:
        traceback(paired, sequence, sequence_Matrix, i, j - 1)
    elif sequence_Matrix[i][j] == sequence_Matrix[i + 1][j - 1] + checker((sequence[i], sequence[j])):
        paired.append((i, j))
        traceback(paired, sequence, sequence_Matrix, i + 1, j - 1)
    else:
        for k in range(i + 1, j):
            if sequence_Matrix[i][j] == sequence_Matrix[i][k] + sequence_Matrix[k + 1][j]:
                traceback(paired, sequence, sequence_Matrix, i, k)
                traceback(paired, sequence, sequence_Matrix, k + 1, j)
                break

    # print(paired)
    listOfTraceBack = []

    for initializedDotts in range(len(sequence)):
        listOfTraceBack.append(".")

    for eachBracket in paired:
        listOfTraceBack[min(eachBracket)] = "("
        listOfTraceBack[max(eachBracket)] = ")"

    listOfTraceBack = "".join(listOfTraceBack)

    return listOfTraceBack


def Nossinov(sequence):
    lenght_of_sequence = len(sequence)

    sequence_Matrix = [[0 for x in range(lenght_of_sequence)] for x in range(lenght_of_sequence)]

    for i in range(0, lenght_of_sequence, 1):
        sequence_Matrix[i][i] = 0
    for i in range(1, lenght_of_sequence, 1):
        sequence_Matrix[i][i - 1] = 0
    for q in range(1, lenght_of_sequence):
        for i in range(0, lenght_of_sequence):
            j = i + q

            if (j >= lenght_of_sequence):
                break

            Down = sequence_Matrix[i + 1][j]
            Left = sequence_Matrix[i][j - 1]
            Diagonal = sequence_Matrix[i + 1][j - 1] + checker((sequence[i], sequence[j]))

            listOfMaxBifuraction = [0]

            for k in range(i + 1, j):
                num = (sequence_Matrix[i][k] + sequence_Matrix[k + 1][j])
                # print(L[i][k] + L[k + 1][j])
                listOfMaxBifuraction.append(num)
            bifuraction = max(listOfMaxBifuraction)

            # print(list)
            sequence_Matrix[i][j] = max(Down, Left, Diagonal, bifuraction)

    result = traceback([], sequence, sequence_Matrix, 0, lenght_of_sequence - 1)

    print("The structure:")

    print(result)
    print("\n")
    print("The Matrix:")

    for i in range(0, len(sequence), 1):
        print(sequence_Matrix[i])


# calling the function
# sequence = "GGGAAAUCC"
# sequence="CGGACCCAGACUUUC"
# sequence="AUACCCUGUGGUAU"
# sequence="GGUUCCUUCCCAA"
sequence = ""
print("Enter sequence of RNA :-")
sequence = input()
Nossinov(sequence)
