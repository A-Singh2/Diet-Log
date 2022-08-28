#Food class is in another file "Food.py"
from Food import Food

def main():
  #Create a new "Food" object with default attributes
  #Printing the defaul attributes of the new Food Object            "ChickenBreast"
  ChickenBreast = Food()
  print("Here is the default chicken breast attributes: ")
  print(ChickenBreast.get_name())
  print(ChickenBreast.get_calories())
  print(ChickenBreast.get_protein())
  print(ChickenBreast.get_fat())
  print(ChickenBreast.get_carbs())
  
# asking user to set new attributes to Food object "ChickenBreast"
  calories = input("Enter the number of calories for chicken breast: ")
  protein = input("Enter the number of protein for chicken breast: ")
  fat = input("Enter the amount of fat for chicken breast: ")
  carbs = input("Enter the number of carbs for chicken breast: ")

  # Setting the ChickenBreast info from user input
  ChickenBreast.set_calories(calories)
  ChickenBreast.set_protein(protein)
  ChickenBreast.set_fat(fat)
  ChickenBreast.set_carbs(carbs)

  # Printing the new ChickenBreast info
  print("Here is the chicken breast information: \n")
  print("Calories: " + str(ChickenBreast.get_calories()) + "\n" +
    "Protein: " +  str(ChickenBreast.get_protein()) + "\n" +
    "Fats: " + str(ChickenBreast.get_fat()) + "\n" +
    "Carbs: " + str(ChickenBreast.get_carbs()) +"\n")

  
# Calling the main function
if __name__== "__main__":
  main()