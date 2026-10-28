googleSAL=eval(input("GOOGLE sales list:"))
awsSAL=eval(input("AWS sales list:"))
gcost=eval(input("GOOGLE cost list"))
acost=eval(input("AWS cost list"))
gpro=sum(googleSAL)-sum(gcost)
apro=sum(awsSAL)-sum(acost)
gros=gpro/sum(googleSAL)
aros=apro/sum(awsSAL)
print("Return on sales for GOOGLE:",gros*100,"%")
print("Return on sales for AWS:",aros*100,"%")
if gros>aros:
    print("GOOGLE co. is better at cost-cutting while increasing revenue ")
elif gros<aros:
    print("AWS co. is better at cost-cutting while increasing revenue ")
else:
    print("both companies are doing equal at cutting costs")
        



