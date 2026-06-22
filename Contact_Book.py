contact_info = {
    'Junaid' : '996655886',
    'mother' : '445511225',
    'father' : '556658856',
    'sister' : '446626941',
    'other' : '115511477'
}
# print(contact_info['Junaid'])
while True :
    name = input("Enter name of the person; ")
    if name in contact_info  :
        print(contact_info[name])
    if name == 'exit':
        break
    else :
        print("number not exist")