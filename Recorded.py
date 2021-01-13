from pydub import AudioSegment
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import speech_recognition as sr
r = sr.Recognizer()

# Conveerting mp3 to wav and store it

src = "D:\\Speech_Project\\test_audio.mp3"
dest = "D:\\Speech_Project\\test_audio.wav"

print("Start Conversion")
sound = AudioSegment.from_mp3(src)
sound.export(dest, format="wav")

#Speech Recognition and store it in txt file

audio = 'D:\\Speech_Project\\test_audio.wav'

with sr.AudioFile (audio) as source:
    print("Start Analyzing")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        file1 = open(r"D:\Speech_Project\test.txt","w")
        print("Analyzing Done, Thank You")
        file1.writelines(text)
        file1.close()
    except:
        print("Sorry We Not recognize You")

# remove stop words from txt and store it again in txt

input_str = ""
with open("D:\\Speech_Project\\test.txt","r") as f:
    for lines in f.readlines():
        input_str=input_str+lines
        
stop_word = set(stopwords.words('english'))
token = word_tokenize(input_str)
result = [i for i in token if not i in stop_word]

file1 = open(r"D:\Speech_Project\Final_Text\test.txt","w")
print("Your File Is Saved In Our Database")
file1.writelines(result)
file1.close()