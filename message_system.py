def send_message(message):
    if not message:  
        return "Message cannot be empty"
    if "spam" in message: 
        return "Message might be spam"
    return "Message sent successfully" 

print(send_message("Hello!"))        
print(send_message("This is spam"))  
print(send_message(""))               
print(send_message("Test message")) 
print(send_message("Spam content"))  
