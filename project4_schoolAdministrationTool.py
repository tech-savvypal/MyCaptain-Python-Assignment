#Building a basic School Administration tool
import csv
def convert_to_csv(str_list):
    with open('s_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact No.","E-mail ID"])
        writer.writerow(str_list)
if __name__ == '__main__':
    condition=True
    s_num=1
    #while loop for taking student information as input from the user of this tool
    while(condition):
        s_info=input("Enter student #{} information in the following format (Name Age Contact_No. E-mail_ID):".format(s_num))
        #splitting the entered string
        str_split=s_info.split(' ')
        print("\nThe entered information is:\nName: {}\nAge: {}\nContact No.: {}\nE-mail ID: {}".format(str_split[0],str_split[1],str_split[2],str_split[3]))
        check=input("Is the entered information correct? (yes/no):")
        if check=="yes":
            convert_to_csv(str_split)
            #checking if the user wants to enter more student information or not
            check=int(input("Enter 1 if you want to enter more student information and enter 0 if you do not want to enter student information:"))
            if check==1:
                condition=True
                s_num=s_num+1
            elif check==0:
                condition=False
        elif check=="no":
            print("\nPlease re-enter the information")