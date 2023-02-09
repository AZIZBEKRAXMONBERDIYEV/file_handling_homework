def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x1=data.split('\n')
    x2=[]
    for i in x1:
        
        x2.append(len(i))
    return x2
    
# Read data from file
f=open('txt_file/data06.txt')
data=f.read()
print(main(data))