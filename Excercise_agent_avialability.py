import datetime
datetime=datetime.datetime.now()
class agent_():
    def welcome(self):
        print("Welcome to our help desk!")
    def issue(self,raiseissue):
        print("Please wait Your issue has been taken and passed to our agent.")
    def start_time(self):
        print("Our agent will be avialable at {}time.Please wait for that time.".format(str(datetime)))
    def answer_time(self):
        print("Our agent working on your issue.")
    def resolved(self):
        print("Your issue has been resolved.")
def abonded_time():
    print("Customer has left at {} ".format(str(datetime)))           
def recall():           
    agent_availability=agent_()
    agent_availability.issue(input("Please Provide Your Issue:"))
    agent_availability.start_time()
    agent_availability.answer_time()
    agent_availability.resolved()    
def customer_reply(reply):
        if reply=="yes":
            print("Tell me your querie.")
            return recall()
        else:
            print("Thank you for contacting us.")
            
recall()
print("Thank you for contacting us.")
customer_reply(input("If you have any queries please enter yes:"))
abonded_time()