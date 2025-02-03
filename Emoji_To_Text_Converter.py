#import library
import emoji

def emoji_to_text(userInput):
    converted_text = emoji.demojize(userInput)
    return converted_text
     

if __name__=="__main__":
    userInput = input("Enter your Text: ")

    output_text = emoji_to_text(userInput)

    print("Input Text: ", userInput)
    print("Output Text: ", output_text)
