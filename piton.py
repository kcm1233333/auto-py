
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options=options)
driver.get("https://account.accurate.id/manage")
driver.maximize_window()
driver.implicitly_wait(60)

#f=driver.find_element("xpath", "//li[@class='nav__item']")
#f.click()
#g=driver.find_element("xpath","//li[@class='nav__subitem'][2]")
#g.click()

f=driver.find_element("xpath", "//*[@id='j_username']")
f.send_keys("andiasdi8888@gmail.com")
g=driver.find_element("xpath", "//*[@id='j_password']")
g.send_keys("Freelance3@")
h=driver.find_element("xpath", "//*[@id='btn-login']")
h.click()
i=driver.find_element("xpath", "//*[@id='content']/div/div[2]/div/div/div/div/div[2]")
i.click()
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
def waktuTunda(t):
  for i in range(0,t):
    for j in range(0,t):
       print(i*j)
#d=driver.current_url
#print("New URL : ",str(d))
#while(!driver.find_element("xpath", "//*[@id='accurate__init--0']/div[2]/div[1]/div[1]/ul/li[1]/a")):
 #  break
#j=driver.find_element("xpath", "//*[@id='accurate__init--0']/div[2]/div[1]/div[1]/ul/li[1]/a")
#j.click()
#d=driver.current_url
a=[['sfadhf','hfdgjasg','dgfsgd',30000,0],['gfdjsfgj','dfhgsjhfgj','dgsjgj',0,30000],['dfjhhg','sgdjagd','dfgjfdgjsa',30000,0],['sadhgfhdf','sfdhdfahsd','asfdhgafdgg',15000,0],['dgfjj','djgfsjfg','sdfhsfd',0,15000],['dgfjsgh','dfhsdsfs','hdfhgf',0,35000],['dgfjsgh','dfhsdsfs','hdfhgf',5000,0],['dgggsjd','dfhfhfhf','asfdahdfh',0,8000],['shfasafsh','dahsdfdjfhgah','hgdjggfgjg',8000,0]]
b=len(a)
c=len(a[0])
d=[]
k=[]
total=0
totalwin=0
totalwei=0
vlag=""
summ=0
sumn=0
print(b,'-----',c)
i=0
while (i+totalwei>=0 and i<b):
   summ=summ+a[i][3]
   sumn=sumn+a[i][4]
   print(a[i][2])
   #print(a[i][3])
   #print(a[i][4])
   totalwin+=1
   if(a[i][3]!=0):
      print(totalwin,"--- D")
      print(a[i][3])
   if(a[i][4]!=0):
      print(totalwin,"--- C")
      print(a[i][4])      
   if(summ==sumn):
      totalwei=totalwin
      print(a[totalwei-1][0])
      print(a[totalwei-1][1])
      print("SIMPAN")
   i+=1    
A=[31,34,2,4,1,90,90,66,67,6,6,6,6,34,4,5,4,3,9,10,578,678,45,443,434,4455,454,2333,3232,4,4,4,4,4,4,4,4,4,4,4,44,444,4,5,5,43535,435,4345,3445,4345645,4644,645,46,44,54,45,645,645,645,6,456,456,46,46,456,44464,6546,4564,5645666,44,56,6,56,56,56,56,56,56,56,56,565,66,56,566,56,56,56,56,56,56,5,65,65,65,6,56,56,56,5,65,6,56,564,5645,56456,456,6,6,656,677,767,67,6767,87,89,9,100,100,1233,3343,5646,456,656,656456,64564,54646,445646,5646,546,456,4646,456,46,6,644,66,46664,64654,5566466,4564,5646,4556456,456,64564,4]
n=len(A)
tempat=0
for i in range (2,n):
  tempat=A[i]
  j=i-1
  while(j>=0 and A[j]>tempat):
  #A[i+1]=A[j] 
     A[j+1]=A[j]
     j=j-1
     A[j+1]=tempat  
print(A)    
#print("New URL : ",str(d))
for i in range(0,500):
 for j in range(0,500):
   print(i*j)
#action.click()
#d=driver.current_url
#print("New URL : ",str(d))
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
driver.implicitly_wait(9000)
pyautogui.click(200 ,40)
#pyautogui.click(button='left')
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
for i in range(0,2000):
 for j in range(0,1000):
   print(i*j)
