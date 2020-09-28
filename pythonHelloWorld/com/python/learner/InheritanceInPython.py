class Mammals:


    def walk(self):
        print('Mammal Walk')


class Dog(Mammals):
 #   pass

    def bark(self):
        print('Dog says baw.. baw...!')

    def walk(self):
        print('Dog Walks')


class Cat(Mammals):
  #  pass

    def meow(self):
        print('Cat says Meow .. Meow .. !')

    def walk(self):
        print('Cat Walks')

mammal=Mammals()
mammal.walk()

dog1=Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.walk()
cat1.meow()
