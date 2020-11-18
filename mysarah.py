import subprocess
import pyttsx3
import getpass
import os
 
from termcolor import colored, cprint
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate


#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Please enter your password")
passwd = getpass.getpass("Enter your password: ")
if passwd == "amisha":
	print("\nSuccessfully logged in.\n ")
else:
	print("Your password is wrong")
	pyttsx3.speak("Your password is wrong")  
	exit()

print("-------------------------------------------------------------> SARAH: YOUR VIRTUAL ASSISTANT <------------------------------------------------------------ \n\n ".center(150))
#print("............ PYTHON MENU ............".center(150))                    
engine.runAndWait()
pyttsx3.speak("I am SARAH your VIRTUAL ASSISTANT. I am here to help you.")
 
#print("\n Press 1: AWS Cloud Automation \n Press 2: Hadoop Cluster Automation \n Press 3: Docker Automation \n Press 4: LVM Automation \n Press 5: To Exit ")


cprint("""
                     
                                                             ! Welcome To Sarah Menu Bar !
              
                                                      --------------------------------------------       
                                                      || OPTIONS ||      SARAH SERVICES         ||       
                                                      --------------------------------------------       
                                                      || Press 1 ||    AWS Cloud Automation     ||       
                                                      --------------------------------------------       
                                                      || Press 2 ||   Hadoop Cluster Automation ||       
                                                      --------------------------------------------       
                                                      || Press 3 ||       Docker Automation     ||       
                                                      --------------------------------------------       
                                                      || Press 4 ||      LVM Automation         ||       
                                                      --------------------------------------------         
                                                      || Press 5 ||           Exit              ||       
                                                      --------------------------------------------
  
                    
           """, 'green')

pyttsx3.speak("This is Sarah menu bar, please enter your choice")
 
