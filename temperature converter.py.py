temp=input("input the temperature you want to convert?")

degree=int(temp[:-1])
i_conversion=temp[-1]

if i_conversion.upper()=="C":
    result=int(round((9*degree)/5+32))
    o_conversion="Fahrenhiet"
    
elif i_conversion.upper()=="F":
    result=int(round((degree-32)*5/9))
    o_conversion="celsius"
else:
    
    print("input proper conversion")
    quit()
    
print("\n")
print("the temperature in",o_conversion,"is",result,"degree")
