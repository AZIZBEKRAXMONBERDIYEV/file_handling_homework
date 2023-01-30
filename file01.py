def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=[]
    s.append(data)
    return s

# Read data from file
f=open('txt_file/data01.txt')
data=f.read()
print(main(data))