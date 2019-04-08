import time, keyboard, webbrowser, pyautogui, pyperclip
from selenium import webdriver
from pynput.keyboard import Key, Controller
import lxml.html as lh
import lxml.html.clean as clean
keyboard = Controller()
import requests
from bs4 import BeautifulSoup

# input the airport list in list_depart and list_destination, and also the complete names in dico_corresp. 
# input the dates and hours in the loop below
# if no flight is found, it will return the URL.

dico_corresp = {"DUB":"dublin",
                "BCN":"barcelone",
                "CPH":"copenhague",
                "PRG":"prague",
                "NAP":"naples",
                "PMO":"palerme",
                "CAG":"cagliari",
                "CLY":"calvi",
                "TLV":"tel aviv"}

list_depart = ["CDG","ORY"] #from where we want to fly 
list_destination = ["DUB","BCN","PMO"] #where we may want to go

#"AGA","CMN","FEZ","RAK","NDR","OUD","RBA","TNG","TTU","VIL","EUN","DJE","TUN"
#"DUB","BCN","CPH","PRG","NAP","PMO","CAG","CLY","BIA","AJA","FSC"]

final_list = []
final_list_before_question =[]
final_list_question = [] #the list that contains all data, joined by "?"


for aeroport_depart in list_depart: #we start with the first departure airport, and try each destination. And then we go to the 2nd
    
    for destination in list_destination: #for each destination, we copy the infos in a variable "all infos", and make a list ou of it
        aero_depart = aeroport_depart # takes the info from the first loop
        aero_arrivee = destination #takes the info from this current loop
        date_depart = "2019-05-01"
        heure_depart = "1800-2400"
        date_retour = "2019-05-10"
        heure_retour = "1800-2400"
        all_infos = "empty"

        # open google flights in firefox, go to the url with all the parameters, and scroll down a bit so that we can access the flights and copy them
        url = 'https://www.google.fr/flights/#flt='+ aero_depart +"."+ aero_arrivee + "."+ date_depart+"*"+aero_arrivee+"."+aero_depart +"." + date_retour +";c:EUR;e:1;s:0*0;dt:"+heure_depart+";at:"+heure_retour+";sd:1;t:f"
        #browser = webdriver.Firefox()
        try:
            browser = webdriver.Chrome()
        except:
            browser = webdriver.Chrome('C:\\Users\\gila\\AppData\\Local\\Google\\Chrome\\chromedriver.exe')

        browser.get(url)
        content=browser.page_source
        cleaner=clean.Cleaner()
        content=cleaner.clean_html(content) 
        doc=lh.fromstring(content)

        soup = BeautifulSoup(html_doc, 'html.parser')
        time.sleep(3)
        pyautogui.press('down')
        pyautogui.press('down')
        time.sleep(1)
        
        #move the mouse to copy the flights info, ctrl c them into the "all_infos" variable, and the close firefox
        pyautogui.moveTo(263, 663)
        time.sleep(1)
        pyautogui.dragTo(1135, 710, 1, button='left')
        time.sleep(1)
        pyperclip.copy("")
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        time.sleep(1)
        all_infos = pyperclip.paste()
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.f4)
        
        #we create a list that will contain all the infos from the flight.
        list_allinfo= []
        list_allinfo= all_infos.split("\n") #each time there is a new line, we split that into an item of the list
        
        #we clean the list, add the url to it, and add all this to a new list "final_list"
        cleaned_all_info_list = []
        for element in list_allinfo:
            if element.strip() != '':
                cleaned_all_info_list.append(element.strip())

        cleaned_all_info_list.append(url)
        final_list.append(cleaned_all_info_list)
        
        # for each list in the final_list, we merge the flight carrier into 1 item in the case there's more than 1
        for sublist in final_list:
            if len(sublist) <2 : #if it's only an url we skip
                continue
            else:
                while "min" not in sublist[2]: #if "min" (minutes) is not the 3rd item, then that means we need to merge the previous items into one
                    print("\n") 
                    print("----------")
                    print("found one!")
                    print("----------")
                    print("\n")
                    print("here it is before:")
                    print(sublist)
                    print("\n")
                    sublist = [sublist[0]]+['-'.join(sublist[1:3])]+sublist[3:] #we take the 1st element of the list, merge the 2nd to 4th, and then add the rest
                    sublist[1] = sublist[1].replace(",","") #remove the comma
                    print("here it is after:")
                    print(sublist)
                    print(type(sublist))
                    print("\n")
        final_list_before_question.append(sublist) #we add all these lists into another list



for sublist in final_list_before_question:
        final_list_question.append("?".join(sublist)) #all the elements are merged into one with a ? as a separator, so that we can split the columns easily later in google sheets


#open google sheets
browser = webdriver.Chrome()
browser.get('https://docs.google.com/spreadsheets/d/14vG9O1Q3MCNytqJZJwPN8xdvP9mCJQTGws3sDJV9I-4/edit?usp=sharing')
time.sleep(7) #wait for it to load

# we copy line by line each element of the final_list_question in google sheets
for sublist in final_list_question:
    pyperclip.copy(str(sublist))
    time.sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(1)

#we add a new colums to the left, that will contain the name of the destination
pyautogui.moveTo(272, 144)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#go back to A1
time.sleep(0.5)
keyboard.press(Key.ctrl)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.release(Key.ctrl)

#write all the destination names line by line
time.sleep(0.5)
for i in list_depart:
    for destination in list_destination:
        destination_long_name =  dico_corresp[destination]
        keyboard.type(destination_long_name)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.5)

#select column B and then go to the google sheets options to separate the content into multiple columns with "?" as a separator
pyautogui.moveTo(197, 233)
pyautogui.click()
pyautogui.moveTo(393, 144)
pyautogui.click()
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)
keyboard.press('?')
keyboard.release('?')