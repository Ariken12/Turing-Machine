class TuringMachine:
    def __init__(self):
        self.node = 'q0'
        self.rules = {} # rule: (node1, mean1): (node2, mean2, shift, end?)

    def execution(self, string):
        line = list(string)
        index = 0
        while True:
            result = self.rules[(self.node, line[index])]
            self.node = result[0]
            line[index] = result[1]
            index += result[2]
            if result[3]:
                break
        string = str(line)
        return string
