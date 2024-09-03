from time import time
import random as ran
# error count this function
def error(mainpra, userpra):
    mstk = 0
    for i in range(len(mainpra)):
        try:
            if mainpra[i] != userpra[i]:
                mstk += 1
        except:
            mstk += 1
    return mstk
# Time calulatiuion this finction 
def time_need(time_s, time_e, userin):
    time_tot = time_e - time_s
    tim_nice = round(time_tot, 2)
    speed = len(userin) / tim_nice
    return round(speed)

def feedback(speed, errors):
    if speed > 40 and errors == 0:
        return "Outstanding! You're a typing master!"
    elif speed > 30 and errors <= 2:
        return "Great job! Just a few minor errors."
    elif speed > 20:
        return "Good work! Keep practicing to improve your speed."
    else:
        return "Don't worry, practice makes perfect! Keep going."

while True:
    chk = input("Ready to start? Type 'yes' or 'no': ").strip().lower()
    
    if chk == "yes":
        test = [
            "Second long one red point found girl enough does began stop give show now him after still any their kind car open once people them also it turn just hand old grow be head upon plant an next seem great these some find great or house tell then but still see page both red those might this he change change over large side follow important talk near girl get big once until spell may something than hard without at life few white how play part at would stop sea always",
            "Success can mean many things and it's more than just a job. Sure, we all want to achieve great things in our careers but there is something to be said for good character as well. The impact that you have on other people is huge. So, how do you leave your mark on society, stay true to yourself and reach your life goals? The answer could be as simple as daring to step out. That's what a lot of these iconic people have done and they haven't even let failures get in the way.",
            "When it comes to pursuing our dreams, two of our enemies are fear and doubt. As Franklin D. Roosevelt has said, 'The only thing we have to fear is fear itself.' When we have courage and perseverance, we can accomplish many great things.",
            "We are lucky to have those who have gone before us—teaching us from their life experiences. These famous quotes summarize those experiences in short impactful phrases that are a great source of inspiration."
        ]

        test1 = ran.choice(test)
        print("\n------------------------ Typing Speed Test ------------------------")
        print(test1)
        print("\n")

        time_1 = time()
        testinput = input("Start typing the text above: ")
        time_2 = time()

        speed = time_need(time_1, time_2, testinput)
        errors = error(test1, testinput)
        

        print("\nYour Typing Speed:", speed, "W/Sec")
        print("Errors:", errors)
        print(feedback(speed, errors))

    elif chk == "no":
        print("Thank you for visiting! Keep practicing and come back soon.")
        break
    else:
        print("Invalid input, please type 'yes' or 'no'.")
