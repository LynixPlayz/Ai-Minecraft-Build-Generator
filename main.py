from g4f.client import Client
from g4f.cookies import set_cookies
import g4f
import json
import time
import pyautogui

build = input("type EXACTLY what you want the ai to build: ")

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": '''You will respond to my prompts exactly as I specifiy, I will send you a minecraft build as input and You will send a map in this form(variables will be put like this /%i want you to fill this in%/) {"layer": /%build number%/, "coords": [[/%x_coords%/, /%y_coords%/, /%block%/, /%z_coords%/], [/%x_coords%/, /%y_coords%/, /%block%/, /%z_coords%/]]}. , an example for one of the [/%x_coords%/, /%y_coords%/, /%block%/ ,/%z_coords%/] would be (1, 5, "minecraft:white_wool", 0) you will treat every prompt as a different object and you will not use any past builds for information. If the prompt is something you cannot do (ex. using a past object) then you can return "null" without the quotes and nothing else. Exclude any information from past builds and generate each prompt as an independent object. Do not reference or use any data from previous prompts or builds. Here is your first prompt "''' + build + '''" you will send ONLY the json and make it in code block markdown format, you will also NOT send any other information other than the provided prompt, you will also always send the full build and iff you cannot you will say Error: cannot send full build  and nothing else, but use a maximum of 200 blocks and only stop if you go over that'''}],
    provider=g4f.Provider.You
)
a = response.choices[0].message.content.replace("```json","").replace("```", "")

print(a[a.find("{"):a.rfind('}')])
raw = json.loads(a[a.find("{"):a.rfind('}') + 1])
l = 0
commandArray = []
for i in raw["coords"]:
    print(i)
    commandArray.append(f'/setblock ~{i[0]} ~{i[1]} ~{i[3]} {i[2]}')
    l += 1
print(commandArray)
print("waiting 5 seconds before sending, be tabbed into the game with your chat not open")
time.sleep(5)
print("Starting..")
for i in commandArray:
    pyautogui.keyDown("t")
    time.sleep(0.00002)
    pyautogui.keyUp("t")
    pyautogui.typewrite(i)
    pyautogui.keyDown("enter")
    time.sleep(0.00002)
    pyautogui.keyUp("enter")