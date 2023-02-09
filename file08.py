def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=[]
    for i in data:
        if i.isdigit():
            a.append(i)
    
        
    return a
    
# Read data from file
f=open('txt_file/data08.txt')
data=f.read()
print(main(data))

