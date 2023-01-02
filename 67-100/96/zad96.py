with open("wyjsciezadanie93.txt", "w") as output:
    with open("danezadanie93.txt", "r") as input:
        for line in input:
            output.write(line.upper())
