contact_info = {
    'Junaid' : '996655886',
    'number1' : '445511225',
    'number2' : '556658856',
    'number3' : '446626941',
    'number4' : '115511477'
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
