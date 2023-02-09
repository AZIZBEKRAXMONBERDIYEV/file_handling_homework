def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x1=0
    for i in data:
        if i.isalpha():
            x1+=1
        if i=='\n':
            x1+=1

    x2=0
    for i in data:
        if i.isdigit():
            x2+=1

    return [x2,x1]
# Read data from file
f=open('txt_file/data05.txt')
data=f.read()
print(main(data))
