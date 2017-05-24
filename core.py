

#Josh's lit bot
class icore():
    def start():
        #Vertion and welcome meassage
        v = "0.69"
        print("Welcome User to Josh's lit bot. Vertion %s" % (v))
        #Get name
        hated_names = ("aden")
        name = input("Hello, what is your name? \n")
        print("Hello %s!" % name)
        print("I like you already. Lets get to know you")
        if name==hated_names:
            print("Piss of :)")
            sys.exit

    def yn(q, yr, nr):
        print("type y (yes) or n (no)")
        ask = input(q)
        no = "n" or "N"
        yes = "y" or "N"
        if ask==yes:
            print (yr)
            return
        if ask==no:
            print(nr)
            return
        else:
            print("invaid input. try again.")
            icore.yn(q, yr, nr)

    def type(q, a, af):
        ak = input(q)
        print(a + " " + ak + af)
