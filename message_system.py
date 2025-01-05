def send_message(prvmessage):
    if not prvmessage:
        return "Message cannot be empty"
    if "spam" in prvmessage:
        return "Message might be spam"
    return "Message sent successfully"
print(send_message("Hello!"))        
print(send_message("This is spam"))  
print(send_message(""))              
