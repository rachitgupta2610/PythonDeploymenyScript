import os
import sys
import time
#Address = "192.168.124.61"
#username = "stpl"
for arguments in sys.argv:
    print arguments
Nexus_Repo_URL='http://192.168.126.99:8087/repository/'
#Repo_name=str(sys.argv[1])
Repo_name='RMS'
print Repo_name
Group_ID="lms"
#Group_ID=str(sys.argv[2])
print Group_ID
Artifact="rms"
#Artifact=str(sys.argv[3])
print Artifact
Version="1.0.1-b_86"
#Version=str(sys.argv[4])
print Version
File_Name="rms-1.0.1-b_86.zip"
#File_Name=str(sys.argv[5])
print File_Name

Nexus_Repo_URL='http://192.168.126.99:8087/repository/'
DOWNLOAD_URL="%s%s""/""%s""/""%s""/""%s""/""%s" %(Nexus_Repo_URL,Repo_name,Group_ID,Artifact,Version,File_Name)
print DOWNLOAD_URL
JBOSS_HOME_7 = "/root/software/jboss-as-7.1.1.Final"
JBOSS_HOME_4 = "/root/rachit/jboss-4.2.2.GA"
JBOSS_BIN_7 = "/root/software/jboss-as-7.1.1.Final/bin"
JBOSS_BIN_4 = "/root/rachit/jboss-4.2.2.GA/bin"
JBOSS_7_DEPLOY="/root/software/jboss-as-7.1.1.Final/standalone/deployments"
JBOSS_4_DEPLOY="/root/rachit/jboss-4.2.2.GA/server/default/deploy"
JBOSS_USER = "root"
#------------jboss.4 Process id-----
#ssh_cmd= "ssh" " %s" "@" "%s" % (username,Address)
#print ssh_cmd
#DOWNLOAD_URL="http://192.168.126.99:8087/repository/RMS/lms/rms/1.0.1-b_11/"
DOWNLOAD_LOCATION="/root/deploy_script/"
#rms-1.0.1-b_17-dist.zip
DEPLOY_VERSION =File_Name.replace(".zip","")
print DEPLOY_VERSION
shutDown_Jboss_7=  "cd"" %s" "&& ""./jboss-cli.sh --connect :shutdown"  %JBOSS_BIN_7#shutDown Jboss-7
start_Jboss_7=  "cd"" %s""&& ""nohup ./standalone.sh -b 0.0.0.0 & >/dev/null"  %JBOSS_BIN_7#start jboss-7
shutDown_Jboss_4=  "cd" " %s""&& ""./shutdown.sh -S" %JBOSS_BIN_4 #shutDown Jboss-4
start_Jboss_4=  "cd" " %s""&& "" nohup ./run.sh -b 0.0.0.0 & >/dev/null " % JBOSS_BIN_4  #start jboss-4
cmd1 = "wget "  "%s %s" % (DOWNLOAD_LOCATION,DOWNLOAD_URL)         #DownLoad Package
print cmd1
os.system(cmd1)
print 'DOWNLOAD DONE'
cmd3 = 'unzip ' "%s" ' -d'  "%s""%s"  % (File_Name,DOWNLOAD_LOCATION,DEPLOY_VERSION)   #Unzip Package
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
warpath= "%s"'/'"%s"  % (Package_path,App)
print warpath
war = os.listdir(warpath)
WarName=war
print WarName
#os.chdir(warpath)

warlist =['DGE','rms','PMS','DrawGameWeb','SportsLottery']
for Warfile in war:
    if Warfile.endswith(".war"):
        for WarName in warlist:
            if WarName in Warfile:
                print WarName
                if WarName=='rms':
                    print "rms"
                    print_Jboss_4_PID = ("ps -ef|grep  jboss-4.2.2.GA |awk '{print $2}'")
                    PIDs = os.popen(print_Jboss_4_PID).read().split()
                    print PIDs
                    for id in PIDs:
                        KillProcess = "kill -9" " %s" % id
                        print KillProcess
                        KillProcess_status = os.system(KillProcess)
                        if KillProcess_status == 0:
                            print "process Killed"
                            print "Jboss-4 Down==========================================================="

                        else:
                            print "Error while Shutting Down Jboss"

                    time.sleep(10)
                    OldWars=os.listdir(JBOSS_4_DEPLOY)
                    for DeleteWar in OldWars:
                        if DeleteWar.endswith(".war"):
                            print DeleteWar
                            RemoveWar_Jboss_4 = "rm -rf " "%s""/""%s" %(JBOSS_4_DEPLOY,DeleteWar)
                            print RemoveWar_Jboss_4
                            RemoveWarCmd_jboss_4=os.system(RemoveWar_Jboss_4)
                            if RemoveWarCmd_jboss_4 == 0:
                                print "Old War Removed"
                            else: print "war not removed"

                    #print shutDown_Jboss_4
                    #os.system(shutDown_Jboss_4)
                    #print "Jboss-4 Down==========================================================="
                    copy_war_jboss_4 = 'cp' " %s"'/'"%s" " %s" % (warpath, Warfile, JBOSS_4_DEPLOY)
                    print copy_war_jboss_4
                    os.system(copy_war_jboss_4)
                    print "War Copied==============================================================="
                    print start_Jboss_4
                    os.system(start_Jboss_4)
                    print "JBoss-4 Started====================================================="
                    sys.exit()

                else:
                    print "LMS not found- Other Available War :"" %s" %WarName
                    print WarName
                    #print shutDown_Jboss_7
                    #os.system(shutDown_Jboss_7)
                    #print "Jboss-7 Down"
                    OldWars = os.listdir(JBOSS_7_DEPLOY)
                    for DeleteWar in OldWars:
                        if DeleteWar.endswith(".war" or ".deployed" or ".failed"):
                            print DeleteWar
                            RemoveWar_jboss_7 = "rm -rf " "%s" % DeleteWar
                            print RemoveWar_jboss_7
                            RemoveWarCmd_jboss_7 = os.system(RemoveWar_jboss_7)
                            if RemoveWarCmd_jboss_7 == 0:
                                print "Old War Removed"
                            else:
                                print "war not removed"
                    copy_war_jboss_7='cp' " %s"'/'"%s" " %s" % (warpath, Warfile, JBOSS_7_DEPLOY)
                    os.system(copy_war_jboss_7)
                    print "War Copied"
                    print copy_war_jboss_7
                    print "JBoss-7 Started"
    else:
        print "war does not exists"

sys.exit()

"""def abc ():
    abcd=os.list(JBOSS_4_DEPLOY)
    for a in abcd:
        if abcd.endswith(".deployed" or ".failed"):
            Deploy_status=a
            print Deploy_status
            if Deploy_status is None:
                abc(JBOSS_4_DEPLOY)
            else:
                return Deploy_status


    else:
        print 'app folder does not exist'

abc(JBOSS_4_DEPLOY)"""


