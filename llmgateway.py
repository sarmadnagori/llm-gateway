
import httpx
from typing import Any

URL= "http://localhost:11434/api/chat"
MODEL="llama3.2"


def make_message(role:str,content:str) -> dict[str, str]:

   return {"role":role, "content":content}

    

def build_payload(messages:list[dict[str,str]])->dict[str,Any]:
    

    payload= {
        
        "model":MODEL,
        "messages":messages,
        "stream":False
    }
    return payload


def send_chat(payload:dict[str,Any])->dict[str,Any]:
    response = httpx.post(
        URL, 
        json=payload,
        timeout=120.0
        )
    response.raise_for_status()
    return response.json()


def extract_reply(response:dict[str,Any])->str:
    reply=response["message"]["content"]

    return reply

# Main LOOP
messages=[]

user_question= make_message("user","How many planents in the solar system")

messages.append(user_question)





payload=build_payload(messages)

response=send_chat(payload)

reply= extract_reply(response)

print(reply)





