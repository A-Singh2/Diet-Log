class Food:
  
  #Every food object should have the name,calories,protein,fat,            and carb attributes
  #Variables are private and have to be accessed using getters and         setters
  
  def __init__(self):
    self.__name = "Name place-holder"
    self.__calories = 0
    self.__protein =  0
    self.__fat = 0
    self.__carbs = 0
    
  # getter methods return the attributes of an object
  def get_name(self):
    return self.__name
  def get_calories(self):
    return self.__calories
  def get_protein(self):
    return self.__protein
  def get_fat(self):
    return self.__fat
  def get_carbs(self):
    return self.__carbs
    
  # setter methods set the attributes of an object
  def set_name(self, name):
    self.__name = name
  def set_calories(self, calories):
    self.__calories =calories
  def set_protein(self, protein):
      self.__protein = protein        
  def set_fat(self, fat):
    self.__fat = fat
  def set_carbs(self, carbs):
    self.__carbs = carbs
        
 