from tkinter import*
from tkinter import ttk
#install pillow for images use/save krne ke liye in terminal cmd(pip install pillow)
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
   def __init__(self,root):  #(root=master)
      self.root=root #initilize self.root to root
      #to creat window
      self.root.geometry("1366x768+0+0") # 1530=len,790=brth,0=x_cordinate_of secreen,0=ycoordinate)
      #for tital
      self.root.title("Employee Management System")
      lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="darkblue",bg="white")
      lbl_title.place(x=0,y=0,width=1366,height=50)
      
      #variable
      self.ver_dep=StringVar()
      self.ver_name=StringVar()
      self.ver_dob=StringVar()
      self.ver_idproof=StringVar()
      self.ver_idno=StringVar()
      self.ver_ref=StringVar()
      self.ver_doj=StringVar()
      self.ver_phone=StringVar()
      self.ver_email=StringVar()
      self.ver_county=StringVar()
      self.ver_salary=StringVar()
      self.ver_meri=StringVar()
      self.ver_gen=StringVar()
     
      
      #ADD LOGO
      #to add logo infornt of Emp tital
      img_logo=Image.open("logo1.png")  #to open
      
      #to resize logo (thats why we use pillow)
      img_logo=img_logo.resize((50,50),Image.LANCZOS)  #LANCZOS convert high level image to low level image
      
      #to set logo
      #we use self here beacuse class ke sath images use ho
      self.photo_logo=ImageTk.PhotoImage(img_logo)
      
      #to show logo with the help of button or lebel(we use lebel)
      self.logo=Label(self.root,image=self.photo_logo)
      self.logo.place(x=190,y=0,width=50,height=50)
      
      #TO SET FREM IMAGE
      #to create freme to insert photos our wo ham self .root ke aandar banate he
      
      img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")  #bd=border ,relief for border styl i.e ridge
      img_frame.place(x=0,y=50,width=1366,height=160)
      
      img1=Image.open("people2.png")
      img1=img1.resize((1366,160),Image.LANCZOS)
      self.photo1=ImageTk.PhotoImage(img1)
      self.img_1=Label(self.root,image=self.photo1)
      self.img_1.place(x=0,y=50,width=1366,height=160)
      
      #main frame
      Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
      Main_frame.place(x=30,y=190,width=1300,height=520)
      
      #upper frame
      upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information",font=("times new roman",11,"bold"),fg="red") #lableframe use for frame ko lable dene ke liye
      upper_frame.place(x=10,y=10,width=1280,height=250)
      
      #LABEL AND FRAME
      
      #label and frame it is locatet in upper frame
      lbl_dep=Label(upper_frame,text="Department Name",font=("arial",12,"bold"),fg="black",bg="white")
      
      #place ham tab krte he jab hame pata nahi hota ki chije kaha rakhni he
      lbl_dep.grid(row=0,column=0,padx=8,sticky="w")  #to mantain destance in x axis use padx and sticky ye text department ko west me chipka ke rakhe ga our bg=white nahi rakhte to grey show krta
      
      #to make combo box for department
      combo_dep=ttk.Combobox(upper_frame,textvariable=self.ver_dep,font=("arial",12,"bold"),width=18,state="readonly") #ttk ke aandar stylish combo box hota he ,state ye read our write ka function deta he
      
      #to set value
      combo_dep["value"]=("Select Department","Front End","HR","Manager","Back End","Full Stack")
      combo_dep.current(0) #to place ,tupal 0 se start hota he
      combo_dep.grid(row=0,column=1,padx=2,pady=2,sticky="w")
      
      #name
      lbl_name=Label(upper_frame,font=("arial",12,"bold"),text="Name",bg="white")
      lbl_name.grid(row=1,column=0,sticky="w",padx=8)
      
      #entry name
      txt_name=ttk.Entry(upper_frame,textvariable=self.ver_name, font=("arial",12,"bold"))
      txt_name.grid(row=1,column=1,padx=2,pady=2)
      
      #email
      lbl_Email=Label(upper_frame,font=("arial",12,"bold"),text="Email",bg="white")
      lbl_Email.grid(row=2,column=0,sticky="w",padx=8)
      
      txt_Email=ttk.Entry(upper_frame,textvariable=self.ver_email,font=("arial",12,"bold"))
      txt_Email.grid(row=2,column=1,padx=2,pady=2)
      
      #date of birth
      lbl_DOB=Label(upper_frame,font=("arial",12,"bold"),text="Birth Date",bg="white")
      lbl_DOB.grid(row=3,column=0,sticky="w",padx=8)
      
      txt_DOB=ttk.Entry(upper_frame,textvariable=self.ver_dob,font=("arial",12,"bold"))
      txt_DOB.grid(row=3,column=1,padx=2,pady=2)
      
      #address
      lbl_addr=Label(upper_frame,font=("arial",12,"bold"),text="Address",bg="white")
      lbl_addr.grid(row=4,column=0,sticky="w",padx=8,pady=2)
      
      txt_addr=ttk.Entry(upper_frame,font=("arial",12,"bold"))
      txt_addr.grid(row=4,column=1,padx=2,pady=2)
      
      #id proof
      lbl_proof=Label(upper_frame,font=("arial",12,"bold"),text="ID Type",bg="white")
      lbl_proof.grid(row=0,column=2,sticky="w",padx=30)
      
      combo_proof=ttk.Combobox(upper_frame,textvariable=self.ver_idproof,font=("arial",12,"bold"),width=18,state="readonly") 
      combo_proof["value"]=("Select Id Proof","Addhar card","Bank passbook","Voter Id","Driving licance","Employee Id","College Id")
      combo_proof.current(0) #to place ,tupal 0 se start hota he
      combo_proof.grid(row=0,column=3,padx=2,pady=8,sticky="w")
      
      #Id no
      lbl_Idno=Label(upper_frame,font=("arial",12,"bold"),text="ID No",bg="white")
      lbl_Idno.grid(row=1,column=2,sticky="w",padx=30)
      
      txt_Idno=ttk.Entry(upper_frame,textvariable=self.ver_idno,font=("arial",12,"bold"))
      txt_Idno.grid(row=1,column=3,padx=2,pady=7)
      
      #marital status
      lbl_marital=Label(upper_frame,font=("arial",12,"bold"),text="Marital Status",bg="white")
      lbl_marital.grid(row=2,column=2,sticky="w",padx=30)
      
      combo_marital=ttk.Combobox(upper_frame,textvariable=self.ver_meri,font=("arial",12,"bold"),width=18,state="readonly") 
      combo_marital["value"]=("Select","Married","Singal","Widow")
      combo_marital.current(0) #to place ,tupal 0 se start hota he
      combo_marital.grid(row=2,column=3,padx=2,pady=8,sticky="w")
      
      #gender
      lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender",bg="white")
      lbl_gender.grid(row=3,column=2,sticky="w",padx=30)
      
      combo_gender=ttk.Combobox(upper_frame,textvariable=self.ver_gen,font=("arial",12,"bold"),width=18,state="readonly") 
      combo_gender["value"]=("Select","Female","Male","Other")
      combo_gender.current(0) #to place ,tupal 0 se start hota he
      combo_gender.grid(row=3,column=3,padx=2,pady=8,sticky="w")
      
      
      
      #date of join
      #lbl_Joining=Label(upper_frame,font=("arial",12,"bold"),text="Joining Date",bg="white")
      #lbl_Joining.grid(row=4,column=2,sticky="w",padx=28)
      
      #txt_Joining=ttk.Entry(upper_frame,textvariable=self.ver_doj,font=("arial",12,"bold"))
      #txt_Joining.grid(row=4,column=3,padx=2,pady=7)
      
      #refrance
      lbl_refrance=Label(upper_frame,font=("arial",12,"bold"),text="Refrance",bg="white")
      lbl_refrance.grid(row=0,column=4,sticky="w",padx=8)
      
      txt_refrance=ttk.Entry(upper_frame,textvariable=self.ver_ref,font=("arial",12,"bold"))
      txt_refrance.grid(row=0,column=5,padx=2,pady=7)
      
      #phone no
      lbl_Phone=Label(upper_frame,font=("arial",12,"bold"),text="Phone_No",bg="white")
      lbl_Phone.grid(row=1,column=4,sticky="w",padx=8)
      
      txt_Phone=ttk.Entry(upper_frame,textvariable=self.ver_phone,font=("arial",12,"bold"))
      txt_Phone.grid(row=1,column=5,padx=2,pady=7)
      
      #country
      lbl_country=Label(upper_frame,font=("arial",12,"bold"),text="Country",bg="white")
      lbl_country.grid(row=2,column=4,sticky="w",padx=8)
      
      txt_country=ttk.Entry(upper_frame,textvariable=self.ver_county,font=("arial",12,"bold"))
      txt_country.grid(row=2,column=5,padx=2,pady=7)
      
      #salary
      lbl_salary=Label(upper_frame,font=("arial",12,"bold"),text="Salary",bg="white")
      lbl_salary.grid(row=3,column=4,sticky="w",padx=8)
      
      txt_salary=ttk.Entry(upper_frame,textvariable=self.ver_salary,font=("arial",12,"bold"))
      txt_salary.grid(row=3,column=5,padx=2,pady=7)
      
      #ADD BUTTON
      #save
      btn_save=Button(upper_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=15,bg="green",fg="white")
      btn_save.grid(row=0,column=6,padx=50,pady=8)
      
      #update
      btn_update=Button(upper_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=15,bg="green",fg="white")
      btn_update.grid(row=1,column=6,padx=50,pady=8)
      
      #delet
      btn_delete=Button(upper_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=15,bg="green",fg="white")
      btn_delete.grid(row=2,column=6,padx=50,pady=8)
      
      
      #clear
      btn_clear=Button(upper_frame,text="Reset",command=self.clear_data,font=("arial",15,"bold"),width=15,bg="green",fg="white")
      btn_clear.grid(row=3,column=6,padx=50,pady=8)
      
      #down frame
      down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information View",font=("times new roman",11,"bold"),fg="red")
      down_frame.place(x=10,y=260,width=1280,height=250)
      
      #search frame
      Search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg="white",text="Search Employee",font=("times new roman",11,"bold"),fg="red")
      Search_frame.place(x=8,y=4,width=1260,height=60)
      
      #search button
      btn_search=Button(Search_frame,text="Search",command=self.search_data,font=("arial",8,"bold"),width=6,bg="blue",fg="white")
      btn_search.grid(row=0,column=3,padx=4,pady=2)
      
      #for search data in def search() function we have creat two variable for combo box and search entry
      self.var_search = StringVar()
      txt_search=ttk.Entry(Search_frame,textvariable=self.var_search,font=("arial",12,"bold"))
      txt_search.grid(row=0,column=2,padx=2,pady=7)
      
      btn_show=Button(Search_frame,text="Show All",command=self.fetch_data,font=("arial",8,"bold"),width=6,bg="blue",fg="white")
      btn_show.grid(row=0,column=4,padx=4,pady=2)
      
      
      lbl_searchby=Label(Search_frame,font=("arial",12,"bold"),text="Short by",bg="gray")
      lbl_searchby.grid(row=0,column=0,sticky="w",padx=30)
      
      #search combo
      #for search data in def search() function we have creat two variable for combo box and entry
      self.var_com_search=StringVar()
      combo_searchby=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=18,state="readonly") 
      combo_searchby["value"]=("select","Department","Name","ID_No","Refrance","Phone_No","Email_Id","Country","Salary")
      #Department=%s,Name=%s, Date_of_Birth=%s , Refrance=%s ,Phone_No=%s,Email_Id =%s,Country=%s,Salary=%s,Marital_Status=%s,Gender=%s,ID_Proof=%s WHERE ID_No=%s
      combo_searchby.current(0) #to place ,tupal 0 se start hota he
      combo_searchby.grid(row=0,column=1,padx=2,pady=8,sticky="w")
      
      #Table frame
      table_frame=Frame(down_frame,bd=3,relief=RIDGE)
      table_frame.place(x=8,y=70,width=1260,height=150)
      
      #to give scroll
      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
      
      #creat treeview or table                                    dummy code                    
      self.employee_table=ttk.Treeview(table_frame,columns=("dep","name","dob","idproof","idno","ref","phone","email","county","salary","mari","gen",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
      #to pack scroll
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      
      #to give command above table/preview (use config command)
      scroll_x.config(command=self.employee_table.xview)
      scroll_y.config(command=self.employee_table.yview)
    
      #creat actual table element
      self.employee_table.heading("dep",text="Department")  
      self.employee_table.heading("name",text="Name")
      self.employee_table.heading("dob",text="Date_of_Birth")
      self.employee_table.heading("idproof",text="ID_Proof")
      self.employee_table.heading("idno",text="ID_No")
      self.employee_table.heading("ref",text="Refrance")
      #self.employee_table.heading("doj",text="Date of Join")
      self.employee_table.heading("phone",text="Phone_No")
      self.employee_table.heading("email",text="Email_ID")
      self.employee_table.heading("county",text="Country")
      self.employee_table.heading("salary",text="Salary")
      self.employee_table.heading("mari",text="Marital_Status")
      self.employee_table.heading("gen",text="Gender")
      #self.employee_table.heading("",text="")
      #self.employee_table.heading("",text="")
      #self.employee_table.heading("",text="")
      #self.employee_table.heading("dep",text="Department")
      
      #colum ke bich me gap rahati uus gap ko hatane ke liye
      
      #pahili empty space remove krne ke liye
      self.employee_table["show"]="headings"
      
      # table ki widdt set krne ke liye
      self.employee_table.column("dep",width=100)  
      self.employee_table.column("name",width=100)
      self.employee_table.column("dob",width=100)
      self.employee_table.column("idproof",width=100)
      self.employee_table.column("idno",width=100)
      self.employee_table.column("ref",width=100)
      #self.employee_table.column("doj",width=100)
      self.employee_table.column("phone",width=100)
      self.employee_table.column("email",width=100)
      self.employee_table.column("county",width=100)
      self.employee_table.column("salary",width=100)
      self.employee_table.column("mari",width=100)
      self.employee_table.column("gen",width=100)
      
      self.employee_table.pack(fill=BOTH,expand=1)  #fill-both ye table bothside se fill krte he and expand=1 ye table ko expand krte he
      
      #cursor ke vetiable ko table ke sath bind krna padta he
      self.employee_table.bind("<ButtonRelease>",self.get_cursor)
      
      self.fetch_data()
      
   
   #*************function decleration*******************
   
   def add_data(self):
      if self.ver_dep.get()=="" or self.ver_email.get()=="":    #to fill all important data data in table
        messagebox.showerror("Error","All Fields are required")   #messagebox has three types showerror,info ,warning of message we use error type
      #                   error tital     error message show     
      #else part me wo chize likhege jo hame chahiye       
      else:
         try:
            #to make connection
         # ver                   haamara host,user name ,password,detabase                                                                                          
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@3101",database="emp_database")
            # to make curser
            my_cursor=conn.cursor()
            #   execute commsnd of mysql , tabe name , here write ,% called person jitne column uutne %s dene hote he
            my_cursor.execute("insert into emp_tab values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.ver_dep.get(),
                                                                                                   self.ver_name.get(),
                                                                                                   self.ver_dob.get(),
                                                                                                   self.ver_idproof.get(),
                                                                                                   self.ver_idno.get(),
                                                                                                   self.ver_ref.get(),
                                                                                                   #self.ver_doj.get(),
                                                                                                   self.ver_phone.get(),
                                                                                                   self.ver_email.get(),
                                                                                                   self.ver_county.get(),
                                                                                                   self.ver_salary.get(),
                                                                                                   self.ver_meri.get(),
                                                                                                   self.ver_gen.get()
                                                                                                ))
            
            conn.commit()
            self.fetch_data()  # jab bi ham koi data add karege tab hame wo niche ki window me turant dikh jayega
            conn.close()  #to close connection
            #connection close krne ke bad/ data enter krne ke bad ek message show hona chahiye
            messagebox.showinfo("Success","Employee has been added",parent=self.root)
             #                 ye wala msg             ye message window ke bahar nahi nikal jaye iisliye parent=self.root                           
         except Exception as any:
            
            messagebox.showerror("Error",f"Due to:{str(any)}",parent=self.root)
            
         
            #                                     iis paranthesis ke aandar sara data insert krna padta he (holding variable )           
   #fetch function
   #to see data in web page
   def fetch_data(self):
    try:
       #fetch data krna hoga detabase se to hame database chahiye hoga jo ni che likhege
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql@3101",database="emp_database")
    except mysql.connector.Error as es:
        print(f'Error: {es}')
        return
    # to make curser
    my_cursor=conn.cursor()
    my_cursor.execute("select * from emp_tab")
    #aab emp_tab ka deta aa raha he wo hame kahipe store krns padega
    data=my_cursor.fetchall()   #data,my_curser=variable , fetchall function 
    if len(data)!=0:
        for item in self.employee_table.get_children():     #get_childreen ==means department, salary,Id no
            self.employee_table.delete(item)                #delet item
        # to insert data tebal ke aandar
        for i in data: #get data from data  
            self.employee_table.insert("",END,values=i)
        conn.commit()
    conn.close()
   
   #creat get curser function [jab ham data par click karege tab hame wo data field me dikhni chahiye] box me
   
   #to creat curser hame event pass krna padta he so take event variable
   def get_cursor(self, event=None):  #The event argument has been given a default value of None so that it's possible to call the function without passing an event.
    cursor_row = self.employee_table.focus()
    
    #The code checks if the cursor_row is empty and returns immediately if it is. This is to avoid an error if the table does not have any rows.
    if cursor_row == '':
        return

    content = self.employee_table.item(cursor_row)
    data = content["values"]

    self.ver_dep.set(data[0])
    self.ver_name.set(data[1])
    self.ver_dob.set(data[2])
    self.ver_idproof.set(data[3])
    self.ver_idno.set(data[4])
    self.ver_ref.set(data[5])
    #self.ver_doj.set(data[6])
    self.ver_phone.set(data[6])
    self.ver_email.set(data[7])
    self.ver_county.set(data[8])
    self.ver_salary.set(data[9])
    self.ver_meri.set(data[10])
    self.ver_gen.set(data[11])

   def update_data(self):
      if self.ver_dep.get()=="" or self.ver_email.get()=="":    #to fill all important data data in table
        messagebox.showerror("Error","All Fields are required")   #messagebox has three types showerror,info ,warning of message we use error type
      #                   error tital     error message show     
      #else part me wo chize likhege jo hame chahiye       
      else:
         try:
            update=messagebox.askyesno("update","Are you sure update this data")
            if update:
            #to make connection
               # ver                   haamara host,user name ,password,detabase                                                                                          
               conn=mysql.connector.connect(host="localhost",username="root",password="mysql@3101",database="emp_database")
               # to make curser
               my_cursor=conn.cursor()
               #write query for update
               values="UPDATE emp_tab SET Department=%s,Name=%s, Date_of_Birth=%s , Refrance=%s ,Phone_No=%s,Email_Id =%s,Country=%s,Salary=%s,Marital_Status=%s,Gender=%s,ID_Proof=%s WHERE ID_No=%s"
               my_cursor.execute(values,(
                  
                                                                                                                                                                                                               self.ver_dep.get(),
                                                                                                                                                                                                               self.ver_name.get(),
                                                                                                                                                                                                               self.ver_dob.get(),
                                                                                                                                                                                                               self.ver_ref.get(),
                                                                                                                                                                                                               #self.ver_doj.get(),
                                                                                                                                                                                                               self.ver_phone.get(),
                                                                                                                                                                                                               self.ver_email.get(),
                                                                                                                                                                                                               self.ver_county.get(),
                                                                                                                                                                                                               self.ver_salary.get(),
                                                                                                                                                                                                               self.ver_meri.get(),
                                                                                                                                                                                                               self.ver_gen.get(),
                                                                                                                                                                                                               self.ver_idproof.get(),
                                                                                                                                                                                                               self.ver_idno.get()
                                                                                                                                                                                                               ))
            else:
               if not update:
                  return
            conn.commit()
            self.fetch_data()  #jab bi update kare tab hi fetch ho jaye data
            conn.close()  #to close connection
            messagebox.showinfo("Success","Employee Successfully updated",parent=self.root)
         #to close exception
         except Exception as es:
            print(es)
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
   
   #delet button
   def delete_data(self):
      if self.ver_idno.get()=="":
         messagebox.showerror("Error","All fields are required")
      else:
         try:
            #              ask box aata he
            Delete=messagebox.askyesno("Delete","Are you sure",parent=self.root)
            if Delete>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="mysql@3101",database="emp_database")
               # to make curser
               my_cursor=conn.cursor()
               sql="delete from emp_tab where ID_No=%s"
               value=(self.ver_idno.get(),)
               my_cursor.execute(sql,value)
            else:
               if not Delete:
                  return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success Delete","Employee Successfully Deleted",parent=self.root)
         except Exception as es:
            print(es)
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
   
   
   #  reset/clear data
   def clear_data(self):
      self.ver_dep.set("Select Department")
      self.ver_name.set("")
      self.ver_dob.set("")
      self.ver_idproof.set("Select Id proof")
      self.ver_idno.set("")
      self.ver_ref.set("")
      #self.ver_doj.set(data[6])
      self.ver_phone.set("")
      self.ver_email.set("")
      self.ver_county.set("")
      self.ver_salary.set("")
      self.ver_meri.set("Select Status")
      self.ver_gen.set("Select Gendar")
   
   
   # to search data
   #here we write search ke function ki functionlity likhte he
   def search_data(self):
      if self.var_com_search.get()=="" or self.var_search.get()=="":
         messagebox.showerror("Error","please select option")
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="mysql@3101",database="emp_database")
               # to make curser
            my_cursor=conn.cursor()
            #$sql query
            my_cursor.execute("SELECT * FROM emp_tab WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")    
            #to store data in this variable
            rows=my_cursor.fetchall()
            if len(rows)!=0:
               self.employee_table.delete(*self.employee_table.get_children())
               for i in rows:
                  self.employee_table.insert("",END,values=i)
            conn.commit
            conn.close()
         except Exception as es:
            print(es)
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
            
                
                  
      

#to close or pack window
if __name__=="__main__":
   root=Tk()
   #to creat class_obj
   obj=Employee(root)
   root.mainloop()