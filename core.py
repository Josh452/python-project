#Josh's lit bot
class icore():
    def start():
        #Vertion and welcome meassage
        v = "0.69"
        print("Welcome User to Josh's lit bot. Vertion %s" % (v))
        #Get name
        hated_names = ("aden")
        name = input("Hello, what is your name? \n")
        if name==hated_names:
            print("Piss of :)")


    def end():
        exit = input("Do you want to exit? y or n \n")
        no = "n" or "N"
        yes = "y" or "N"
        if exit==no:
            print("-Info- Restarting")
            icore.start()

        if exit==yes:
            print ("-Info- Exiting")
        else:
            print("-Info- Not valid input")
            icore.end()
            