class Person():
   def set_name(self, name):   self.n = name
   def get_name(self):   return self.n
   def greet(self):    print("Hello, world! I'm {}.".format(self.n))


wcc = Person()
tgw = Person()
wcc.set_name('吴长城')
tgw.set_name('吴帅')
wcc.greet()
tgw.greet()


print(wcc.n)