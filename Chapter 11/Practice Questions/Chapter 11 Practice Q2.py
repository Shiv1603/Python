class Animals():
    pass

class Pets(Animals):
    pass

class Dogs(Pets):

    def bark(self):
        print("Woaf woaf..")

d=Dogs()
d.bark()