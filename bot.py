import random
import string
import smtplib
import os
import json
import imghdr
from email.message import EmailMessage
from datetime import datetime
import uuid
#QR module import
import qrcode
from PIL import Image
import cv2 as cv

def find_all(name, path):
    result = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            result = 1
    return result
class tools :
        def id_number_genrator(self):
            id_number = uuid.uuid1()
            print(id_number)
            return id_number

            
        def retrieve(self,users,number_of_users,type_alram):
            print("working")
            print(number_of_users)
            try:
                array_of_emails=[]
                for i in users:
                    array_of_emails.append(i["email"])
                for i in range(0,number_of_users):
                    email_address  ="dummyjackson8@gmail.com"
                    email_password  ="dummy101@1"      
                    email_recieve = (array_of_emails[i])
                   
                    msg = EmailMessage()
                    msg['Subject'] = 'Security Breach'
                    msg['From'] = email_address
                    msg['To']= email_recieve
                    msg.add_alternative(f"""
                            <!DOCTYPE html>
                            <html>
                                <body>
                                    <h1 style ="color:#ff0000;">Security Breach</h1> 
                                    <h2 style ="color:#ff0000;">{type_alram}</h2>
                                    <p>There has been a breach.</p>
                                    <p>This email has been sent to inform you that a breach of the type above has occured on shool campus with has be idetified as a danger to persons of this facility</p>
                                    <p>Please stand by for instruction and make plans to leave school grounds after evcuation</p>
                                    <p style ="color:#ff0000;">Please parents make plan to fecth your children</p>
                                    <p>Please  feel safe under Salus</p>
                                    <p> We care about your well being </p>
                                    <p>Yours sincerly</p>
                                    <p>The Salus team</p>
                                </body>
                            </html>
                            """,subtype= "html")                    
                    files = ["saluswithname.jpg"]
                    for images in files:
                        with open(f"{images}","rb") as image :
                            file_data = image.read()
                            file_type = imghdr.what(image.name)
                            file_name= image.name
                            msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name) 
                    with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                        smtp.login(email_address,email_password)
                        smtp.send_message(msg)
            except Exception as e :
                 print("[retrieve] retrieve() error:",e)