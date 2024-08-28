#MadLib.py
#Name:Aaron Spicka
#Date:8/28/24
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("enter a noun: ")
  name1 = input("enter a name: ")
  name2 = input("enter a name: ")
  noun2 = input("enter a noun: ")
  noun3 = input("enter a noun: ")
  noun4 = input("enter a noun: ")
  #Print the story with the user supplied words.
  print("Me and my friends " + name1 + " and " + name2 + " drove to " + noun2 + " in a " + noun1 + " but " + name1 + " forgot his " + noun3 + " in his " + noun4) 
  
  
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
