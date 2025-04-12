import numpy as np

class nTupleNewrok:
    def tuple_id(self, values):
        values = values[::-1]
        k = 1
        n = 0
        for v in values:
            n += v * k
            k *= self.TARGET_PO2
        return n

    def V(self, board):
        vals = []
        for i, (tp, LUT) in enumerate(zip(self.TUPLES, self.LUTS)):
            tiles = [board[i] for i in tp]
            tpid = self.tuple_id(tiles)
            vals.append(LUT[tpid])
        return np.mean(vals)
