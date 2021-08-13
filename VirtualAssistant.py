import wikipedia 
from typing import Text
from nltk import text
from datetime import datetime
from chat import get_response, bot_name
from speeching import speaking
from hearing import hearing

#initialize the variable
robot_brain = ""
now = datetime.now()

while True:
    #hearing
    text = hearing()
    print("Bạn: " + text)
    #Understanding
    if text == "":
        robot_brain = "Tôi đang lắng nghe bạn đây"
    elif "Xin chào" in text:
        robot_brain = "Chào bạn có khỏe không"
    elif "ngày bao nhiêu" in text:
        robot_brain = now.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "mấy giờ" in text:
        robot_brain = now.strftime("%H:%M:%S")
    elif "tạm biệt" in text:
        robot_brain = "Tạm biệt. Hẹn gặp lại."
        print("Ego:" + robot_brain)
        break
    elif text == "I can't recognize your voice.":
        print("Hệ thống: Tôi không nhận ra giọng nói của bạn.")
        robot_brain = "Tôi không nghe thấy gì cả. Bạn có thể nói lại được không."
    elif "hỏi" in text:
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(text, sentences=1)
    else:    
        robot_brain = f"{bot_name}: {get_response(text)}\n\n"

    #Print on the screen    
    print(robot_brain)

    # Speeching
    speaking(robot_brain, 'vi')