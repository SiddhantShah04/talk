import speech_recognition as r
import pyttsx3
import wolframalpha
import wikipedia
class voicePrint:
    def __init__(self):
        self.voice = r.Recognizer()
        
    def set_Microphone(self,index):
        self.mic = r.Microphone(device_index = index)
        
    def mic_Listen(self):
            with self.mic as source:
                self.voice.adjust_for_ambient_noise(source,duration= 0.6)
                print("say something")
                self.audio = self.voice.listen(source)
               
    def display(self):
        self.text = self.voice.recognize_google((self.audio))
        return(self.text)

    def indexfind(self):
        return(self.mic.list_microphone_names())
      
    def textChecker(self): 
        try:
            self.text_Data = self.text
        except:
            self.text_data = "sorry but i am not understanding"
        
    def playaudio(self,textSpeaker):
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.setProperty('rate', 140) 
        engine.say(textSpeaker)
        engine.runAndWait()

    
    def wolframalphaCon(self,app_id,querry):
        #self_id=XWH3RH-KE5EVL4W5Q
        client = wolframalpha.Client(app_id)
        res = client.query(querry)
        return(next(res.results).text)

    def wiki(self,search):
        return(wikipedia.summary(search, sentences=2))
        

if __name__ == "main":
    
    talk = voicePrint()

    # Asking for language input
    language = input("If you need english press enter or enter the language.")
    if language:
        talk.language = language
    else:
        talk.language = 'eng'
       
    talk.set_Microphone(2)
    talk.mic_Listen()

