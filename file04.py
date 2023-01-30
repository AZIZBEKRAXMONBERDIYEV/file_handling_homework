def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data:
        if i.isidentifier():
            a.append(i)
        if i=='\n':
            a.append('\n')
    return a
    
# Read data from file
f=open('txt_file/data04.txt')
data=f.read()
print(main(data))