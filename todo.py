#First thing to do is inspect the XML properly - you have the timecodes, so the index might be irrelvent.

#Second thing to do, is to look at


#I need two things, I need a test XML file, and I need a test translation file. one of which I can get from other subtitle repos, and the other I can get general.


#So, we should go though the timings in the source file, and fir each timeing, pull out the xml line in the thing.
for subitem in sources:

  replacement_line=line[40:]+subitem.text+"<\p>

  xmlfile=xmlfile.replace(line,replacementline).



