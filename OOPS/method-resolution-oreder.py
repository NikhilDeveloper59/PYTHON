# Method Resolution Order (MRO)
# In multiple inheritance, Python follows C3 Linearization.

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())# D,B,C,A
