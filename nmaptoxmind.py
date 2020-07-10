#!/usr/bin/python3

import xmind
import nmap3
import sys
dirstring = sys.argv[1]
workbook = xmind.load( dirstring)  # Requires '.xmind' extension
nampSheet = workbook.createSheet()
nampSheet.setTitle("Nmap")
nmapSheetRoot = nampSheet.getRootTopic()
nmapSheetRoot.setTitle("Nmap")

# EX: [443](Ubuntu) http - ngnix 1.14.0
def makeNmapString(nmapScan):
    try:
        portstate = nmapScan["state"]
    except:
        portstate= ""
    try:
        port = nmapScan["port"]
    except:
        port= ""

    try:
        extrainfo = nmapScan["service"]["extrainfo"]
    except:
        extrainfo= ""

    try:
        name = nmapScan["service"]["name"]
    except:
        name=""

    try:
        product = nmapScan["service"]["product"]
    except:
        product= ""

    try:
        version = nmapScan["service"]["version"]
    except:
        version=""

    NmapScanString = "[{}][{}]({}) {} - {}  {}"
    FormattedNmapString = NmapScanString.format(portstate,port, extrainfo, name, product, version)
    return FormattedNmapString

nmap = nmap3.Nmap()
NmapResult = nmap.nmap_version_detection(sys.argv[2])

for NmapPiece in NmapResult:
    NmapString = makeNmapString(NmapPiece)
    topicElement = nmapSheetRoot.addSubTopic()
    topicElement.setTopicHyperlink(nmapSheetRoot.getID())
    topicElement.setTitle(NmapString)
xmind.save(workbook,dirstring) 