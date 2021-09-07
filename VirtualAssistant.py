import wikipedia 
from typing import Text
from nltk import text
from datetime import datetime
from chat import get_response, bot_name
from speeching import speaking
from hearing import hearing
import sys
sys.path.append('D:\\projects\\Automation')
from open_app import Script

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
        speaking(robot_brain, 'vi') # Speeching
    elif "ngày bao nhiêu" in text:
        robot_brain = now.strftime("Hôm nay là ngày %d tháng %m năm %Y")
        speaking(robot_brain, 'vi') # Speeching
    elif "mấy giờ" in text:
        robot_brain = now.strftime("%H:%M:%S")
        speaking(robot_brain, 'vi') # Speeching
    elif "tạm biệt" in text:
        robot_brain = "Tạm biệt. Hẹn gặp lại."
        print("Ego:" + robot_brain)
        speaking(robot_brain, 'vi') # Speeching
        break
    elif "hỏi" in text:
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(text, sentences=1)
        speaking(robot_brain, 'vi') # Speeching
    elif "mở" in text:
        Script.run()
    else:    
        robot_brain =  get_response(text)
        speaking(robot_brain, 'vi') # Speeching

    #Print on the screen    
    print(robot_brain)