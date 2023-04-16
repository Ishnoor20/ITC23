#integral value for number of seconds
no_of_seconds=int(input("Enter no of Seconds:"))
#if value to ensure less than 60 seconds are printed as is
if(no_of_seconds<60):
    print("no of seconds",no_of_seconds,"seconds")
#else to ensure higher input values are caluclated as minutes and the remainder as seconds
else:
    e=no_of_seconds//60
    f=no_of_seconds%60

    print(e,"minutes", "and", f,"seconds")
