from tkinter import *
import tkinter as tkt
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0, END) #delete 함수 통해 text 영역 내용 리셋

def save_file():
    f = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', '.txt')]) #filedialog의 asksaveasfile 함수 사용
    if f is None:
        return #저장 실패시 대비
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()
    text_area.delete(1.0, END) #저장 이후 내용 리셋


def maker():
    newWindow = Toplevel(window) #새 창을 띄우는 함수
    newWindow.geometry('200x50+800+300')
    newWindow.title('만든 이')
    name = Label(newWindow, text = "우정주")
    name.pack()

    
window = Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0) #프레임 설정

window.iconbitmap("memo.ico") #아이콘 설정

text_area = Text(window)
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W) #TEXT 입력 영역

menuMaker = Menu(window) #메뉴 생성
first_menu = Menu(menuMaker, tearoff=0) 
first_menu.add_command(label = '새 파일', command = new_file) 
first_menu.add_command(label = '저장', command = save_file) 
menuMaker.add_cascade(label='파일', menu=first_menu) 
window.config(menu = menuMaker) #첫 번째 메뉴칸 생성

first_menu.add_separator()  # 구분선 추가

first_menu.add_command(label='종료', command=window.destroy) #종료 버튼


# 두 번째 메뉴 만들기
second_menu = Menu(menuMaker, tearoff=0)
second_menu.add_command(label = '만든 이', command = maker)
menuMaker.add_cascade(label='정보', menu = second_menu)


window.mainloop()