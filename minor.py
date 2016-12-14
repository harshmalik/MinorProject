import sys
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse("./result.xml")
root = tree.getroot()
l= list()
print 'Enter resource type and specific query parameter'
s=raw_input().split()
resource=s[0]
query=s[1]
st='{http://hl7.org/fhir}'


r=1
for i in root.iter(st+resource):
    
    """print 'hi'"""
    for m in i.iter(st+query): 

       l=   m.get('value').split()
       
       if len(l)==1:
         
          l=l[0]
          
          try:
              l=float(l)
              plt.plot([r],[l], 'ro')
          except:print r,l    
       else:
         
          try:t= map(float,m.get('value').split()[:-1])
          except:r, l
          try:plt.plot(t)
          except: continue
    r=r+1
plt.show()
      
   
