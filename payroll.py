import mysql.connector as sqltor
mycon=sqltor.connect(host='127.0.0.1',port='3307',user='root',passwd='jeemain
s',database='project')
if mycon.is_connected()==False:
 print("Error connecting to Database")
cursor=mycon.cursor()
def designation():
 st="select Emp_id,Emp_name,Designation from employeedetails"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def Phone_no():
 st="selecr Emp_id,Emp_name,PhoneNumber from employeedetails"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def design(x):
 st="select * from employeedetails where Designation='%s'"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def empdetails(x):
 st="select * from employeedetails where Emp_name='%s'"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def order_name():
 cursor.execute("SELECT * FROM employeedetails ORDER BY Emp_Name
ASC")
 data=cursor.fetchall()
 for row in data:
 print(row)
def countdesig():
 st="select count('Designation')'Total Designation' from employeedetails"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def distinctsdesign():
 st="select count(DISTINCT Designation)'Distinct Designstion' from
employeedetails"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def basesal():
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.BaseSalary from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def base_sal_max():
 cursor.execute("select max(BaseSalary)'Maximum Base Salary' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def base_sal_min():
 cursor.execute("select min(BaseSalary)'Minimum Base Salary' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def allowances():
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Allowances from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def max_allowance():
 cursor.execute("select max(Allowances) 'Maximum Allowances' from
salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def min_allowance():
 cursor.execute("select min(Allowances) 'Minimium Allowances' from
salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def gratuity():
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Gratuity from employeedetails,salary where
salary.Emp_id=employeedetails.Emp_id"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def max_gratuity():
 cursor.execute("select max(Gratuity) 'Maximum Gratuity' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def min_gratuity():
 cursor.execute("select min(Gratuity) 'Minimum Gratuity' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def tax():
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Tax
from employeedetails,salary and salary.Emp_id=employeedetails.Emp_id"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def max_tax():
 cursor.execute("select max(Tax) 'Maximum Tax' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def min_tax():
 cursor.execute("select min(Gratuity) 'Manimum Tax' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def total():
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Total
from employeedetails,salary where salary.Emp_id=employeedetails.Emp_id"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def max_total():
 cursor.execute("select max(Total) 'Maximum Total Salary' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def min_total():
 cursor.execute("select min(Total) 'Minimum Total Salary' from salary")
 data=cursor.fetchall()
 for row in data:
 print(row)
def banks(x):
 st="select * from salary where BankName='%s'"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
 
def bank_count():
 st="select count(BankName)'Total No of Banks' from salary"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def dis_bank_count():
 st="select count(DISTINCT BankName)'Total No differnt of Banks' from
salary"
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def base_emp(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.BaseSalary from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id and Emp_id= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def grat_emp(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Gratuity from employeedetails,salary where
salary.Emp_id=employeedetails.Emp_id and Emp_id= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def allow_emp(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Allowances from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id and Emp_id= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def tax_emp(x):
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Tax
from employeedetails,salary where salary.Emp_id=employeedetails.Emp_id
and Emp_id= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def total_emp(x):
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Total
from employeedetails,salary where salary.Emp_id=employeedetails.Emp_id
and Emp_id= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def base_emp_name(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.BaseSalary from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id and Emp_name= '%s'"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def grat_emp_name(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Gratuity from employeedetails,salary where
salary.Emp_id=employeedetails.Emp_id and Emp_name= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def allow_emp_name(x):
 st="select employeedetails.Emp_id,
employeedetails.Emp_name,salary.Allowances from employeedetails,salary
where salary.Emp_id=employeedetails.Emp_id and Emp_name= '%s'"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def tax_emp_name(x):
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Tax
from employeedetails,salary where salary.Emp_id=employeedetails.Emp_id
and Emp_name= '%s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def total_emp_name(x):
 st="select employeedetails.Emp_id, employeedetails.Emp_name,salary.Total
from employeedetails,salary where salary.Emp_id=employeedetails.Emp_id
and Emp_name= %s"%(x)
 cursor.execute(st)
 data=cursor.fetchall()
 for row in data:
 print(row)
def emp_sal(x):
 st="select salary.*,employeedetails.Emp_id from salary,employeedetails
where Emp_name='%s' and employeedetails.Emp_id=salary.Emp_id"%(x)
 cursor.execute(st)
 dats=cursor.fetchall()
 for row in data:
 print(row)
def emp_sal_id(x):
 st="select salary.*,employeedetails.Emp_id from salary,employeedetails
where Emp_id= %s and employeedetails.Emp_id=salary.Emp_id"%(x)
 cursor.execute(st)
 dats=cursor.fetchall()
 for row in data:
 print(row)
def sal():
 st="select * from salary"
 cursor.execute(st)
 dats=cursor.fetchall()
 for row in data:
 print(row)
def insert_into_empdetails(x,y,z,r):
 st=" INSERT INTO
project.employeedetails(Emp_id,Emp_name,Designation,PhoneNumber)
VALUES (%s,'%s','%s',%s)"%(x,y,z,r)
 cursor.execute(st)
 mycon.commit()
def insert_into_salary(x,y,z,r,s,q,t):
 st=" INSERT INTO
project.salary(Emp_id,BankName,BaseSalary,Allowances,Gratuity,Tax,Total)
VALUES (%s,'%s',%s,%s,%s,%s,%s)"%(x,y,z,r,s,q,t)
 cursor.execute(st)
 mycon.commit()
print("Welecome to our company")
ch=0
n=0
while(n <=3):
 print("\t--")
 print("Admin Portal")
 print("\t--")
 print("1.To enter details of Employees")
 print("2.To enter details of Salary of Employee")
 print("3.Exit")
 n=int(input("Enter your choice"))
 if n==1:
 x=int(input("Enter Emp_ID"))
 y=str(input("Enter Employee's Name"))
 z=str(input("Enter the Employee's Designation"))
 r=int(input("Enter the Employee's Phone no."))
 insert_into_empdetails(x,y,z,r)
 elif n==2:
 X=int(input("Enter Emp_ID"))
 Y=str(input("Enter Bank Name"))
 Z=int(input("Enter the Base Salary"))
 R=int(input("Enter the Allowance"))
 s=int(input("Enter the Gratuity"))
 q=int(input("Enter the Tax"))
 t=Z+R+s-q
 insert_into_salary(X,Y,Z,R,s,q,t)
 elif n==3:
 break
 else:
 print("Invalid Choice:")

while(ch <=39 ):
 print("\t--")
 print("Menu")
 print("\t--")
 print("1.For all of our employees details")
 print("2.For all of our employees designation")
 print("3.For all of our employees phone no.")
 print("4.To search details of all the employess of a paricular designation")
 print("5.To search details of a particular employee")
 print("6.To count total no of designation")
 print("7.To count total no of distinct designations")
 print("8.To find Base Salary of all the employees")
 print("9.To find the maximum Base Salary")
 print("10.To find the minimum Base Salary")
 print("11.To find Allowances of all the employees")
 print("12.To find the maximum Allowance")
 print("13.To find the minimum Allowance")
 print("14.To find Gratuity of all the employees")
 print("15.To find the maximum Gratuity")
 print("16.To find the minimum Gratuity")
 print("17.To find Taxes of all the employees")
 print("18.To find the maximum Tax")
 print("19.To find the minimum Tax")
 print("20.To find Total Salary of all the employees")
 print("21.To find the maximum Total Salary")
 print("22.To find the minimum Total Salary")
 print("23.To find paycheck details by Bank Name")
 print("24.To find total no. of Banks")
 print("25.To find total no. of distinct Banks")
 print("26.To find Salary of all the employees")
 print("27.To find Base Salary by Employee Name")
 print("28.To find Base Salary by Employee Id")
 print("29.To find Gratuity by Employee Name")
 print("30.To find Gratuity by Employee Id")
 print("31.To find Allowances by Employee Name")
 print("32.To find Allowances by Employee Id")
 print("33.To find Tax by Employee Name")
 print("34.To find Tax by Employee Id")
 print("35.To find Total Salary by Employee Name")
 print("36.To find Total Salary by Employee Id")
 print("37.To find salary details by Employee Name")
 print("38.To find salary details by Employee Id")
 print("39.To EXIT")
 ch=int(input("Enter your choice(1-39):"))
 if ch==1:
 order_name()
 elif ch==2 :
 designation()
 elif ch==3 :
 Phone_no()
 elif ch==4 :
 x=str(input("Enter the Designation"))
 design(x)
 elif ch==5 :
 y=str(input("Enter the Employee's Name"))
 empdetails(y)
 elif ch==6 :
 countdesig()
 elif ch==7 :
 distinctsdesign()
 elif ch==8 :
 basesal()
 elif ch==9 :
 base_sal_max()
 elif ch==10 :
 base_sal_min()
 elif ch==11 :
 allowances()
 elif ch==12 :
 max_allowance()
 elif ch==13 :
 min_allowances()
 elif ch==14 :
 gratuity()
 elif ch==15 :
 max_gratuity
 elif ch==16 :
 min_gratuity
 elif ch==17 :
 tax()
 elif ch==18 :
 max_tax()
 elif ch==19 :
 min_tax()
 elif ch==20 :
 total()
 elif ch==21 :
 max_total()
 elif ch==22 :
 min_total()
 elif ch==23 :
 X=str(input("Enter the Bank Name"))
 banks(X)
 elif ch==24 :
 bank_count()
 elif ch==25:
 dis_bank_count()
 elif ch==26:
 sal()
 elif ch==27:
 e=str(input("Enter the Employee's Name"))
 base_emp_name(e)
 elif ch==28:
 f=int(input("Enter the Employee's ID"))
 base_emp(f)
 elif ch==29:
 g=str(input("Enter the Employee's Name"))
 grat_emp_name(g)
 elif ch==30:
 h=int(input("Enter the Employee's ID"))
 grat_emp(h)
 elif ch==31:
 i=str(input("Enter the Employee's Name"))
 allow_emp_name(i)
 elif ch==32:
 o=int(input("Enter the Employee's ID"))
 allow_emp(o)
 elif ch==33:
 X=str(input("Enter the Employee's Name"))
 tax_emp_name(X)
 elif ch==34:
 Y=int(input("Enter the Employee's ID"))
 tax_emp(Y)
 elif ch==35:
 Z=str(input("Enter the Employee's Name"))
 total_emp_name(Z)
 elif ch==36:
 A=int(input("Enter the Employee's ID"))
 total_emp(A)
 elif ch==37:
 S=str(input("Enter the Employee's Name"))
 emp_sal(S)
 elif ch==38:
 R=int(input("Enter the Employee's ID"))
 emp_sal_id(R)
 elif ch==39:
 break
 else:
 print("You have entered the wrong Choice") 
