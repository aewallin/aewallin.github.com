
# https://help.launchpad.net/API/launchpadlib
import sys
from launchpadlib.launchpad import Launchpad

def get_archive_data(archive):
    data=[]
    data.append("Package Name")
    data.append("Version")
    data.append("Downloads")
    for individualarchive in archive.getPublishedBinaries():
        x = individualarchive.getDownloadCount()
        if x > 0:
            data.append(individualarchive.binary_package_name)
            data.append(individualarchive.binary_package_version)
            data.append(str(individualarchive.getDownloadCount()))
            #print individualarchive.binary_package_name + "\t" + individualarchive.binary_package_version + "\t" + str(individualarchive.getDownloadCount())
    return data

def get_build_data(archive):
    bld = archive.getBuildCounters()
    data = []
    for k in bld.viewkeys():
        data.append(k)
        data.append(str( bld[k] ))
    return data
    
def print_table(data, row_length):
    print '<table border="1">'
    counter = 0
    for element in data:
        if counter % row_length == 0:
            print '<tr>'
        print '<td>%s</td>' % element
        counter += 1
        if counter % row_length == 0:
            print '</tr>'
    if counter % row_length != 0:
        for i in range(0, row_length - counter % row_length):
            print '<td>&nbsp;</td>'
        print '</tr>'
    print '</table>'
    
if __name__ == "__main__":  
    PPAOWNER = "anders-e-e-wallin" #sys.argv[1]
    PPA = "cam" # sys.argv[2]
    #dist = "oneiric"
    #arch = "amd64"


    cachedir = "~/.launchpadlib/cache/"
    lp_ = Launchpad.login_anonymously('ppastats', 'edge', cachedir, version='devel')
    owner = lp_.people[PPAOWNER]
    archive = owner.getPPAByName(name=PPA)
    
    print "<HTML>"
    print "<H1>PPA Statistics</H1>"
    print "<H2>PPA</H2>"
    ppa_data = ["Owner", PPAOWNER, "PPA", PPA]
    print_table(ppa_data,2)
    
    bld_data = get_build_data(archive)
    #print bld_cnt
    print "<H2>Build counts</H2>"
    print_table(bld_data,2)
    #published = archive.getPublishedBinaries()
    #print len(published)," published binaries."
    #print published
    data = get_archive_data(archive)
    print "<H2>Download counts</H2>"
    print_table(data,3)
    print "</HTML>"
