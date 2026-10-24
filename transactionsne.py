totalTrans,totalSales=0,0
count=1
while count<7:
    trans=int(input("enter transaction made on a day"+str(count)+":"))
    items=int(input("items sold on day "+str(count)+":"))
    totalTrans+=trans
    totalSales+=items
    count+=1

avgsales=totalSales/totalTrans
print("Total Sales made:",totalSales)
print("Total Transactions made:",totalTrans)
print("Average Sales per Transactions:",avgsales)
    