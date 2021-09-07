import speech_recognition as sr
import warnings
from translate import Translator

# Initiation
translator= Translator(to_lang="vi")
# Ignore any waring message
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def hearing():
    # Record the audio
    r = sr.Recognizer() # Creating a recognizer object
    
    with sr.Microphone() as source:
        #read the audio data from the default microphone
        print("Hệ thống: Đang nhận diện giọng nói...")
        audio_data = r.record(source, duration=5)
    
    # Use Google speech recognition
    text = ''
    try:
        text = r.recognize_google(audio_data, language="vi")
    except sr.UnknownValueError:
        print('Nhận dạng giọng nói của Google không nghe thấy âm thanh.')
    except sr.RequestError as e :  
        translation = translator.translate(e)  
        print('Yêu cầu kết quả từ lỗi dịch vụ Nhận dạng giọng nói của Google: \n' + translation)
    return text
