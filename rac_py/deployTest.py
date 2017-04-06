import os
import sys

Address = "192.168.124.61"
username = "root"
JBOSS_HOME_7 = "/home/stpl/software/jboss-as-7.1.1.Final"
JBOSS_HOME_4 = "/home/stpl/jboss-4.2.2"
JBOSS_BIN_7 = "/home/stpl/software/jboss-as-7.1.1.Final/bin"
JBOSS_BIN_4 = "/home/stpl/jboss-4.2.2/bin/"
JBOSS_7_DEPLOY="/home/stpl/software/jboss-as-7.1.1.Final/standalone/deployments"
JBOSS_USER = "root"
ssh_cmd= "ssh" " %s" "@" "%s" % (username,Address)
print ssh_cmd
DOWNLOAD_URL="http://192.168.126.99:8087/repository/DGE-release-local/content/repositories/DGE-Lagos/DGE/DGE-Worlf/1.0/"
DOWNLOAD_LOCATION="/root/rachit/"
DEPLOY_VERSION="DGE-Worlf-1.0"
DV=DOWNLOAD_URL.split('/',len(DOWNLOAD_URL))
DEPLOY_VERSION_NEW=(DV[len(DV)-2])
print DEPLOY_VERSION_NEW
cmd5= "%s " "'" "%s""/bin/jboss-cli.sh --connect :shutdown""'" % (ssh_cmd,JBOSS_HOME_7) #shutDown Jboss-7
cmd7="%s " "'" "%s""/bin/nohup ./standalone.sh -b 0.0.0.0""'" %(ssh_cmd,JBOSS_HOME_7)  #start jboss-7
cmd8="%s " "'" "%s""/bin/./shutdown.sh -S""'" % (ssh_cmd,JBOSS_HOME_4) #shutDown Jboss-4
cmd9="%s " "'" "%s""/bin/nohup ./run.sh -b 0.0.0.0""'" %(ssh_cmd,JBOSS_HOME_4)  #start jboss-4
cmd1 = "wget "  "%s %s%s"'.zip' % (DOWNLOAD_LOCATION,DOWNLOAD_URL,DEPLOY_VERSION)         #DownLoad Package
print cmd1
os.system(cmd1)
print 'DOWNLOAD DONE'
cmd3 = 'unzip ' "%s"'.zip' ' -d'  "%s" % (DEPLOY_VERSION,DEPLOY_VERSION)   #Unzip Package
print cmd3
os.system(cmd3)
print "UNZIP DONE"
Package_path = "%s"''"%s" %(DOWNLOAD_LOCATION,DEPLOY_VERSION)
print Package_path
files= os.listdir(Package_path)
print files

if 'app' in files:
    print 'file found'
    App='app'
else:
    print 'app folder does not exist'
    sys.exit()
    #for App in files:
    #if App in 'app':
    #break
    #print App'''

warpath= "%s"'/'"%s"  % (Package_path,App)
print warpath
war = os.listdir(warpath)
print war
#os.chdir(warpath)
#ls='ls *war'
#warlist =['DGE','LMS','PMS']
for Warfile in war:
    if Warfile.endswith(".war"):
        for WarName in warlist:
            if WarName in Warfile:
                print WarName
                if WarName=='LMS':
                    print "LMS"
                else:
                    print "LMS not found- Other Available War :"" %s" %WarName

            else: print "No War for LMS available"
            sys.exit()
    else:print "War File not available"
    sys.exit()

"""       if 'lms' in Warfile:
            print 'this is lms war'
            print Warfile

        elif 'pms' or 'DGE' or 'SLE' or 'DGWEB' in Warfile:
            print Warfile

    else:
        print "war not found"
    sys.exit()"""

"""cmd6 = "%s ""'"'scp' " %s"'/'"%s" " %s""'" % (ssh_cmd, warpath, Warfile,JBOSS_7_DEPLOY)
print cmd6
print cmd5
print cmd7"""

        # os.system(cmd5)
        # os.system(cmd6)
        #os.system(cmd7)













