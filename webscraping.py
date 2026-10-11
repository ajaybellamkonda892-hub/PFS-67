#web scraping
#web scraping is a process of automatically collecting information from websites using a program

#where is web scraping used?
#Extracting article headlines
#collecting product data
#gathering job listing
#collecting publicly available research data 

# 2. Request Module
# The request library allows python to send HTTP request to webisites
#and receive their responses


#sending a request to website

# import requests
# url="https://www.geeksforgeeks.org/"
# response=requests.get(url)
# print(response.status_code)
# print(response.text)

#status code ----> meaning
#200 : requset successfull
#201 :created
#301 :redirected
#403:access forbiden
#404:page not found
#500:server error

# import requests
# url="https://www.geeksforgeeks.org/"
# try: 
#     response=requests.get(url,timeout=10)
#     response.raise_for_status()
#     print(response.text)
# except requests.RequestException as error:
#     print("Request failed: ",error)

#Beautifulsoup:
#request download the HTML,but weed a convinent way to fing a 
#particular elements inside it that's where beautysoup is help

# from bs4 import BeautifulSoup

# html="""
# <html>
# <head>
#     <title>my first website></'title>
# </head>
# <body>
#     <h1>welcome</h1>
#     <p>learn web scraping</p>
# </body>
# </html>
# """
# soup=BeautifulSoup(html,"html.parser")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.h1.get_text())
# print(soup.p.get_text())


# from bs4 import BeautifulSoup

# html = """
# <html>
# <head>
#     <title>my first website</title>
# </head>
# <body>
#     <h1>welcome</h1>
#     <p>learn web scraping</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.h1.get_text())
# print(soup.p.get_text())


#Important beautifulsoup methods
#1.find():finds the first matching element
# soup.find("p")
# #2.find_all(): finds all matching elements
# soup.find_all("p")
# #3.get_text(): extract text
# #4.get() : extract an attribute
# link=soup.find("a")
# print(link.get("href"))


#EXTRACTING website data
# import requests
# from bs4 import BeautifulSoup
# url="https://www.geeksforgeeks.org/"
# response=requests.get(url,timeout=10)
# response.raise_for_status()
# soup = BeautifulSoup(response.text,"html.parser") #soup is used for serch all html elements
# title=soup.title.get_text(strip=True)
# heading=soup.find("h1").get_text(strip=True)
# print("Page title: ",title)
# print("Heading:",heading)

#extract all links
# import requests
# from bs4 import BeautifulSoup
# url="https://amazon.jobs/en/"
# response=requests.get(url,timeout=10)
# response.raise_for_status()
# soup = BeautifulSoup(response.text,"html.parser")
# links=soup.find_all("a")
# for link in links:
#     text=link.get_text(strip=True)
#     url=link.get("href")
#     print("Link text",text)
#     print("URL",url)


# #email automation
# import smtplib
# from email.message import EmailMessage
# #EMAILMESSAGE: creates all email messege
# sender="ajaybellamkonda892@gmail.com"
# password="npbc qetv iyxa myoc"
# receiver="ajaybellamkonda16@gmail.com"
# msg=EmailMessage()
# msg["subject"]="Preparation Email"
# msg["From"]=sender
# msg["To"]=receiver
# msg.set_content("hello this is a preparation using python")
# with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
# #SMTP_SSL: connects to email smtp server using port 465
#     server.login(sender,password)
#     #login : log in using email and app password
#     server.send_message(msg)
#     #send_message()-sends the email
# print("Email sent successfully")


#sending mail with pdfs
# import smtplib
# from email.message import EmailMessage
# #EMAILMESSAGE: creates all email messege
# sender="ajaybellamkonda892@gmail.com"
# password="npbc qetv iyxa myoc"
# receiver="ajaybellamkonda16@gmail.com"
# msg=EmailMessage()
# msg["subject"]="Preparation Email"
# msg["From"]=sender
# msg["To"]=receiver
# msg.set_content("hello this is a preparation using python")
# #attach a pdf or word document
# file_path=r"C:\Users\B.Sandhya\Downloads\Agriculture_Robot_Smart_Farming (1) (1).pdf"
# with open(file_path,"rb") as file:
#     file_data=file.read()
# msg.add_attachment(
#     file_data,
#     maintype="application",
#     subtype="pdf",
#     filename="Agriculture_Robot_Smart_Farming (1) (1).pdf"
# )
# with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
# #SMTP_SSL: connects to email smtp server using port 465
#     server.login(sender,password)
#     #login : log in using email and app password
#     server.send_message(msg)
#     #send_message()-sends the email
# print("Email sent pdf successfully")

#VIRTUAL ASSIANT PROGRAM
import datetime
import webbrowser
print("Hello I'm your virtual assiant.")
while True:
    command=input("\nhow may i help you").lower()
    if "hello" in command or "hi" in command:
        print("hello ajay! how are you?")
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print("current time is:",time)
    elif "date" in command:
        date=datetime.datetime.now().strftime("%d-%m-%Y")
        print("today date is:",date)
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        print("opening google.....")
    elif "your name" in command:
        print("i am your python virtual")
    elif "exit" in command or "bye" in command:
        print("goodbye! have a nice day")
        break
    else:
        print("sorry,i don't understand that command")