d=driver.current_url
print("New URL : ",str(d))
#driver.find_element("xpath", "//*[@id='post-5910']/div/div[1]/div/div/div/div/div/ul[1]/li[1]/a/span/img").click()   
pyautogui.click(6 ,300)
for i in range(0,300):
 for j in range(0,300):
   print(i*j)
pyautogui.click(70 ,500)
for i in range(0,2000):
 for j in range(0,1000):
   print(i*j)

import xlrd
import pyautogui
book = xlrd.open_workbook("FINREPKCM.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=2, colx=3)))
#import xlsxwriter
#a=[['sfadhf','hfdgjasg','dgfsgd',30000,0],['gfdjsfgj','dfhgsjhfgj','dgsjgj',0,30000],['dfjhhg','sgdjagd','dfgjfdgjsa',30000,0],['sadhgfhdf','sfdhdfahsd','asfdhgafdgg',15000,0],['dgfjj','djgfsjfg','sdfhsfd',0,15000],['dgfjsgh','dfhsdsfs','hdfhgf',0,35000],['dgfjsgh','dfhsdsfs','hdfhgf',5000,0],['dgggsjd','dfhfhfhf','asfdahdfh',0,8000],['shfasafsh','dahsdfdjfhgah','hgdjggfgjg',8000,0]]
b=sh.nrows
totalwin=0
totalwei=0
summ=0
sumn=0
#pyautogui.write(sh.cell_value(rowx=1, colx=5))
#workbook = xlsxwriter.Workbook('dmfirst.xlsx')
#worksheet = workbook.add_worksheet()
i=0
#Giorrando
while (i+totalwei>=0 and i<b):
   #print(sh.cell_value(rowx=1, colx=5)+1)
   summ=summ+sh.cell_value(rowx=i, colx=4)
   sumn=sumn+sh.cell_value(rowx=i, colx=5)
   
   totalwin+=1
   if(sh.cell_value(rowx=i, colx=4)!=0):
      pyautogui.click(120 ,360)#Memasukkan tipe akun
      pyautogui.write(str(sh.cell_value(rowx=i, colx=3)))
      pyautogui.press('up')   
      pyautogui.press('enter')
      waktuTunda(1000)
      pyautogui.click(610, 363)#Menentukan D
      #waktuTunda(1000)
      pyautogui.click(710, 410)#Menentukan nilai
      pyautogui.write(str(sh.cell_value(rowx=i, colx=4)))
      pyautogui.press('delete')#menentukan nilai
      pyautogui.click(870, 630)#Tekan Lanjut585000.0      #waktuTunda(1000)
   else:
      pyautogui.click(120 ,360)#Memasukkan tipe akun
      pyautogui.write(str(sh.cell_value(rowx=i, colx=3)))
      pyautogui.press('up')   
      pyautogui.press('enter')
      waktuTunda(1000)
      pyautogui.click(870, 630)#Tekan Lanjut
   if(sh.cell_value(rowx=i, colx=5)!=0):
      pyautogui.click(120 ,360)#Memasukkan tipe akun
      pyautogui.write(str(sh.cell_value(rowx=i, colx=3)))
      pyautogui.press('up')   
      pyautogui.press('enter')
      waktuTunda(1000)
      pyautogui.click(710, 363)#Menentukan C
      #waktuTunda(1000)
      pyautogui.click(710, 410)#Menentukan nilai
      pyautogui.press('delete')#menentukan nilai
      #waktuTunda(1000)
      pyautogui.write(str(sh.cell_value(rowx=i, colx=5)))
      pyautogui.click(870, 630)#Tekan Lanjut
      #waktuTunda(1000)
   else:
      pyautogui.click(120 ,360)#Memasukkan tipe akun
      pyautogui.write(str(sh.cell_value(rowx=i, colx=3)))
      pyautogui.press('up')   
      pyautogui.press('enter')
      waktuTunda(1000)
      pyautogui.click(870, 630)#Tekan Lanjut
   if(summ==sumn):
      totalwei=totalwin
      pyautogui.click(300,250)#Memasukkan tanggal
      pyautogui.write(str(sh.cell_value(rowx=totalwei-1,colx=6)))
      pyautogui.click(90 ,400)#Memasukkan keterangan
      pyautogui.click(400 ,400)
      pyautogui.write(str(sh.cell_value(rowx=totalwei-1,colx=1)))
      pyautogui.click(1300, 290)#Tekan SIMPAN
      
      
      
   i+=1       
driver.quit()
