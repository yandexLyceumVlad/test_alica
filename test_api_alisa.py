from requests import post, get
import json

request_alisa = {
  "request": {
    "command": "закажи пиццу на улицу льва толстого, 16 на завтра",
    "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра"
  },
  "session": {
    "new": True,
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
  },
  "version": "1.0"
}

#print(post('https://test-alisa-md.herokuapp.com', json=request_alisa).json())
#print(post('http://127.0.0.1:5000/', json=request_alisa).json())
print(post('http://7c67-5-175-109-98.ngrok.io/', json=request_alisa).json())
