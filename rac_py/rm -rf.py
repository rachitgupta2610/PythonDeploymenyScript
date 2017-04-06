import os
JBOSS_4_DEPLOY="/home/stpl/servers/jboss-4.2.2.GA_new/server/default/deploy"
OldWars=os.listdir(JBOSS_4_DEPLOY)
for DeleteWar in OldWars:
    if DeleteWar.endswith(".war"):
        print DeleteWar
        RemoveWar = "rm -rf " "%s""/""%s" %(JBOSS_4_DEPLOY,DeleteWar)
        print RemoveWar
        RemoveWarCmd=os.system(RemoveWar)
        if RemoveWarCmd == 0:
            print "Old War Removed"
        else: print "war not removed"