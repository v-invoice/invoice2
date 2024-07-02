from tabulate import tabulate
complete=False
userData=[]
while complete==False:
    
    ID = str(input('User ID '))
    username = str(input('Username '))
    password = str(input('Password Hash '))
    role=str(input('Role '))

    #if role == ''
   
    row=[ID, username, password, role]
    userData.append(row)   
    header=['User ID','Username', 'Password', 'Role']
    print(tabulate(userData, headers=header, tablefmt="fancygrid"))

    finish = str(input('Complete? '))
    if finish=='yes':
        complete=True
