# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
while True:
    print("""\n\n\t**************************************************************
        ################# WELCOME TO PROGRAM MENU ####################
          \n\t**************************************************************
        \n\n \t Press the following Keys to Continue :
            
               Press 1: Docker Installation 
               Press 2: Docker Compose Installation
               Press 3: To launch Wordpress Site
               Press 4: To see the docker images present in your docker.
               Press 5: To pull the image of centos:7
               Press 6: To launch the centos:7
               Press 7: To pull the image of latest version of ubuntu
               Press 8: To launch the latest version of ubuntu
               Press 9: To see the all commands in docker
               Press 0: EXIT
               
    """)
    choice= int(input("\t\tEnter  your  Choice :"))
    
    if choice == 1:
        os.system("cp dock.repo/etc/yum.repos.d/")
        os.system("yum install docker-ce --nobest")
        print("Docker is succesfully installed GO and check")
    elif choice == 2:
        os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system("chmod +x /usr/local/bin/docker-compose")
    elif choice == 3:
        os.system("docker-compose up -d")
    elif choice == 4:
        os.system("docker images")
    elif choice == 5:
        os.system("docker pull centos:7")
    elif choice == 6:
        os.system("docker run -it centos:7")
    elif choice == 7:
        os.system("docker pull ubuntu:latest")
    elif choice == 8:
        os.system("docker run -it ubuntu:latest")
    elif choice == 9:
        os.system("docker --help")
    elif choice == 0:
        exit(0)
    else:
        print("SORRY WRONG INPUT TRY AGAIN..........................................")    
        
