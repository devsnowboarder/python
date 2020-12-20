#this is a car example

class car():
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


audi = car("audi a4","blue")
ferrari = car ("ferrari 488", "green")
ford = car("F150","black")
toyota = car("Supra","white")audi.show()
ferrari.show()
ford.show()
toyota.show()
