#@author:Akhil P Jacob
#HLRobotics-Automation
import speech_recognition as sr

def sR():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            print("HLEngine:You said: " + r.recognize_google(audio))
            content = r.recognize_google(audio)
            return(content)

        except sr.UnknownValueError:
            return ("HLEngine:----------------waiting----------------")


        except sr.RequestError as e:
            return ("HLEngine:Could not request results from Google Speech Recognition service; {0}".format(e))
    except:

        return ('HLEngine:microphone not connected')


def sentiment(param):
    import nltk
    # import TextBlob
    from textblob import TextBlob
    blob1 = TextBlob(param)
    return (blob1.sentiment.polarity)



