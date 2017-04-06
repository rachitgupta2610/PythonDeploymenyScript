import os
import sys
import time
JBOSS4_HOME=os.environ["JBOSS4_HOME"]
print JBOSS4_HOME
JBOSS7_HOME=os.environ["JBOSS7_HOME"]
DOWNLOAD_LOCATION=os.environ["DOWNLOAD_LOCATION"]
print DOWNLOAD_LOCATION
print JBOSS7_HOME
for arguments in sys.argv:
    print arguments
Nexus_Repo_URL=str(sys.argv[1])
Repo_name=str(sys.argv[2])
print Repo_name
Group_ID=str(sys.argv[3])
print Group_ID
Artifact=str(sys.argv[4])
print Artifact
Version=str(sys.argv[5])
print Version
File_Name=str(sys.argv[6])
print File_Name
DOWNLOAD_URL="%s""/repository/""%s""/""%s""/""%s""/""%s""/""%s" %(Nexus_Repo_URL,Repo_name,Group_ID,Artifact,Version,File_Name)
print DOWNLOAD_URL
JBOSS7_BIN = "%s""/bin" %JBOSS7_HOME
JBOSS4_BIN = "%s""/bin" %JBOSS4_HOME
JBOSS7_DEPLOY="%s""/standalone/deployments" %JBOSS7_HOME
JBOSS4_DEPLOY="%s""/server/default/deploy" %JBOSS4_HOME
JBOSS_USER = "root"

DEPLOY_VERSION =File_Name.replace(".zip","")
print DEPLOY_VERSION
shutDown_Jboss_7=  "cd"" %s" "&& ""./jboss-cli.sh --connect :shutdown"  %JBOSS7_BIN            #shutDown Jboss-7
start_Jboss_7=  "cd"" %s""&& ""nohup ./standalone.sh -b 0.0.0.0 & >/dev/null"  %JBOSS7_BIN   #start jboss-7
shutDown_Jboss_4=  "cd" " %s""&& ""./shutdown.sh -S" %JBOSS4_BIN                            #shutDown Jboss-4
start_Jboss_4=  "cd" " %s""&& "" nohup ./run.sh -b 0.0.0.0 & >/dev/null " % JBOSS4_BIN       #start jboss-4
cmd1 = "wget "  "%s %s" % (DOWNLOAD_LOCATION,DOWNLOAD_URL)                                   #DownLoad Package
print cmd1
os.system(cmd1)
print 'DOWNLOAD DONE'
cmd3 = 'unzip ' "%s" ' -d'  "%s""/""%s"  % (File_Name,DOWNLOAD_LOCATION,DEPLOY_VERSION)   #Unzip Package
print cmd3
os.system(cmd3)
print "UNZIP DONE"
Package_path = "%s"'/'"%s" %(DOWNLOAD_LOCATION,DEPLOY_VERSION)
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
warlist =['DGE','rms','PMS','DrawGameWeb','sportsLottery']
for Warfile in war:
    if Warfile.endswith(".war"):
        for WarName in warlist:
            if WarName in Warfile:
                print WarName
                if WarName=='rms':
                    print_Jboss_4_PID = ("ps -ef|grep jboss-4-1 |awk '{print $2}'")
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
                    OldWars=os.listdir(JBOSS4_DEPLOY)
                    for DeleteWar in OldWars:
                        if DeleteWar.endswith(".war"):
                            print DeleteWar
                            RemoveWar_Jboss_4 = "rm -rf " "%s""/""%s" %(JBOSS4_DEPLOY,DeleteWar)
                            print RemoveWar_Jboss_4
                            RemoveWarCmd_jboss_4=os.system(RemoveWar_Jboss_4)
                            if RemoveWarCmd_jboss_4 == 0:
                                print "Old War Removed"
                            else: print "war not removed"
                    copy_war_jboss_4 = 'cp' " %s"'/'"%s" " %s" % (warpath, Warfile, JBOSS4_DEPLOY)
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
                    OldWars = os.listdir(JBOSS7_DEPLOY)
                    RemoveOldWar = "rm -rf " "%s""/""%s""*" % (JBOSS7_DEPLOY, Artifact)
                    print RemoveOldWar
                    os.system(RemoveOldWar)
                    print "Old Deployed War Removed"
                    time.sleep(10)
                    for DeleteWar in OldWars:
                        if DeleteWar.endswith (".failed") or DeleteWar.endswith (".undeployed") :
                            print DeleteWar
                            RemoveWar_jboss_7 = "rm -rf " "%s""/""%s" %(JBOSS7_DEPLOY,DeleteWar)
                            print RemoveWar_jboss_7
                            RemoveWarCmd_jboss_7 = os.system(RemoveWar_jboss_7)
                            if RemoveWarCmd_jboss_7 == 0:
                                print "Old Deployed War Removed"
                            else:
                                print "Undeployed war not removed"
                    copy_war_jboss_7='cp' " %s"'/'"%s" " %s" % (warpath, Warfile, JBOSS7_DEPLOY)
                    os.system(copy_war_jboss_7)
                    print "War Copied"
                    print copy_war_jboss_7
                    print "JBoss-7 Started"
    else:
        print "war does not exists"

sys.exit()





