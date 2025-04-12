import numpy as np

class nTupleNewrok:
    def __init__(self, tuples):
        self.TUPLES = tuples
        self.TARGET_PO2 = 15
        self.LUTS = self.initialize_LUTS(self.TUPLES)

    def initialize_LUTS(self, tuples):
        LUTS = []
        for tp in tuples:
            LUTS.append(np.zeros((self.TARGET_PO2 + 1) ** len(tp)))
        return LUTS
    
    def tuple_id(self, values):
        values = values[::-1]
        k = 1
        n = 0
        for v in values:
            if v >= self.TARGET_PO2:
                return 0
            n += v * k
            k *= self.TARGET_PO2
        return n

    def V(self, board):
        total = 0
        k = 0
        for (tp, LUT) in zip(self.TUPLES, self.LUTS):
            tempboard = board.flatten()
            tiles = [tempboard[i] for i in tp]
            tpid = self.tuple_id(tiles)
            total += LUT[tpid]
            k += 1
        return total / k
