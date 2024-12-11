print("Phone contact apk is open:\n1:Add number\n2:Search number\n3:Edit number\n4:Delete number\n5:Call number\n6:recents calls\n7:Exit Apk.")
call_list = []
ringing = []
########################################################################################
def phone_contact():
    ordre_phone = int(input("Enter number to order:\n"))
########################################################################################    
    if ordre_phone == 1:
        # إضافة رقم جديد
        name = input("Enter the name: \n")
        number = input("Enter the number: \n")
        call_list.append({"name": name, "phone": number})
        print(call_list)  # عرض الأرقام المدخلة
#########################################################################################   
    elif ordre_phone == 2:
        # البحث عن رقم
        search = input("Name for search: \n").strip().lower()
        found = False 
        for contact in call_list:
            if contact["name"].lower() == search.lower():
                print(f"Phone number for {contact['name']}: {contact['phone']}")
                found = True
                break
        if not found:
            print("Name not found in the phone book.")
########################################################################################    
    elif ordre_phone == 3:
      
        eddit_name = input("Enter the name for editing number: \n")
        found = False 
        for contact in call_list:
            if contact["name"].lower() == eddit_name.lower():
                print(f"Phone number for {contact['name']}: {contact['phone']}")
                new_number = input("Enter the new number for the name: \n")
                contact["phone"] = new_number  # تحديث الرقم
                print(f"Your new number for {eddit_name} is {new_number}")
                found = True
                break
        if not found:
            print("Name not found in the phone book.")
    elif  ordre_phone == 4:
        delet = input("Enter name for delet numbe: \n")   
        for contact in call_list:
            if  contact["name"].lower()== delet.strip().lower():
                print(f"Phone number for {contact['name']}: {contact['phone']}:")
                del contact['phone']
                print(contact)
########################################################################################
    elif ordre_phone == 5:
        call = input("Enter phone to call the guy: \n")
        for contact in call_list:
            if call == contact['phone']:
                print("ringing.................\n")
                ringing.append(call)  
            else:
                print("not found phone the guy")
########################################################################################
    elif ordre_phone == 6:
        for index, i in enumerate (ringing, start = 1):
            print(f"{index}: {i}")
########################################################################################    
    elif ordre_phone == 7:  
        print("Goodbye!")
        return False
    
    else:
        print("Invalid choice. Please enter a valid option.")

    return True  

########################################################################################
while True:
    if not phone_contact():
        break
        

#A simple project I did to prove the basics I learned and I learned new things.