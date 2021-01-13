import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        file1 = open(r"D:\Speech_Project\Audio_Text\test.txt","w")
        file1.writelines(text)
        file1.close()
    except:
        print("Sorry We Not recognize You")

input_str = ""
with open("D:\\Speech_Project\\Audio_Text\\test.txt","r") as f:
    for lines in f.readlines():
        input_str=input_str+lines
        
stop_word = set(stopwords.words('english'))
token = word_tokenize(input_str)
result = [i for i in token if not i in stop_word]

file1 = open(r"D:\Speech_Project\Final_Text\test.txt","w")
file1.writelines(result)
file1.close()