def send_message(message):
    blocked_words = ["spam", "blocked", "banned"]
    #loop below
    for word in blocked_words:
        if word in message:
            if len(message) < 10:
                return "Message is too short and might contain spam"
            return "Message might contain spam"
    
    if len(message) < 10:  # Check if message is  short
        return "Message is short"
    return "Message sent"
#codes to test if it works
print(send_message("Hi"))            
print(send_message("This is spam"))    
print(send_message("Hello world!"))    
print(send_message("This is blocked")) 
