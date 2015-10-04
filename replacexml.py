import csv


def generate_lines(filename):
        """generator for subtitle lines in a file"""
        with open(filename, 'rb') as subs_file:
                reader = csv.reader(subs_file, skipinitialspace=True)
                headers = next(reader, None)[3:]
                lines = filter(None, reader)
                for line in lines:
                        yield line


# First thing to do is inspect the XML properly - you have the timecodes,
# so the index might be irrelvent.

# Second thing to do, is to look at


# I need two things, I need a test XML file, and I need a test translation
# file. one of which I can get from other subtitle repos, and the other I
# can get general.


# So, we should go though the timings in the source file, and fir each
# timeing, pull out the xml line in the thing.

def itteratate_over_xml(filename):
        f = open(filename)
        line_generator = generate_lines("inputsubtitlefile.test")
        for line in f:
                index = line.find("begin")
                if index > 0:
                        # Then this is a line containing a subtitle, let's
                        # assert that it really is
                        start_index = line[index+7:index+7+11]
                        sub_line = (next(line_generator))
                        sub_index = sub_line[0].replace(",", ".")[:-1]
                        assert start_index == sub_index,\
                            "Start times are different for xml and srt %s and %s" % (
                                start_index, sub_index)
                        index = line.find("end")
                        replaceMe = line[index+18:]
                        line = line.replace(replaceMe, sub_line[3].replace("\n","")+"</p>\n")
                print line,
        f.close()

itteratate_over_xml('target.xml')
# for subitem in sources:
#
#  replacement_line=line[40:]+subitem.text+"<\p>
#
#  xmlfile=xmlfile.replace(line,replacementline).