while True:
  print()
  p = input("Enter your choice: ")




   
  if ("1" in p):
    pyttsx3.speak("Welcome to AWS Cloud menu")
    print("-----> AWS CLOUD MENU BAR <-----\n".center(150))
    print(" Press 1: Login to AWS CLI \n Press 2: To launch an EC2 instance \n Press 3: To create an EBS Volume \n Press 4: To attach EBS volume to ec2 instance \n Press 5: To stop the EC2 instance \n Press 6: To Exit ")	  
    while True:
      print()
      a = input("Enter your choice: ")
      if ("1" in a):
        pyttsx3.speak("Starting AWS cloud services ")
        os.system("aws configure")
        print("----> Successfully logged in AWS Cloud <----")	

      elif ("2" in a):
        pyttsx3.speak("Please enter your security group id")
        b = input("Enter Your Security Group ID :")
        pyttsx3.speak("Please enter your Instance type")
        f = input("Enter Your Instance Type :")
        pyttsx3.speak("Please enter your Key name")
        d = input("Enter Your Key Name :")
        pyttsx3.speak("Please enter your AMI ID")
        ami = input("Enter AMI id : ")
        pyttsx3.speak("How many instances you want to launch?")
        c = input("How many instances you want to launch? :")
        os.system("aws ec2 run-instances --security-group-ids {} --instance-type {} --image-id {}  --key-name {} --count {} ".format(b , f , ami , d , c))
        pyttsx3.speak("Successfully Launched EC2 instance")
        print("Successfully launched EC2 instance!!")
        
      elif ("3" in a):
        pyttsx3.speak("Please select the volume type")
        vol = input("Enter volume type(gp2/io1/io2/sc1/st1/standard) :")
        pyttsx3.speak("How much amount of EBS you want")
        amt = input("How much amount of EBS you want :")
        pyttsx3.speak("Enter your Availability Zone")
        az = input("Enter your Availability Zone :")
        os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vol , amt , az))
        pyttsx3.speak("Successfully Created EBS Volume")
        print("Successfully Created EBS Volume!!")

      elif ("4" in a):
        pyttsx3.speak("Please Enter your Volume ID")
        vol = input("Enter your Volume ID :")
        pyttsx3.speak("Please Enter your Instance ID")
        id = input("Enter your Instance ID :")
        os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(vol , id))
        pyttsx3.speak("Attaching EBS volume to the EC2 instance")
        print("Attaching EBS volume to the EC2 instance")

      elif ("5" in a):
        pyttsx3.speak("Please Enter EC2 Instance ID that you want to Shut-down")
        id = input("Enter EC2 Instance ID that you want to Shut-down : ")
        os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
        pyttsx3.speak("Shutting-down EC2 instance")
        print("Shutting-down EC2 instance")

      elif ("6" in a) or ("exit" in a):
        pyttsx3.speak("closing AWS cloud")
        print("-----> Closing AWS Cloud <-----\n".center(150))
        break
      else:
        pyttsx3.speak("This option is invalid")
        print("This is invalid")
            

  elif ("2" in p):
    pyttsx3.speak("Welcome to Hadoop Cluster Automation menu bar")
    print("-----> HADOOP CLUSTER MENU BAR <-----".center(150))
    print(" Press 1: To download softwares (requirements) \n Press 2: To configure Name Node \n Press 3: To configure Data Node \n Press 4: To configure Client Node \n Press 5: To upload data to Hadoop Cluster \n Press 6: To stop the Name Node \n Press 7: To stop the Data Node \n Press 8: To exit")

    while True:
      print()
      a = input("Enter your choice: ")
      if ("1" in a):
        pyttsx3.speak("Downloading the Hadoop requirements")
        os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
        os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
        print("\nSoftwares are Sucessfully Installed In Name Node".center(150))
        print("\n---------------------------------------------------------------------".center(150))
        b = input("Enter Your Data Node IP :")
        os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(b))
        os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(b))
        print("\nSoftwares are Sucessfully Installed In Data Node".center(150))
        print("\n---------------------------------------------------------------------".center(150))
        s = input("Enter Your Client Node IP :")
        os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(s))
        os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(s))
        print("\nSoftwares are Sucessfully Installed In Client Node".center(150))
      elif ("2" in a):
        pyttsx3.speak("Configuring Name Node")
        pyttsx3.speak("Please enter the directory name for the name node")
        dir = input("Enter the directory name : ")
        pyttsx3.speak("configuring hdfs-site.xml file")
        print("!!Configuring hdfs-site.xml file!!".center(150))
        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
        os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
        os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
        os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
        os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
        os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
        os.system('echo -e "</property>" >> /root/hdfs-site.xml')
        os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
        os.system('rm -rf /etc/hadoop/hdfs-site.xml')
        os.system('cp  /root/hdfs-site.xml  /etc/hadoop')
        os.system('rm -rf /root/hdfs-site.xml')
        print("\n -----> Formatting the Name Node <-----".center(150))
        pyttsx3.speak("Formatting the name node")
        print()
        os.system('hadoop namenode -format')
        print()
        print()
        pyttsx3.speak("Please enter the name node ip address")
        nip = input("Enter Name Node IP : ")
        pyttsx3.speak("Configuring core-site.xml file")
        print("!!Configuring core-site.xml file!!".center(150))
        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
        os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
        os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
        os.system('echo -e "\n<property>" >> /root/core-site.xml')
        os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
        os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
        os.system('echo -e "</property>" >> /root/core-site.xml')
        os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
        os.system('rm -rf /etc/hadoop/core-site.xml')
        os.system('cp  /root/core-site.xml  /etc/hadoop')
        os.system('rm -rf /root/core-site.xml')
        print("\n--------------------------------------------------------------".center(150))
        print("\n -----> Starting Hadoop Name Node Services <-----".center(150))
        pyttsx3.speak("Starting hadoop name node services")
        os.system('hadoop-daemon.sh start namenode') 
        os.system('jps')
      elif ("3" in a):
        pyttsx3.speak("Configuring data node")
        pyttsx3.speak("Please enter data node ip address")
        dip = input("Enter Data Node IP : ")
        pyttsx3.speak("Please enter directory name for the data node")
        dio = input("Enter directory name : ")
        pyttsx3.speak("Configuring hdfs-site.xml file")
        print("!!Configuring hdfs-site.xml file!!".center(150))
        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
        os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
        os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
        os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
        os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
        os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
        os.system('echo -e "</property>" >> /root/hdfs-site.xml')
        os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
        os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
        os.system('rm -rf /root/hdfs-site.xml')
        pyttsx3.speak("Please enter name node ip address")
        niq = input("Enter Name Node IP :")
        pyttsx3.speak("Configuring core-site.xml file")
        print("!!Configuring core-site.xml file!!".center(150))
        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
        os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
        os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
        os.system('echo -e "\n<property>" >> /root/core-site.xml')
        os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
        os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
        os.system('echo -e "</property>" >> /root/core-site.xml')
        os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
        os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
        os.system('rm -rf /root/core-site.xml')
        print("\n--------------------------------------------------------------".center(150))
        pyttsx3.speak("starting Hadoop Data Node Services")
        print("\n-----> Starting Hadoop Data Node Services <-----".center(150))
        os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
        os.system('ssh {} jps'.format(dip))
        print("\n--------------------------------------------------------------".center(150))
        print("\n-----> Showing Hadoop Cluster Report <-----".center(150))
        pyttsx3.speak("Showing Hadoop Cluster Report")
        os.system('ssh {} hadoop dfsadmin -report'.format(dip))
      elif ("4" in a):
        pyttsx3.speak("Configuring Client node, please enter name node ip address")
        yu = input("Enter Name Node IP : ")
        print("!!Configuring core-site.xml file!!".center(150))
        pyttsx3.speak("Please enter client's IP address")
        ip = input("Enter Client IP : ")
        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
        os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
        os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
        os.system('echo -e "\n<property>" >> /root/core-site.xml')
        os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
        os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(yu))
        os.system('echo -e "</property>" >> /root/core-site.xml')
        os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
        os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
        pyttsx3.speak("Hadoop Client Successfully Configured")
        print("-----> Hadoop Client Successfully Configured <-----".center(150))
      elif ("5" in a):
        pyttsx3.speak("To upload data to Hadoop Cluster")
        x = input("Enter Client IP : ")
        y = input("Enter The Name of File You want to upload on Hadoop Cluster : ")
        os.system('ssh {} hadoop fs -put {} /'.format(x , y))
        print("!!File Sucessfully Uploaded!!".center(150))
        os.system('ssh {} hadoop fs -ls /'.format(x))
      elif ("6" in a):
        pyttsx3.speak("To stop the name node")
        os.system('hadoop-daemon.sh stop namenode')
        os.system('jps')
      elif ("7" in a):
        pyttsx3.speak("To stop the data node")
        s = input("Enter Data Node IP : ")
        os.system('ssh {} hadoop-daemon.sh stop datanode'.format(s))
        os.system('ssh {} jps'.format(s))
       
      elif ("8" in a) or ("exit" in a):
        pyttsx3.speak("Closing Hadoop cluster menu bar")
        print("-----> Closing Hadoop Cluster Menu Bar <-----\n".center(150))
        break
      else: 
        pyttsx3.speak("This is invalid")
        print("This is invalid")
    
  elif ("3" in p):
    pyttsx3.speak("Welcome to Docker Automation menu bar")
    print("-----> DOCKER AUTOMATION MENU BAR <-----".center(150))
    print(" Press 1: To start Docker services \n Press 2: To check the status of Docker services \n Press 3: To launch a webserver on the top of docker container \n Press 4: Start/Stop the container \n Press 5: To see Docker images \n Press 6: To delete Docker images \n Press 7: To Exit")

    while True:
      print()
      a = input("Enter your choice: ")
      if ("1" in a):
        pyttsx3.speak("Starting docker services")
        os.system('systemctl start docker')
      elif ("2" in a):
        pyttsx3.speak("Checking the status of the docker services")
        os.system('systemctl status docker')
      elif ("3" in a):
        pyttsx3.speak("Launching webserver on the top of the docker container")
        y = input("Enter the Image name :")
        x = input("Name to the Container :")
        os.system('docker create -it -p 9091:80 --name {} {}'.format(x , y))
        os.system('docker start {}'.format(x))
        os.system('docker ps')
        os.system('docker exec -it {} yum install httpd -y'.format(x))
        os.system('sudo docker cp /root/home.html {}:/var/www/html/'.format(x))
        print("--------------------------------------------------------------")
        print("Checking the Status of Webserver Services .....")
        os.system('docker exec -it {} /usr/sbin/httpd'.format(x))
        os.system('docker exec -it {} /usr/sbin/httpd'.format(x))
      elif ("4" in a):
        print()
        z = input(" What you want to do?(start/stop): ")
        if ("start" in z):
          pyttsx3.speak("Name of the container that you want to start")
          v = input("Enter container name: ")
          os.system('docker start {}'.format(v))
        elif ("stop" in z):
          pyttsx3.speak("Name of the container that you want to stop")
          v = input("Enter container name: ")
          os.system('docker stop {}'.format(v))
        else:
          pyttsx3.speak("this is invalid")
          print("This is Invalid")
      elif ("5" in a):
        pyttsx3.speak("These are the docker images")
        os.system('docker images')
      elif ("6" in a):
        pyttsx3.speak("Which image you want to delete?")
        n = input("Enter Image Name: ")
        os.system('docker rmi {}'.format(n))
        os.system('docker images')
      elif ("7" in a):
        pyttsx3.speak("Closing the docker automation menu bar")
        break
      else:
        pyttsx3.speak("This is invalid")
        print("This is invalid") 
  elif ("4" in p):
    pyttsx3.speak("Welcome to LVM Automation Menu Bar") 
    print(" Press 1: Create LVM \n Press 2: Extend the size of the LVM \n Press 3: To Exit")  
    while True:
      print()
      a = input("Enter your choice: ")
      if ("1" in a):
        print(" Press 1: Create PV \n Press 2: Display PV \n Press 3: Create VG \n Press 4: Display VG \n Press 5: Create LV (Creating Partition) \n Press 6: Display LV \n Press 7: Format the Partition \n Press 8: Mount the Partition \n Press 9: To Exit")
        while True:
          print()
          u = input("Enter your choice: ")
          if ("1" in u): 
            os.system("pvcreate /dev/sdc")
          elif ("2" in u):
            os.system("pvdisplay /dev/sdc")
          elif ("3" in u):     
            os.system("vgcreate iiecvg /dev/sdc /dec/sdd")
          elif ("4" in u):  
            os.system("vgdisplay iiecvg")
          elif ("5" in u):  
            print("Starting STEP 1: Partition")
            os.system("lvcreate --size 30G --name mylv1 iiecvg")
          elif ("6" in u):  
            os.system("lvdisplay /iiecvg/mylv1")
            os.system("lvdisplay")
          elif ("7" in u):
            os.system("mkfs.ext4 /dev/iiecvg/mylv1")
          elif ("8" in u):
            os.system("mkdir /l1")
            os.system("mount /dev/iiecvg/mylv1")
          elif ("9" in u) or ("exit" in u):
            print("Exit")   
            break
          else:
            print("This option is invalid")
      elif ("2" in a):
        print("Extending the size of the LVM")
        os.system("lvextend --size +5G /dev/iiecvg/mylv1")
        os.system("resize2fs /dev/iiecvg/mylv1")   
      elif ("3" in a) or ("exit" in a):
        print("Closing LVM Automation Menu Bar")	
        break
      else:
        print("This option is invalid") 
  elif ("5" in p) or ("exit" in p):
    pyttsx3.speak("Always happy to help you. Have a nice day!.")
    break
  else: 
    pyttsx3.speak("Please try something else")

  