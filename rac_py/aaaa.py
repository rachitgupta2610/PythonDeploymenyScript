import os
import sys
warpath='/home/stpl/jboss-as-7.1.1.Final/standalone/deployments'
war = os.listdir(warpath)
print war
warlist =['DGE','lms','PMS','DrawGameWeb']
for Warfile in war:

    if Warfile.endswith(".war"):
        for WarName in warlist:
            if WarName in Warfile:
                print WarName
                if WarName=='lms':
                    print "lms"
                else:
                    print "LMS not found- Other Available War :"" %s" %WarName

            else: print "No War for LMS available"

    else:print "War File not available"
sys.exit()


