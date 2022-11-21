from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class Billing_App:
        def __init__(self, window):
            self.window = window
            self.window.title("Supermarket billing app")
            self.window.geometry("1380x700+0+0")





       #product category list
            self.category=["Select Option","Clothing","Lifestyle","Mobiles"]

            #subcatclothing
            self.subcatClothing=["Pant","Shirt","T-shirt"]
            #pant
            self.Pant=["LeeCooper","Levis","Adidas"]
            self.price_LeeCooper=2499
            self.price_Levise = 3299
            self.price_Adidas = 3999
            #shirt
            self.Shirt=["Arrow","FlyingMechine","Allensolly"]
            self.price_Arrow=1599
            self.price_FlyingMechine=1799
            self.price_AllenSolly=2299
            #T-shirt
            self.T_shirt=["Highlander","Roadster","Reebok"]
            self.price_Highlander=229
            self.price_Roaster=355
            self.price_Reebok=349

            #subcategory lifestyle

            self.subcatLifestyle=["BathSoap","Face cream","Hair oil"]
            #Bathsoap
            self.Bathsoap=["lux","elaria","chandrika"]
            self.price_lux=28
            self.price_elaria = 35
            self.price_chandrika = 25
            #facecream
            self.Faceream=["fair lovely","cuticura","ponds"]
            self.price_Fairlovely=25
            self.price_cuticura=15
            self.price_ponds=35
            #hair oil
            self.Hairoil=["parachute","jasmine","alovera"]
            self.price_parachute=15
            self.price_jasmine=49
            self.price_alovera=37



            # subcategory mobiles
            self.subcatMobiles=["Iphone","Samsung","One Plus"]
            #Iphone
            self.Iphone=["7plus","12pro","13mini"]
            self.price_7plus=28000
            self.price_12pro=78999
            self.price_13mini=10099
            #Samsung
            self.samsung=["galaxy13","M30","A50"]
            self.price_galaxy13=22000
            self.price_M30=18500
            self.price_A50=25499
            #oneplus
            self.oneplus=["oneplus1""oneplus2","oneplus3"]
            self.price_oneplus1=17499
            self.price_oneplus2=24999
            self.price_oneplus3=35499














            '''------------------------Frontend designing part------------------------------------'''

            # img1
            # img=Image.OPEN("images/girl-7024553.jpg")
            # img=img.resize((500,130),Image.ANTIALIAS)
            # self.photoimg=ImageTk.PhotoImage(img)

            lbl_tilte = Label(self.window, text="BESTEE HYPERMARKET", font=("times new roman", 30, "bold"),
                              bg="DARK BLUE", fg="WHITE", )
            lbl_tilte.place(x=-100, y=130, width=1530, height=60)

            '''main frame'''
            main_Frame = Frame(self.window, bd=5, relief=GROOVE, background="white")
            main_Frame.place(x=0, y=190, width=1530, height=600)



            '''customer details '''
            cust_Frame = LabelFrame(main_Frame, text="Customer Details", font=("times new roman", 12, "bold"), bg="white",
                                    fg="red")
            cust_Frame.place(x=10, y=5, width=350, height=140)

            # mob
            self.lbl_cust = Label(cust_Frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
            self.lbl_cust.grid(row=0, column=0, stick=W, padx=5, pady=2)

            self.entry_cust = ttk.Entry(cust_Frame, font=("times new roman", 12, "bold"), width=24)
            self.entry_cust.grid(row=0, column=1)

            # customer name
            self.lbl_mob = Label(cust_Frame, text="Mobile Number", font=("times new roman", 12, "bold"), bg="white")
            self.lbl_mob.grid(row=1, column=0, stick=W, padx=5, pady=2)

            self.entry_mob = ttk.Entry(cust_Frame, font=("times new roman", 12, "bold"), width=24)
            self.entry_mob.grid(row=1, column=1)

            # email
            self.lbl_email = Label(cust_Frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
            self.lbl_email.grid(row=2, column=0, stick=W, padx=5, pady=2)

            self.entry_email = ttk.Entry(cust_Frame, font=("times new roman", 12, "bold"), width=24)
            self.entry_email.grid(row=2, column=1)





            '''PRODUCT DEATAILS'''
            product_Frame = LabelFrame(main_Frame, text="Product Details", font=("times new roman", 12, "bold"), bg="white", fg="red")
            product_Frame.place(x=370, y=5, width=600, height=140)

            # select category

            self.lbl_category = Label(product_Frame, text="Category", font=("times new roman", 12, "bold"), bg="white")
            self.lbl_category.grid(row=0, column=0, stick=W, padx=5, pady=2)

            self.combo_category = ttk.Combobox(product_Frame, values=self.category,
                                               font=("times new roman", 12, "bold"), width=24)
            self.combo_category.current(0)   # 0th position of category list
            self.combo_category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
            # self.combo_category.bind("<<ComboboxSelected>>",self.cate)



            self.lbl_subcategory = Label(product_Frame, text="Subcategory", font=("times new roman", 12, "bold"),
                                         bg="white")
            self.lbl_subcategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

            self.comboSubcategory = ttk.Combobox(product_Frame, font=("times new roman", 12, "bold"), width=24)
            self.comboSubcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)

            # product name

            self.lbl_product_name = Label(product_Frame, text="Product name", font=("times new roman", 12, "bold"),
                                          bg="white")
            self.lbl_product_name.grid(row=2, column=0, stick=W, padx=5, pady=2)

            self.combo_category = ttk.Combobox(product_Frame, font=("times new roman", 12, "bold"), width=24)
            self.combo_category.grid(row=2, column=1, sticky=W, padx=5, pady=2)


            # price

            self.lbl_price = Label(product_Frame, text="Price", font=("times new roman", 12, "bold"),
                                   bg="white")
            self.lbl_price.grid(row=0, column=2, stick=W, padx=5, pady=2)

            self.entryCategory = ttk.Entry(product_Frame, font=("times new roman", 12, "bold"), width=24)
            self.entryCategory.grid(row=0, column=3, sticky=W, padx=5, pady=2)

            # quantity

            self.lbl_qty = Label(product_Frame, text="Qty", font=("times new roman", 12, "bold"),
                                 bg="white")
            self.lbl_qty.grid(row=1, column=2, stick=W, padx=5, pady=2)

            self.entryQty= ttk.Entry(product_Frame, font=("times new roman", 12, "bold"), width=24)
            self.entryQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)



            '''middlie frame'''

            middleFrame = Frame(main_Frame, bd=0, relief=GROOVE)
            middleFrame.place(x=10, y=150, height=340,width=960)
            #
            # #Image 1
            # img12=Image.OPEN("girl.jpg")
            # img12=img.img12.resize
            #


            '''search frame'''

            Search_frame = Frame(main_Frame, bd=2,bg="white")
            Search_frame.place(x=1000,y=15,width=500,height=40)

            self.lbl_bill = Label(Search_frame,text="Bill Number", font=("times new roman", 10, "bold"), bg="dark blue",fg="white")
            self.lbl_bill.grid(row=0, column=0, sticky=W, padx=0)

            self.entrybill = ttk.Entry(Search_frame, font=("ariel", 10, "bold"), width=26)
            self.entrybill.grid(row=0, column=1, sticky=W)

            self.BtnSearch = Button(Search_frame, text="Search", font=("ariel", 8, "bold"), bg="red", fg="white", width=7,
                                    cursor="hand2")
            self.BtnSearch.grid(row=0, column=2,sticky=W)





            '''right frame billing area'''

            right_Frame = LabelFrame(main_Frame, text="Bill Area", bd=3, font=("times new roman", 12, "bold"), bg="white",
                                     fg="red")
            right_Frame.place(x=1000, y=40, width=330, height=360)

            scroll_y = Scrollbar(right_Frame, orient=VERTICAL)
            self.text_area = Text(right_Frame, yscrollcommand=scroll_y.set, bg="white", fg="blue",
                                  font=("times new roman", 12, "bold"))
            scroll_y.pack(side=RIGHT, fill=Y)
            # scrolling
            scroll_y.config(command=self.text_area.yview)
            self.text_area.pack(fill=BOTH, expand=1)






            ''' bill counter label frame'''

            #bottom frame................

            bottom_frame = LabelFrame(main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white",
                                      fg="red")
            bottom_frame.place(x=0, y=400, width=1520, height=125)

            # subtotal
            self.lblsubTotal = Label(bottom_frame, font=("ariel", 10, "bold"), bg="white", text="Sub Totoal", bd=4)
            self.lblsubTotal.grid(row=1, column=2, sticky=W, padx=5, pady=2)

            self.entrysubTotal = ttk.Entry(bottom_frame, font=("ariel", 10, "bold"), width=26)
            self.entrysubTotal.grid(row=1, column=3, sticky=W, padx=5, pady=2)

            # gov tax
            self.lblgovtax = Label(bottom_frame, font=("ariel", 10, "bold"), bg="white", text="Gov Tax", bd=4)
            self.lblgovtax.grid(row=2, column=2, sticky=W, padx=5, pady=2)

            self.entrygovtax = ttk.Entry(bottom_frame, font=("ariel", 10, "bold"), width=26)
            self.entrygovtax.grid(row=2, column=3, sticky=W, padx=5, pady=2)

            # Total
            self.lblTotal = Label(bottom_frame, font=("ariel", 10, "bold"), bg="white", text="Total", bd=4)
            self.lblTotal.grid(row=3, column=2, sticky=W, padx=5, pady=2)

            self.entryTotal = ttk.Entry(bottom_frame, font=("ariel", 10, "bold"), width=26)
            self.entryTotal.grid(row=3, column=3, sticky=W, padx=5, pady=2)

            #button FRAME
            btn_frame=Frame(bottom_frame, bd=2,bg="white")
            btn_frame.place(x=310,y=15)

            self.BtnAddToCart=Button(btn_frame,text="Add to Cart",font=("ariel", 15, "bold"),bg="red",fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0,column=0)

            self.BtnAddToCart = Button(btn_frame, text="Generate Bill", font=("ariel", 15, "bold"), bg="red", fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0, column=2)

            self.BtnAddToCart = Button(btn_frame, text="Save Bill", font=("ariel", 15, "bold"), bg="red", fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0, column=3)

            self.BtnAddToCart = Button(btn_frame, text="Print", font=("ariel", 15, "bold"), bg="red", fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0, column=4)

            self.BtnAddToCart = Button(btn_frame, text="Clear", font=("ariel", 15, "bold"), bg="red", fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0, column=5)

            self.BtnAddToCart = Button(btn_frame, text="Exit", font=("ariel", 15, "bold"), bg="red", fg="white",width=13,cursor="hand2")
            self.BtnAddToCart.grid(row=0, column=6)

        #
        # def Cate(self,event=""):
        #     if self.combo_category.get()=="Clothing":
        #         self.comboSubcategory.config(values=self.subcatClothing)
        #         self.comboSubcategory.current(0)


if __name__ == '__main__':
    window = Tk()
    obj = Billing_App(window)

    window.mainloop()
