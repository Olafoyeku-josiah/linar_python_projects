
from tkinter import Tk ,ttk
from tkinter import *
from PIL import Image,ImageTk

import requests
import json



"""As a result of the currency converter api used
 ...the code can only be executed using a stable internet connection"""
#colors to be used 
colour0="#FFFFFF"# white
colour1="#333333" # black
colour2="#FF0000" #red

window=Tk()
window.geometry('300x320')
window.title('a converter')
window.configure(bg=colour0)
window.resizable(width=False,height=False)


top= Frame(window, width=300, height=60, bg=colour2)
top.grid(row=0,column=0)

main=Frame(window, width=300, height=260, bg=colour0)
main.grid(row=1,column=0)


def conversion():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1=combo1.get()
    currency_2=combo2.get()
    amount=value.get()

    if currency_2=="NGN":
        symbol="₦"
    elif currency_2=="EUR":
        symbol="€"
    elif currency_2=="USD":
        symbol="$"
    elif currency_2=="CAD":
        symbol="C$"
    elif currency_2=="GBP":
        symbol="£"
    elif currency_2=="AUD":
        symbol="A$"
    elif currency_2=="JMD":
        symbol="J$"
    elif currency_2=="CHF":
        symbol="Fr"
    elif currency_2=="CLP":
        symbol="$"
    elif currency_2=="EGP":
        symbol="£"
    elif currency_2=="SOS":
        symbol=""
    
    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "f332892779msha39d7da2929843fp166289jsncf9bf133e940",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data=json.loads(response.text)
    converted_amount=data['result']['convertedAmount']
    formatted=symbol + " {:.2f}".format(converted_amount)
    print(converted_amount,formatted)
    result['text']=formatted


icon=Image.open('linar_python_projects/images/icon.png')
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)
app_name=Label(top, image=icon , compound=RIGHT ,text="My currency converter", height=5, padx=9,pady=30, anchor=CENTER ,font=('Arial 16 bold'), bg=colour2 ,fg=colour0)
app_name.place(x=0,y=0)
# list of currencies available to the user 
currency=['NGN','EUR','USD','CAD','GBP','CHF','jMD','AUD','SOS','ILS','FJD','EGP','DZD','CZK','CUP','COP','CDF','BZD','CLP']
#main frame
result=Label(main , text="", width=15,height=2,pady=7, relief="solid",anchor=CENTER ,font=('ivy 16 bold'), bg=colour0 ,fg=colour1)
result.place(x=50,y=10)

from_label=Label(main , text="FROM", width=8,height=1,padx=0,pady=0, relief="flat",anchor=NW ,font=('ivy 9 bold'), bg=colour0 ,fg=colour1)
from_label.place(x=48,y=90)
combo1=ttk.Combobox(main, width=8, justify=CENTER,font=('ivy 12 bold'))
combo1['values']=(currency)
combo1.place(x=50,y=115)

to_label=Label(main , text="TO", width=8,height=1,padx=0,pady=0, relief="flat",anchor=NW ,font=('ivy 9 bold'), bg=colour0 ,fg=colour1)
to_label.place(x=158,y=90)
combo2=ttk.Combobox(main, width=8, justify=CENTER,font=('ivy 12 bold'))
combo2['values']=(currency)
combo2.place(x=160,y=115)

amount_label=Label(main, text="Input your amount in the box below",padx=3,pady=1,relief="groove",font=('ivy 9 bold'))
amount_label.place(x=49,y=150)
value=Entry(main,width=22,justify=CENTER, font=('ivy 12 bold'),relief="solid")
value.place(x=50,y=179)

converter_button=Button(main, text="convert", width=19, height=1, bg=colour2,fg=colour0,font=('ivy 12 bold'),command=conversion)
converter_button.place(x=50,y=210)

window.mainloop()