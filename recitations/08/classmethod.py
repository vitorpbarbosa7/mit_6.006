class Writer():
    def __init__(self):
        pass

    def write(self, text):
        print(text)

    # bound to the class instance and not the object class instance (no need to instantiate the class in a 
    # object)
    @classmethod
    def write_new(cls, text):
        print(text)

Writer.write_new('Hi hi')
