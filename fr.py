from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as con
import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first imag
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=800,height=200)

        # second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=800,y=0,width=500,height=200)

        # bg image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg")#imageposition
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.photoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_1b1=Label(bg_img,text="ATTANDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_1b1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

         #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        
        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg") #imageposotion
        img_left=img_left.resize((720,150))
        self.photoimg_left =ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # label and entry
        # attendance id

        attendanceID_label = Label(left_inside_frame,text="AttendanceID: ",font=("times new roman",12,"bold"))
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #rollno.
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLabel=Label(left_inside_frame,text="Name",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # Attendance
        attendanceLabel=Label(left_inside_frame,text="Attandance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=37)

        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Right_frame.place(x=750,y=10,width=800,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # ========scroll bar table======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
    

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)



if __name__== "main":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
