import os
import getpass
passwd = getpass.getpass("Enter the passsword\n")

if passwd!="eku":
  print("incorrect")
  exit()
print("where you want to run the program (locally/remotely)")
wish = input()
while True:
  os.system("clear")
  if wish=="locally":
    print("Press 1: For date command")
    print("Press 2: For cal command:")
    print("Press 3: To exit")
    print("Press 4: To configure Apache Web server")
    print("Press 5: To start Docker")
    print("Press 6: To launch your Container")
    print("Press 7: To Enter inside the OS")
    print("Press 8: Create Partition Using LVM and provide elasticity to the namnode")
    print("Press 9: TO launch OS on AWS Cloud")
    print("PRESS 10: TO Create EBS Vol on AWS Cloud")
    n = int(input("enter the number: "))
    if n==1:
      os.system("date")
    elif n==2:
      os.system("cal")
    elif n==3:
      exit()
    elif n==4:
      os.system("cd /var/www/html")
      os.system("echo 'my webserver configured using python' > /var/www/html/ekansh.html")
      os.system("setenforce 0")
      os.system("systemctl start httpd")
      print("Configured Sucessfully")
      os.system("ifconfig enp0s3")
    elif n==5:
      os.system("systemctl start docker")
      print("Docker Service has Activated")
    elif n==6:
      os.system("docker images")
      osname = input("Enter your OS name\n")
      imgname = input("Enter your Image Name")
      os.system("docker run -dit --name {} {}".format(osname,imgname))
    elif n==7:
      os.system("docker attach {}".format(osname))
    elif n==8:
      os.system("pvcreate /dev/sdb")
      os.system("vgcreate vg /dev/sdb")
      os.system("lvcreate --size +2G --name lv vg")
      os.system("mkfs.ext4 /dev/vg/lv")
      os.system("mount /dev/vg/lv /hello")
      os.system("hadoop dfsadmin -report | less")
    elif n==9:
      os.system("1) aws ec2 run-instances --image-id ami-015a6758451df3cb9 --instance-type t2.micro --count 1 --subnet-id subnet-9f7df1c6 --security-group-ids sg-02089309c3d33f824")
    elif n==10:
      os.system("aws ec2 create-volume --size 10 --availability-zone ap-southeast-1c")
  elif wish == "remotely":
      ip = input("enter the ip address: ")
      print("Press 1: for date command")
      print("Press 2: for cal command:")
      print("Press 3: to exit")
      n = int(input("enter the number: "))
      if n==1:
        os.system("ssh {} date".format(ip))
      elif n==2:
        os.system("ssh {} cal".format(ip))
      elif n==3:
        exit()
  else:
  print("Not Valid")
  input("Press Enter to Proceed")
