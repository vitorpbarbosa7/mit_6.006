def ht(A):
    if A: return A.ht
    else: return -1
class BN:
    def __init__(A, x):
        A.it = x
        A.lf = None
        A.rh = None
        A.pr = None
        A.s_up()
    def s_up(A):
        A.ht = 1 + max(ht(A.lf), ht(A.rh))
    def s(A):
        return ht(A.rh) - ht(A.lf)
    def s_iter(A):
        if A.lf: yield from A.lf.s_iter()
        yield A 
        if A.rh: yield from A.rh.s_iter()
    def s_first(A):
        if A.lf:  return A.lf.s_first()
        else: return A
    def s_last(A):
        if A.rh: return A.rh.s_last()
        else: return A
    def sss(A):
        if A.rh: return A.rh.s_first()
        while A.pr and (A is A.pr.rh):
            A = A.pr
        return A.pr
    def pred(A):
        if A.lf: return A.lf.s_last()
        while A.pr and (A is A.pr.lf):
            A = A.pr
        return A.pr
    def sib(A, B):
        if A.lf:
            A = A.lf.s_last()
            A.rh, B.pr = B, A
        else:
            A.lf, B.pr = B, A
        A.mn()
    def sia(A, B):
        if A.rh:
            A = A.rh.s_first()
            A.lf, B.pr = B, A
        else:
            A.rh, B.pr = B, A
        A.mn()
    def s_delete(A):
        if A.lf or A.rh:
            if A.lf: B = A.pred()
            else: B = A.sucessor()
            A.it, B.it = B.it, A.it
            return B.s_delete()
        if A.pr:
            if A.pr.lf is A: A.pr.lf = None
            else: A.pr.rh = None
        return A
    def s_rot_rh(D):
        assert D.lf
        B, E = D.lf, D.rh
        A, C = B.lf, B.rh
        D, B = B, D
        D.it, B.it = B.it, D.it
        B.lf, B.rh = A, D
        D.lf, D.rh = C, E
        if A: A.pr = B
        if E: E.pr = D
        B.s_up()
        D.s_up()
    def s_rot_lf(B):
        assert B.rh
        A, D = B.lf, B.rh
        C, E = D.lf, D.rh
        B, D = D, B
        B.it, D.it = D.it, B.it
        D.lf, D.rh = B, E
        B.lf, B.rh = A, C
        if A: A.pr = B
        if E: E.pr = D
        B.s_up()
        D.s_up()
    def mn(A):
        A.rb()
        A.s_up()
        if A.pr: A.pr.mn()
    def rb(A):
        if A.s() == 2:
            if A.rh.s() < 0:
                A.rh.s_rot_rh()
            A.s_rot_lf()
        elif A.s() == -2:
            if A.lf.s() > 0 :
                A.lf.s_rot_lf()
            A.s_rot_rh()
tree = BN('A')
tree.sib(BN('B'))
tree.sib(BN('C'))
