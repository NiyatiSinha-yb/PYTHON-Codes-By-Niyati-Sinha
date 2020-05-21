#modules
import app69_converters #to import the whole module
from app69_converters import kg_to_lbs #importing a function from the module
print(kg_to_lbs(100)) #when we have imported a particular module then we do not need to reference it with the module name
print(app69_converters.lbs_to_kgs(100))#reference to the module


# def lbs_to_kgs(weight):
#   return weight*.45

# def kg_to_lbs(weight):
#   return weight/.45
