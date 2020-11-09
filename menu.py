import os
import getpass

os.system("tput setaf 3")
print("\t\t\tWelcome to my Menu !!")
os.system("tput setaf 7")

passwd=getpass.getpass("Enter your password : ")

if passwd!="lw":
   print("Password incorrect ...")
   exit()
r=input("Where do you want to run this menu? (Local/Remote)? : ")
print(r)

while True:
    os.system("clear")
    print("""
    \n
    press 1: To run date cmd
    press 2: To create Security group on AWS
    press 3: To create EBS volume on AWS
    press 4: To launch EC2 instance on AWS
    press 5: To set up webserver on VM
    press 6: To Exit
    """)
    ch=input("Enter your choice : ")
    print(ch)
    
    if r=="local":
       if int(ch)==1:
          os.system("date")
       elif int(ch)==2:
          os.system('aws ec2 create-security-group --group-name autosecgrp --description "Security group from program"')
       elif int(ch)==3:
          os.system('aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2')
       elif int(ch)==4:
          os.system('aws ec2 run-instances --image-id ami-0e306788ff2473ccb --count 1 --instance-type t2.micro --key-name awsclikey --subnet-id subnet-59037915')
       elif int(ch)==5:
          os.system("yum install httpd")
          os.system("cp /root/webpages/index.html /var/www/html")
          os.system("systemctl start httpd")
       elif int(ch)==6:
          exit()
       else:
          print("Option not supported") 
    elif r=="remote":
       ip=input("Enter your remote ip : ")
       print(ip)
       if int(ch)==1:
          os.system("ssh {} date".format(ip))
       elif int(ch)==2:
          os.system('ssh {} aws ec2 create-security-group --group-name autosecgrp --description "Security group from program"'.format(ip))
       elif int(ch)==3:
          os.system('ssh {} aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2'.format(ip))
       elif int(ch)==4:
          os.system('ssh {} aws ec2 run-instances --image-id ami-0e306788ff2473ccb --count 1 --instance-type t2.micro --key-name awsclikey --subnet-id subnet-59037915'.format(ip))
       elif int(ch)==5:
          os.system("ssh {} yum install httpd".format(ip))
          os.system("ssh {} cp /root/webpages/index.html /var/www/html".format(ip))
          os.system("ssh {} systemctl start httpd".format(iP))
       else:
          print("Not Supported")
    else:
       print("Not supported log in....")

    input("\nPress enter to continue...")
