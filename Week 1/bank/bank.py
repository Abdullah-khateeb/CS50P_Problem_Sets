answer = input("Greeting: ")
new_answer = answer.lower().strip()
# check if the answer has "hello"
if "hello" in new_answer:
    print("$0")
    #check if answer starts with"h"
elif "h" == new_answer[0]:
    print("$20")
else:
    print("$100")
