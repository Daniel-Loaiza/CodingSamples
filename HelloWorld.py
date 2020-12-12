def greet(who="World"):
    """Prints a greeting to the user

    >>> greet(Pedro)
    Hello Pedro!
    """
    print ("Hello "+who+"!")

if __name__=="__main__":
    greet() #Calls the function to print the default option
    greet(who='amigo') #Calls the function to print with a specific argument 
    name=input("Hey, What's your name?\n")
    greet(name) #Calls the function to print with a specific argument
    help(greet) #Prints the Docstrings of the function