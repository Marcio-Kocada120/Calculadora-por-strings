from tkinter import *
from functools import partial

calcula=Tk()
calcula.title("Calculadora")
calcula.geometry("210x190+100+100")
calcula["bg"]="black"
calcula.resizable(width=False, height=False)

def clear():
    lb["text"]="0"

def bt_click(botao):
    if lb["text"]=="0":
        lb["text"]=botao["text"]
        if lb["text"]==".":
            a=botao["text"]
            lb["text"]="0"+a
        if lb["text"]=="000":
            a=botao["text"]
            lb["text"]="SyntaxError"
        if lb["text"]=="/":
            a=botao["text"]
            lb["text"]="SyntaxError"
        if lb["text"]=="*":
            a=botao["text"]
            lb["text"]="SyntaxError"
        if lb["text"]=="-":
            a=botao["text"]
            lb["text"]="SyntaxError"
        if lb["text"]=="+":
            a=botao["text"]
            lb["text"]="SyntaxError"
        if lb["text"]==")":
            a=botao["text"]
            lb["text"]="SyntaxError"
    elif lb["text"]!="SyntaxError" and lb["text"]!="insert operator press c":
        a=botao["text"]
        lb["text"]=lb["text"]+a
        print(lb["text"])
    if lb["text"].count("./")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(".+")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(".-")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(".*")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("..")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(".(")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(".)")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("++")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+.")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+-")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+*")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+/")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+)")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-.")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-+")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("--")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-*")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-/")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-)")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*.")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*+")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*-")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*/")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*)")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/.")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/+")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/-")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/*")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("//")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/)")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("(.")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("(+")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("(*")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("(/")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("()")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(").")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(")(")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("(000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count(")000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("/000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("*000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("-000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("+000")>0:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if lb["text"].count("0(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("1(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("2(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("3(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("4(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("5(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("6(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("7(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("8(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("9(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if lb["text"].count("000(")>0:
        lb["text"]="insert operator press c"
        print(lb["text"])
    if re.search("\d+(\.\d+)\.",lb["text"]):
        lb["text"]="SyntaxError"
        print(lb["text"])

       
def resultado():
    b=lb["text"]
    b.endswith(".")
    if b.endswith(".")==True:
        lb["text"]="SyntaxError"
    b.endswith("+")
    if b.endswith("+")==True:
        lb["text"]="SyntaxError"
    b.endswith("-")
    if b.endswith("-")==True:
        lb["text"]="SyntaxError"
    b.endswith("*")
    if b.endswith("*")==True:
        lb["text"]="SyntaxError"
    b.endswith("/")
    if b.endswith("/")==True:
        lb["text"]="SyntaxError"
    b.endswith("(")
    if b.endswith("(")==True:
        lb["text"]="SyntaxError"
    if b.count("(")==True and b.count(")")==False:
        lb["text"]="SyntaxError"
        print(lb["text"])
    if b.count(")")==True and b.count("(")==False:
        lb["text"]="SyntaxError"
        print(lb["text"])
    pa=b.count("(")
    pf=b.count(")")
    if pa!=pf:
        lb["text"]="SyntaxError"
        print(lb["text"])
    
    print(b)
    print(eval(b))
    lb["text"]=eval(b)
    lb["text"]=str(eval(b))
    


    
lb1=Label(calcula, text="calculadora simples", bg="red", fg="white" )
lb1.pack(side=TOP, fill=X, expand=0)
lb2=Label(calcula, bg="red")
lb2.pack(side=LEFT, fill=Y)
lb3=Label(calcula, bg="red")
lb3.pack(side=RIGHT, fill=Y)
lb=Label(calcula, text="0", bg="white")
lb.pack(anchor=NE, fill=X, expand=0)

bt7=Button(width=3,text="7",bg="yellow")
bt7["command"]=partial(bt_click, bt7)
bt7.place(x=10,y=50)
bt8=Button(width=3,text="8",bg="yellow")
bt8["command"]=partial(bt_click, bt8)
bt8.place(x=50,y=50)
bt9=Button(width=3,text="9",bg="yellow")
bt9["command"]=partial(bt_click, bt9)
bt9.place(x=90,y=50)
bt4=Button(width=3,text="4",bg="yellow")
bt4["command"]=partial(bt_click, bt4)
bt4.place(x=10,y=85)
bt5=Button(width=3,text="5",bg="yellow")
bt5["command"]=partial(bt_click, bt5)
bt5.place(x=50,y=85)
bt6=Button(width=3,text="6",bg="yellow")
bt6["command"]=partial(bt_click, bt6)
bt6.place(x=90,y=85)
bt1=Button(width=3,text="1",bg="yellow")
bt1["command"]=partial(bt_click, bt1)
bt1.place(x=10,y=120)
bt2=Button(width=3,text="2",bg="yellow")
bt2["command"]=partial(bt_click, bt2)
bt2.place(x=50,y=120)
bt3=Button(width=3,text="3",bg="yellow")
bt3["command"]=partial(bt_click, bt3)
bt3.place(x=90,y=120)
bt0=Button(width=3,text="0",bg="yellow")
bt0["command"]=partial(bt_click, bt0)
bt0.place(x=10,y=155)
btp=Button(width=3,text=".",bg="yellow")
btp["command"]=partial(bt_click, btp)
btp.place(x=50,y=155)
btt=Button(width=3,text="000",bg="lightgreen")
btt["command"]=partial(bt_click, btt)
btt.place(x=90,y=155)
btd=Button(width=3,text="/",bg="lightblue")
btd["command"]=partial(bt_click, btd)
btd.place(x=130,y=50)
btm=Button(width=3,text="*",bg="lightblue")
btm["command"]=partial(bt_click, btm)
btm.place(x=130,y=85)
bts=Button(width=3,text="-",bg="lightblue")
bts["command"]=partial(bt_click, bts)
bts.place(x=130,y=120)
bta=Button(width=3,text="+",bg="lightblue")
bta["command"]=partial(bt_click, bta)
bta.place(x=130,y=155)
btpa=Button(width=3,text="(",bg="lightgreen")
btpa["command"]=partial(bt_click, btpa)
btpa.place(x=170,y=85)
btpf=Button(width=3,text=")",bg="lightgreen")
btpf["command"]=partial(bt_click, btpf)
btpf.place(x=170,y=120)
btc=Button(width=3,text="c",fg="white", bg="red", command=clear)
btc.place(x=170,y=50)
bti=Button(width=3, text="=", bg="lightgray", command=resultado)
bti.place(x=170,y=155)



calcula.mainloop()
