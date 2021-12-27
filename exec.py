# 안내판
import pickle
import os.path as Path
from datetime import *

message = ''
def FileIsFile(file):
    if Path.isfile(file):
        return 1
    else:
        return -1
clock = datetime.now()
day = clock.day
file = "_board_{}.md".format(day) # 날짜도 같이
tf = FileIsFile(file)
if tf == 1:
    print("-- 안내 --")
    with open(file, "rb") as r:
        message = pickle.load(r)
        print(message)
else:
    print("-- 안내판 프로그램 --")
    message = str(input("메시지: "))
    # 문자열 앞에다가 문자(=>)를 같이 입력해주는 기능 추가해요
    mainMessage = "=> " + message + " <="
    print(mainMessage)
    with open(file, "wb") as w:
        _log_ = pickle.dump(mainMessage, w) # 파일에 기록한다

