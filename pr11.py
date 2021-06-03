import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.connectDB()
        self.blist=[]
        self.layout=QHBoxLayout()
        self.mainTab=QTabWidget()
        self.setWindowTitle("Practical 11")
        self.setGeometry(100,100,500,250)
        self.tab1=QTabWidget()
        self.tab2=QTabWidget()
        self.tab3=QTabWidget()
        self.tab4=QTabWidget()
        self.tab5=QTabWidget()
        self.mainTab.addTab(self.tab1,"Add Book")
        self.mainTab.addTab(self.tab2,"Update Book Details")
        self.mainTab.addTab(self.tab3,"Search Book")
        self.mainTab.addTab(self.tab4,"Check Availability")
        self.mainTab.addTab(self.tab5,"Sell Book")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.layout.addWidget(self.mainTab)
        self.setLayout(self.layout)
        self.show()

    

    def tab1UI(self):
        
        grid1=QGridLayout()
        
        self.lblname=QLabel("Book name")
        self.bname=QLineEdit()
        self.validateName=QtCore.QRegExp("[A-Za-z ]+")
        self.validatorName=QtGui.QRegExpValidator(self.validateName)
        self.bname.setValidator(self.validatorName)
        grid1.addWidget(self.lblname,0,0)
        grid1.addWidget(self.bname,0,1)

        self.lblauthor=QLabel("Author name")
        self.bauthor=QLineEdit()
        self.validateAuthor=QtCore.QRegExp("[A-Za-z ]+")
        self.validatorAuthor=QtGui.QRegExpValidator(self.validateAuthor)
        self.bauthor.setValidator(self.validatorAuthor)
        grid1.addWidget(self.lblauthor,1,0)
        grid1.addWidget(self.bauthor,1,1)

        self.lblprice=QLabel("Price ")
        self.bprice=QLineEdit()
        self.validatePrice=QtCore.QRegExp("[0-9]+(\.[0-9][0-9])")
        self.validatorPrice=QtGui.QRegExpValidator(self.validatePrice)
        self.bprice.setValidator(self.validatorPrice)
        grid1.addWidget(self.lblprice,2,0)
        grid1.addWidget(self.bprice,2,1)

        self.lblpublisher=QLabel("Publisher")
        self.bpublisher=QComboBox(self)
        self.bpublisher.addItem("Willey")
        self.bpublisher.addItem("Wrox")
        self.bpublisher.addItem("TATA")
        self.bpublisher.addItem("McGrawhill")
        self.bpublisher.addItem("apress")
        grid1.addWidget(self.lblpublisher,3,0)
        grid1.addWidget(self.bpublisher,3,1)

        self.lblcategory=QLabel("Category")
        self.bcategory=QComboBox(self)
        self.bcategory.addItem("Computer")
        self.bcategory.addItem("Medical")
        self.bcategory.addItem("Management")
        self.bcategory.addItem("Engineering")
        grid1.addWidget(self.lblcategory,4,0)
        grid1.addWidget(self.bcategory,4,1)

        self.lblisbn=QLabel("ISBN Number")
        self.bisbn=QLineEdit()
        #self.validateisbn=QtCore.QRegExp("\d{13}")
        #self.validatorisbn=QtGui.QRegExpValidator(self.validateisbn)
        #self.bisbn.setValidator(self.validatorisbn)
        grid1.addWidget(self.lblisbn,5,0)
        grid1.addWidget(self.bisbn,5,1)

        self.lblqty=QLabel("Quantity")
        self.bqty=QLineEdit()
        self.validateQty=QtCore.QRegExp("\d+")
        self.validatorQty=QtGui.QRegExpValidator(self.validateQty)
        self.bqty.setValidator(self.validatorQty)
        grid1.addWidget(self.lblqty,6,0)
        grid1.addWidget(self.bqty,6,1)

        self.btnadd=QPushButton("Add Book")
        grid1.addWidget(self.btnadd,7,0,1,2)

        self.btnadd.clicked.connect(self.addBook)
        self.tab1.setLayout(grid1)

    def connectDB(self):
        self.conn=sqlite3.connect('example.db')
        
        #print("Table created successfully")
        print("Connection established")

        self.conn.execute('''CREATE TABLE IF NOT EXISTS Book
                (
                BNAME TEXT NOT NULL,
                ANAME TEXT NOT NULL,
                PRICE FLOAT NOT NULL,
                PUBLISHER TEXT NOT NULL,
                CATEGORY TEXT NOT NULL,
                ISBN TEXT NOT NULL,
                QTY INT NOT NULL
                );''')
        
        print("table created")
        cursor=self.conn.execute("select * from Book")
        for row in cursor:
            print("NAME=",row[0])
            print("AUTHOR NAME=",row[1])
            print("PRICE=",row[2])
            print("PUBLISHER=",row[3])
            print("CATEGORY=",row[4])
            print("ISBN=",row[5])
            print("QTY=",row[6],"\n") 

    def addBook(self):
        
        name=self.bname.text()
        #self.bname.clear()

        author=self.bauthor.text()
        #self.bauthor.clear()

        price=(self.bprice.text())
        #self.bprice.clear()
        
        publisher=self.bpublisher.currentText()
        #print (publisher)
        #self.bpublisher.clear()
        category=self.bcategory.currentText()
        #print (category)
        #self.bcategory.clear()
        isbn=self.bisbn.text()
        #print (isbn)
        #self.bisbn.clear()
        qty=(self.bqty.text())
        #print (qty)
        #self.bqty.clear()
        '''
        dict={"NAME":name,"AUTHOR":author,"PRICE":price,"PUBLISHER":publisher,
              "CATEGORY":category,"ISBN":isbn,"Qty":qty}
        self.blist.append(dict)
        print(self.blist)
        '''
        self.conn.execute('''INSERT INTO Book(BNAME,ANAME,PRICE,PUBLISHER,CATEGORY,ISBN,QTY)
                     VALUES('name','author','price','publisher','category','isbn','qty')''');
        self.conn.commit()
        print("Records inserted successfully")

    def tab2UI(self):
        vbox=QVBoxLayout()
        self.tab2.setLayout(vbox)
        
        group1=QGroupBox("Update Price")
        vbox.addWidget(group1)
        
        group2=QGroupBox("Delete Book")
        vbox.addWidget(group2)

        grid1=QGridLayout()
        group1.setLayout(grid1)
        self.lbluname=QLabel("Enter Book Name")
        self.txtuname=QLineEdit()
        grid1.addWidget(self.lbluname,0,0)
        grid1.addWidget(self.txtuname,0,1)

        self.lbluprice=QLabel("Enter Updated Price")
        self.txtuprice=QLineEdit()
        grid1.addWidget(self.lblprice,1,0)
        grid1.addWidget(self.txtuprice,1,1)

        self.btnprice=QPushButton("Update Price")
        grid1.addWidget(self.btnprice,2,0,1,2)
        self.btnprice.clicked.connect(self.updatePrice)

        grid2=QGridLayout()
        group2.setLayout(grid2)
        self.lblname2=QLabel("Enter Book Name")
        self.txtname2=QLineEdit()
        grid2.addWidget(self.lblname2,0,0)
        grid2.addWidget(self.txtname2,0,1)

        self.btndelete=QPushButton("Delete Record")
        grid2.addWidget(self.btndelete,1,0,1,2)

    def updatePrice(self):
        
        bookname=self.txtuname.text()
        updated=float(self.txtuprice.text())
        self.conn.execute('''UPDATE Book SET PRICE=updated WHERE BNAME=bookname''');
        self.conn.commit()
        print("Price updated successfully")
        
        '''print(bookname,updated)
        for book in self.blist:
            for key,value in book.items():
                print(key,value)
                if value==self.bookname:
                    print("found")
                    book['PRICE']=self.updated
                    print(self.blist)
                    break'''
                    

    def tab3UI(self):
        vbox=QVBoxLayout()
        
        group=QGroupBox()
        vbox.addWidget(group)
        grid1=QGridLayout()
        self.lblname=QLabel("Enter Book Name")
        self.txtname=QLineEdit()
        grid1.addWidget(self.lblname,0,0)
        grid1.addWidget(self.txtname,0,1)

        self.btnsearch=QPushButton("Search Book")
        grid1.addWidget(self.btnsearch,1,0,1,2)
        group.setLayout(grid1)
        self.tab3.setLayout(vbox)

    def tab4UI(self):
        
        grid=QGridLayout()
        self.lblbook=QLabel("Select Book")
        self.b=QComboBox(self)
        self.b.addItem("Willey")
        self.b.addItem("Wrox")
        self.b.addItem("TATA")
        
        grid.addWidget(self.lblbook,0,0)
        grid.addWidget(self.b,0,1)

        self.lblavail=QLabel("Enter number of copies required")
        self.txtavail=QLineEdit()
        grid.addWidget(self.lblavail,1,0)
        grid.addWidget(self.txtavail,1,1)

        self.btncheck=QPushButton("Check")
        grid.addWidget(self.btncheck,2,0,1,2)
        self.tab4.setLayout(grid)

    def tab5UI(self):

        grid=QGridLayout()
        self.lblcname=QLabel("Customer Name")
        self.txtcname=QLineEdit()
        grid.addWidget(self.lblcname,0,0)
        grid.addWidget(self.txtcname,0,1)

        self.lblcnum=QLabel("Contact Number")
        self.txtcnum=QLineEdit()
        grid.addWidget(self.lblcnum,1,0)
        grid.addWidget(self.txtcnum,1,1)

        self.lblcopies=QLabel("Number of Copies")
        self.txtcopies=QLineEdit()
        grid.addWidget(self.lblcopies,2,0)
        grid.addWidget(self.txtcopies,2,1)

        self.lblpaid=QLabel("Total Amount Paid")
        self.txtpaid=QLineEdit()
        grid.addWidget(self.lblpaid,3,0)
        grid.addWidget(self.txtpaid,3,1)

        self.btnsell=QPushButton("Sell")
        grid.addWidget(self.btnsell,4,0,1,2)
        self.tab5.setLayout(grid)
def main():
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
