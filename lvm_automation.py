import subprocess as sp
import os
import pyfiglet

def createpv() :
    fdisk = sp.getoutput("\nfdisk -l")
    print(fdisk)
    disk = input("\nEnter Your Disk Name: ")
    oput = sp.getoutput("\npvcreate {}".format(disk))
    print(oput)

def createvg():
    p=sp.getoutput("\npvdisplay")
    print(p)
    pv1 = input("\nEnter the name of 1st pv : ")
    pv2 = input("Enter the name of 2nd pv : ")
    vgname=input("Enter the name of volume group you want to create : ")
    oput=sp.getoutput("\nvgcreate {} {} {}".format(vgname,pv1,pv2))
    print(oput)

def lvcreate():
    size=int(input("\nEnter the size of logical volume : "))
    vgname=input("Please enter  the volume group name to create LV : ")
    lv=input("Enter the name to create logical volume : ")
    oput=sp.getoutput("\nlvcreate --size {}G --name {} {}".format(size,lv,vgname))
    print(oput)
    
def format():
    op=sp.getoutput("\nlvdisplay")
    print(op)
    op1=input("Enter the lv to be formatted:")
    op2=sp.getoutput(f"\nmkfs.ext4 {op1}")
    print(op2)

def mpoint():
    dir=input("\nPlease enter the directory name to create  : ")
    op=sp.getoutput("\nfdisk -l")
    print(op)
    lv=input("Please enter the full name of  volume group that is to be mount :  ")
    oput=sp.getoutput("mkdir {}".format(dir))
    oput1=sp.getoutput("mount {} {}".format(lv,dir))
    op2=sp.getoutput("\ndf -hT")
    print(op2)


def displaypv():
    disk = input("\nEnter Your Disk Name : ")
    oput = sp.getoutput("\npvdisplay {}".format(disk))
    print(oput)

def displayvg():
    vgname=input("\nEnter the name of the volume group : ")
    oput=sp.getoutput("\nvgdisplay {}".format(vgname))
    print(oput)

def displaylv():
    dir=input("\nEnter full directory of LV ex. [vgname/lvname] : ")
    oput=sp.getoutput("\nlvdisplay {}".format(dir))
    print(oput)

def extendlv():
    op=sp.getoutput("\nlvdisplay")
    print(op)
    lv = input("\nEnter name of the lv to be resized : ")
    size=int(input("Please enter the size do you want to contribute:"))
    oput=sp.getoutput("lvextend --size +{}G {}".format(size,lv))
    oput2=sp.getoutput(f"\nresize2fs  {lv}")
    print(oput2)

    
def extendvg():
    fdisk = sp.getoutput("\nfdisk -l")
    print(fdisk)
    hd=input("\nEnter name of hard disk to add : ")
    vgname=input("Enter the name of volume group : ")
    oput=sp.getoutput("\nvgextend {} {}".format(vgname,hd))
    print(oput)

col, lines = os.get_terminal_size()

#welcome = "-----Welcome To LVM Automation-----".center(col)
#welcome = pyfiglet.figlet_format("Welcome To LVM Automation",font = "digital" )

while True :
    os.system('clear')
    os.system("figlet -r Welcome To LVM Automation  ")



    print("""\n\n\t\t\t\t\t\t1) Create a New Physical Volume 
   \t\t\t\t\t\t2) Create New Volume Group
   \t\t\t\t\t\t3) Create New Logical Volume
   \t\t\t\t\t\t4) Format Logical Volume
   \t\t\t\t\t\t5) Create A Mount Point
   \t\t\t\t\t\t6) Extend Logical Volume
   \t\t\t\t\t\t7) Extend Volume Group
   \t\t\t\t\t\t8) Show Physical Volume
   \t\t\t\t\t\t9) Show Volume Group
  \t\t\t\t\t\t10) Show Logical Volume
  \t\t\t\t\t\t11) Quit\n""")

    try:

        choice = int(input("Please Choose an Option To Continue : "))



    except ValueError:

        print("\n\nwhoops Please Enter the Choice in Number, for eg. 2 for Creating A Volume Group.. ")

        input('\nPress Enter to continue..')

        continue



    if choice == 1:

        createpv()


    elif choice == 2:

        createvg()


    elif choice == 3:

        lvcreate()

    elif choice == 4:
          
        format()


    elif choice == 5:

         mpoint()


    elif choice == 6:

         extendlv()


    elif choice == 7:

         extendvg()


    elif choice == 8:

        displaypv()


    elif choice == 9:

        displayvg()
    
    elif choice == 10:

        displaylv()
    
    elif choice == 11:

        print('THANKS FOR USING THIS SERVICE'.center(col))

        input('\n\nPress Enter To Exit..')

        os.system('clear')

        break

    input('\nPress Enter To Continue..') 

