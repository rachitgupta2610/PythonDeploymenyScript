
import fileinput
import sys
HelpOpts = ('-help','-h','--help','-?','?')
FileA="DGW.properties"
VaribleA="databaseName"
SettingA="Neeraj"
def ModConfig(File, Variable, Setting):
    VarFound = False
    AlreadySet = False
    F=str(File)
    V=str(Variable)
    S=str(Setting)
    # use quotes if setting has spaces #
    if ' ' in S:
        S = '"%s"' % S
    for line in fileinput.input('%s' %F, inplace = 1):
        # process lines that look like config settings #
        if not line.lstrip(' ').startswith('#') and '=' in line:
            _infile_var = str(line.split('=')[0].rstrip(' '))
            _infile_set = str(line.split('=')[1].lstrip(' ').rstrip())
            # only change the first matching occurrence #
            if VarFound == False and _infile_var.rstrip(' ') == V:
                VarFound = True
                # don't change it if it is already set #
                if _infile_set.lstrip(' ') == S:
                    AlreadySet = True
                else:
                    line = "%s=%s\n" % (V,S)
        sys.stdout.write(line)

    # Append the variable if it wasn't found #
    if not VarFound:
        print "Variable '%s' not found.  Adding it to %s" % (V, F)
        with open('%s' %F, "a") as f:
            f.write("%s=%s\n"%(V,S))
    elif AlreadySet == True:
        print "Variable '%s' unchanged" % (V)
    else:
        print "Variable '%s' modified to '%s'" % (V,S)

    return

ModConfig(FileA,VaribleA,SettingA)