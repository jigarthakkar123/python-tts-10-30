class Base:
    def show(self):
        print("Show From Base")
class Derived1(Base):
    def show(self):
        super().show()
        print("Show From Derived1")
class Derived2(Base):
    def show(self):
        super().show()
        print("Show From Derived2")
class SubDerived(Derived1,Derived2):
    def show(self):
        super().show()
        print("Show From SubDerived")

s1=SubDerived()
s1.show()

