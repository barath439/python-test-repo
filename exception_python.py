def division(a,b):
    try:
        out= a/b
        return out
    except Exception as e:
        print("there are some issues with division",e)
        adds=a+b
        print(adds)


result=division(12,0)
print(result)