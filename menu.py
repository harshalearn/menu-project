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
    press 6: To create partition and load drivers on VM
    press 7: To format partition on VM
    press 8: To mount partition on VM
    press 15: To Exit
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
    

          os.system("fdisk -l")
          print()

          print("!!!!!ATTENTION!!!!!!Please note that you can only create 4 primary partitions and you cannot go beyond the size of harddisk!!!!!!")  

          print()

          dev=input("Enter your hardisk name from available devices : ")
          print()
    
          while True:

              print("""
              \n
              press p: For listing available partitions
              press n: For creating new partition
              press d: For deleting partition
              press e: For exiting partition section
              """)

              pch=input("Enter partition choice from above options : ")

              print()

              if pch=='p':
                 os.system("(echo {})|fdisk {}".format(pch,dev))
              elif pch=='d':
                 print()
                 pdel=input("Enter partition number to be deleted : ")
                 
                 pdelch=input("Are you sure you want to delete partition {} ? Type y for yes or n for No : ".format(pdel))
                 
                 if pdelch=="y":

                    os.system("(echo {}; echo {}; echo w)|fdisk {}".format(pch,pdel,dev))
                 elif pdelch=="n":
                    print("partition number {} not deleted".format(pdel))
                 else:
                    print("Going back to main partition menu....")
                 
              elif pch=='n':
                 ptype=input("Enter partition type. p for primary or e for extended: ")

                 print()

                 psize=input("Enter your partition size. Append K for KiB: M for MiB: G for GiB: T for TiB: P for PiB : ")
          
                 print()

                 pcommit=input("Please review all your selected options and if you are okay press w to save otherwise q to quit without saving : ")

                 print()

                 os.system("(echo {}; echo {}; echo ''; echo ''; echo {}; echo {})|fdisk {}".format(pch,ptype,psize,pcommit,dev))

                 if pcommit=='w':
                    
                    os.system("udevadm settle")
               
              elif pch=='e':
                 break
              else:
                 print("selected partition option not supported")
                 break
   
          print()

       elif int(ch)==7:
    

          os.system("fdisk -l")

          print()

          hdname=input("Enter your device name from above listed devices : ")

          os.system("fdisk -l {}".format(hdname))
 
          print()

          pname=input("Enter your partition name from above listed partitions for formatting : ")

          print()

          fstype=input("Enter your file system name for formatting : ")

          print()

          os.system("mkfs.{} {}".format(fstype,pname))

       elif int(ch)==8:
    

          os.system("fdisk -l")

          print()

          hdname=input("Enter your device name from above listed devices : ")

          os.system("fdisk -l {}".format(hdname)) 

          print()

          pname=input("Enter your partition name for mounting from above listed partitions: ")

          print()

          dirmount=input("Enter your directory name for mounting : ")

          print()

          os.system("mkdir {}".format(dirmount))

          os.system("mount {} {}".format(pname,dirmount))

       elif int(ch)==15:
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
