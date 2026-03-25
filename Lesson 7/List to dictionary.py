def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result
students=[[1,'Jean Castro','V'],[2,'Lulu Powell','V'],'3','Brian Howell','VI']
print("\nOriginal list of lists:")
print(students)

print("\nConverted lists to a dictionary:")
print(test(students))
