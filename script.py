from shutil import copyfile
from sys import exit
import os

def replace_class():
    for root,dirs,files in os.walk('Dev/classes/'):
        for fileName in files:
            if fileName.endswith('.cls'):
                print("Replacing Class File ::::::: "+fileName)
                try:
                    copyfile('C:/Users/bmaheshwari/Desktop/source/tdc_erhverv_cpq_dev_r1/src/classes/'+fileName,'C:/Users/bmaheshwari/Documents/Deployment/Dev/classes/'+fileName);
                except IOError as e:
                    print("Unable to copyfile class file ::: %s" %e)
                

        print("All Class Files Replaced Successfully")


def replace_trigger():
    for root,dirs,files in os.walk('Dev/triggers/'):
        for fileName in files:
            if fileName.endswith('.trigger'):
                print("Replacing Trigger File ::::::: "+fileName)
                try:
                    copyfile('C:/Users/bmaheshwari/Desktop/source/tdc_erhverv_cpq_dev_r1/src/triggers/'+fileName,'C:/Users/bmaheshwari/Documents/Deployment/Dev/triggers/'+fileName);
                except IOError as e:
                    print("Unable to copyfile trigger file ::: %s" %e)
                    

        print("All Trigger Files Replaced Successfully")


if __name__ == '__main__':
    replace_class()
   
    replace_trigger()

