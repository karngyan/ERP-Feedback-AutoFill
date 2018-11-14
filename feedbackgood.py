#!/usr/bin/env python

#author: @karngyan

from selenium import webdriver
import sys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

webbrowser = webdriver.Firefox()
# webbrowser = webdriver.Chrome(r'/home/karn/Downloads/chromedriver/chromedriver')
webbrowser.get(r"http://115.114.127.54:8080/psp/bitcsprd/EMPLOYEE/HRMS/")

# sleep(5)

search_form_password = None
search_form_username = None
while search_form_password == None or search_form_username == None:
    search_form_username = webbrowser.find_element_by_id('userid')
    search_form_password = webbrowser.find_element_by_id('pwd')



# search_form_username.send_keys(open(r"username",'r').read())
# search_form_password.send_keys(open(r"pass",'r').read())
username = str(sys.argv[1])
password = str(sys.argv[2])

search_form_username.send_keys(username)
search_form_password.send_keys(password)


search_form_submit = webbrowser.find_element_by_name('Submit')
search_form_submit.click()


webbrowser.get(r'http://115.114.127.54:8080/psp/bitcsprd/EMPLOYEE/HRMS/c/B_STDNT_SLF.B_OFFRD_CRSE_CMP.GBL?PORTALPARAM_PTCNAV=B_STUDENT_FEED_BACK&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=B_FACULTY_FEEDBACK&EOPP.SCLabel=Feedback&EOPP.SCPTfname=B_FACULTY_FEEDBACK&FolderPath=PORTAL_ROOT_OBJECT.B_FACULTY_FEEDBACK.B_STUDENT_FEED_BACK&IsFolder=false')


nsubjects = int(sys.argv[3])

webbrowser.switch_to.frame(webbrowser.find_element_by_id('ptifrmtgtframe'))#Fucker Dimaag ka dahi kr diya tha iframe ne

num = 0
while(num < nsubjects):
    subject = webbrowser.find_element_by_id(f'B_FEEDBACK_WRK_B_CLICK_HERE${num}')
    if(subject.text.strip() == 'View'):
        num+=1
        continue
    subject.click()
    sleep(2)
    webbrowser.switch_to.default_content()
    sleep(2)
    webbrowser.switch_to.frame(webbrowser.find_element_by_id('ptifrmtgtframe'))
    print(webbrowser.page_source)

    expand_all = webbrowser.find_element_by_id('B_FEEDBACK_WRK_COLLAPSE_ALL_PB')
    expand_all.click()
    sleep(3)
    #good feedback + very less bad + i dont want to go and do for each (time ni hai bhai)
    buttons = webbrowser.find_elements_by_css_selector("input[type='radio'][value='1']")
    #thik thak feedback
    # buttons = webbrowser.find_elements_by_css_selector("input[type='radio'][value='2']")

    for i in buttons:
        i.click()

    submit_btn = webbrowser.find_element_by_id('B_FEEDBACK_WRK_SUBMIT_BTN')
    submit_btn.click()
    sleep(3)
    accept = webbrowser.find_element_by_id('#ICYes')
    accept.click()
    sleep(3)
    num+=1
webbrowser.quit()
