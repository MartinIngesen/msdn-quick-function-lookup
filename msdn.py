import requests
import xml.etree.ElementTree as ET
import sys

def usage():
    print "Example usage: "
    print "\tpython msdn.py <function name>"
    print "\tpython msdn.py [-h|--h|-help|--help]"

if len(sys.argv) != 2:
    print "Error: Incorrect number of arguments."
    usage()
    sys.exit()

arg = sys.argv[1]

help = ['-h', '--h', '--help', '-help']

if arg in help:
    usage()
    sys.exit()

get = requests.get('https://social.msdn.microsoft.com/search/en-US/feed?query=' + arg + '%20function&format=RSS&theme=windows')

xml = get.text
root = ET.fromstring(xml.encode('utf-8'))
item = root.find('channel').find('item')

print item.find('title').text
print "======================"
print item.find('description').text
print "======================"
print item.find('link').text
