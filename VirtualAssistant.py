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
    if "Xin chào" in text:
        robot_brain = "Chào bạn có khỏe không"
    elif "ngày bao nhiêu" in text:
        robot_brain = now.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "mấy giờ" in text:
        robot_brain = now.strftime("%H:%M:%S")
    elif "tạm biệt" in text:
        robot_brain = "Tạm biệt. Hẹn gặp lại."
        print("Ego:" + robot_brain)
        speaking(robot_brain, 'vi')
        break
    elif "hỏi" in text:
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(text, sentences=1)
    else:    
        robot_brain =  get_response(text)

    #Print on the screen    
    print(robot_brain)

    # Speeching
    speaking(robot_brain, 'vi')