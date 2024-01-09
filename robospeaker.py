import pyttsx3
while True:
    if __name__ == "__main__":
        x = input("Enter the thing you want to say: ")
    
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        
        # Say the input
        engine.say(x)
        if x=="q":
            print("bye! bye!")
            break
        # Wait for the speech to finish
        engine.runAndWait()
