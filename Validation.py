#!usr/bin/python
# coding: utf-8
import sys
import subprocess
import os
import datetime

class GeneClass(object):
    """A class for holding gene objects and methods"""
    def __init__(self,name):
        self.name = name
    
    def C2Picard(self,intervalfile):
        cmd = "grep -w %s %s" % (self.name, intervalfile)
        proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell =True)
        (interval, err) = proc.communicate()
        return interval
        

    def C2Bed(self,bedfile):
        cmd = "grep -w %s %s" % (self.name, bedfile)
        proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell =True)
        (interval, err) = proc.communicate()
        return interval


def shell(cmd): #Count the number of exons and regions in picard file
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell =True)
    (stat, err) = proc.communicate()
    return stat

def list_dup(l):
    return list(set([x for x in l if l.count(x) > 1]))




#Importing List of Good Genes
good_genes = open("", "r")

#Creating List for Genes
good_genes_list = []

#Putting Genes into a list
for gene in good_genes:
     good_genes_list.append(gene.strip())

#Closing File
good_genes.close()


#Opening Input Gene list
filename = sys.argv[1] #Argument right after pythonscript.py
input_genes = open(filename,"r")

#Creating list
input_genes_list = []

#Putting input genes into a list
for gene in input_genes:
     input_genes_list.append(gene.strip())

#Closing File
input_genes.close() 


#Filtering gene input list to sort bad genes from good genes
good_input = []
bad_input = []
for gene in input_genes_list:
    if gene in good_genes_list:
        good_input.append(gene)
    else:
        bad_input.append(gene)

good_gene_count = len(good_input)

bad_gene_count = len(bad_input)

intervalfinal = """@HD	VN:1.4	SO:unsorted
@SQ	SN:chr1	LN:249250621	UR:file:/vg01/vol1/hg19/hg19.fa	M5:1b22b98cdeb4a9304cb5d48026a85128
@SQ	SN:chr2	LN:243199373	UR:file:/vg01/vol1/hg19/hg19.fa	M5:a0d9851da00400dec1098a9255ac712e
@SQ	SN:chr3	LN:198022430	UR:file:/vg01/vol1/hg19/hg19.fa	M5:641e4338fa8d52a5b781bd2a2c08d3c3
@SQ	SN:chr4	LN:191154276	UR:file:/vg01/vol1/hg19/hg19.fa	M5:23dccd106897542ad87d2765d28a19a1
@SQ	SN:chr5	LN:180915260	UR:file:/vg01/vol1/hg19/hg19.fa	M5:0740173db9ffd264d728f32784845cd7
@SQ	SN:chr6	LN:171115067	UR:file:/vg01/vol1/hg19/hg19.fa	M5:1d3a93a248d92a729ee764823acbbc6b
@SQ	SN:chr7	LN:159138663	UR:file:/vg01/vol1/hg19/hg19.fa	M5:618366e953d6aaad97dbe4777c29375e
@SQ	SN:chr8	LN:146364022	UR:file:/vg01/vol1/hg19/hg19.fa	M5:96f514a9929e410c6651697bded59aec
@SQ	SN:chr9	LN:141213431	UR:file:/vg01/vol1/hg19/hg19.fa	M5:3e273117f15e0a400f01055d9f393768
@SQ	SN:chr10	LN:135534747	UR:file:/vg01/vol1/hg19/hg19.fa	M5:988c28e000e84c26d552359af1ea2e1d
@SQ	SN:chr11	LN:135006516	UR:file:/vg01/vol1/hg19/hg19.fa	M5:98c59049a2df285c76ffb1c6db8f8b96
@SQ	SN:chr12	LN:133851895	UR:file:/vg01/vol1/hg19/hg19.fa	M5:51851ac0e1a115847ad36449b0015864
@SQ	SN:chr13	LN:115169878	UR:file:/vg01/vol1/hg19/hg19.fa	M5:283f8d7892baa81b510a015719ca7b0b
@SQ	SN:chr14	LN:107349540	UR:file:/vg01/vol1/hg19/hg19.fa	M5:98f3cae32b2a2e9524bc19813927542e
@SQ	SN:chr15	LN:102531392	UR:file:/vg01/vol1/hg19/hg19.fa	M5:e5645a794a8238215b2cd77acb95a078
@SQ	SN:chr16	LN:90354753	UR:file:/vg01/vol1/hg19/hg19.fa	M5:fc9b1a7b42b97a864f56b348b06095e6
@SQ	SN:chr17	LN:81195210	UR:file:/vg01/vol1/hg19/hg19.fa	M5:351f64d4f4f9ddd45b35336ad97aa6de
@SQ	SN:chr18	LN:78077248	UR:file:/vg01/vol1/hg19/hg19.fa	M5:b15d4b2d29dde9d3e4f93d1d0f2cbc9c
@SQ	SN:chr19	LN:59128983	UR:file:/vg01/vol1/hg19/hg19.fa	M5:1aacd71f30db8e561810913e0b72636d
@SQ	SN:chr20	LN:63025520	UR:file:/vg01/vol1/hg19/hg19.fa	M5:0dec9660ec1efaaf33281c0d5ea2560f
@SQ	SN:chr21	LN:48129895	UR:file:/vg01/vol1/hg19/hg19.fa	M5:2979a6085bfe28e3ad6f552f361ed74d
@SQ	SN:chr22	LN:51304566	UR:file:/vg01/vol1/hg19/hg19.fa	M5:a718acaa6135fdca8357d5bfe94211dd
@SQ	SN:chrX	LN:155270560	UR:file:/vg01/vol1/hg19/hg19.fa	M5:7e0e2e580297b7764e31dbc80c2540dd
@SQ	SN:chrY	LN:59373566	UR:file:/vg01/vol1/hg19/hg19.fa	M5:1e86411d73e6f00a10590f976be01623\n"""


bedfinal = ""
gene_list = ""
#Creating Picard and Bed Files from genes
for gene in good_input:
    gene_list+= gene + "\n"
    temp = GeneClass(gene)
    temp_interval = temp.C2Picard("")
    temp_bed = temp.C2Bed("")
    intervalfinal += temp_interval
    bedfinal += temp_bed

print "This is writing the Picard Interval and Bed Regions files to the same directory as the input genes." 
#Writing the files to the place where the input genes are...complicated string editing going on here
panel_name = sys.argv[1][len(os.path.dirname(sys.argv[1])):]  #Getting rid of the directory from the file
panel_head, sep, ext = panel_name.partition('.')  #Splitting the filename from the extension
path_input = os.path.abspath(os.path.dirname(sys.argv[1])) + panel_head  #Creating a new path to created folder
if not os.path.exists(path_input): os.makedirs(path_input)
file_interval = path_input + panel_head + "-Interval" #Making the interval file name
file_bed = path_input + panel_head + ".Bed" #Making the bed file name
file_genes = path_input + panel_head + ".genes" #Making the bed file name
bed_file_name = panel_head[1:] + ".Bed" 

#creating Interval file in directory
file_interval_write = open(file_interval, "w")
file_interval_write.write(intervalfinal)
file_interval_write.close()

#Creating Bed File in directory
file_bed_write = open(file_bed, "w")
file_bed_write.write(bedfinal)
file_bed_write.close()

#Creating Gene List File in directory
file_gene_write = open(file_genes, "w")
file_gene_write.write(gene_list)
file_gene_write.close()

#Count Exons and Regions 
cmd = "cat %s | wc -l" % (file_bed)
count_exons = shell(cmd)





#List of Input Bams
input_bams = ('/vg05/vol2/data/ExomeValidation/v2/1300011-Exome-Analysis/1300011_sorted.bam', '/vg05/vol2/data/ExomeValidation/v2/1300012-Exome-Analysis/1300012_sorted.bam', '/vg05/vol2/data/ExomeValidation/v2/1300013-Exome-Analysis/1300013_sorted.bam', '/vg05/vol2/data/ExomeValidation/v2/1300014-Exome-Analysis/1300014_sorted.bam','/vg05/vol2/data/ExomeValidation/v2/1300019-Exome-Analysis/1300019_sorted.bam','/vg05/vol2/data/ExomeValidation/v2/1300060-TruS-Exome-Analysis/1300060-TruS_sorted.bam','/vg05/vol2/data/ExomeValidation/v2/02062013_A3BPF_Patient1_TSEX-Exome-Analysis/02062013_A3BPF_Patient1_TSEX_sorted.bam','/vg05/vol2/data/ExomeValidation/v2/02062013_A3BPF_Patient2_TSEX-Exome-Analysis/02062013_A3BPF_Patient2_TSEX_sorted.bam')

name_bams = ('1300011', '1300012', '1300013', '1300014', '1300019', '1300060', 'A3BPF_Patient1', 'A3BPF_Patient2')


output_stat_files = []

for bam, bamname in zip(input_bams, name_bams):
    cmd = "java -jar /vg01/vol1/picard-tools-1.89/CollectTargetedPcrMetrics.jar I=%s O=%s/%s_%s_picard.txt AI=%s TI=%s R='/vg01/vol1/Bioinformatic_PipeLine_Files/hg19.fa' PER_TARGET_COVERAGE=%s/%s_%s_PTC.txt" % (bam, path_input, bamname ,panel_head[1:], file_interval, file_interval, path_input, bamname, panel_head[1:])
    os.system(cmd) #-------------This executes the picard run down----------------------
    output_stat_files.append(cmd.split("="))

summary_stats_values = []
ptc_stats_values = []
low_coverage_regions = []
count_regions_file = ""

#Getting file outputs so I can extract info from picard metrics file
for count in range(0,len(output_stat_files)):
    summary_stat_file = output_stat_files[count][2][:-3]
    per_target_file = output_stat_files[count][6]
    cmd1 = "awk 'NR==8 {print $2,$5,$11,$14*100,$24,$30*100,$31*100,$32*100}' %s" % (summary_stat_file)
    summary_stats_values.append(shell(cmd1).split())
    cmd2 = "cat %s" % (per_target_file)
    ptc_stats_values.append(shell(cmd2))
    cmd3 = "awk '{if($7<20) print $1,$2,$3,$4,$5}' %s" % (per_target_file)
    regions = shell(cmd3).splitlines()
    for region in regions:
         low_coverage_regions.append(region)
    count_regions_file = per_target_file 

cmd = "cat %s | awk 'NR > 1{print 0;}' | wc -l" % (count_regions_file)
count_regions = shell(cmd)


low_coverage_regions = list_dup(low_coverage_regions)
bad_regions_count = len(low_coverage_regions)
bad_regions_ratio = str(bad_regions_count) + "/" + str(count_regions)

bad_regions_percent = (int(bad_regions_count)/float(int(count_regions)))*100

bad_regions_percent = '%.2f' % (bad_regions_percent)

good_regions_percent = float(100 - float(bad_regions_percent))

#Put the PTC Coverage files into a seperate folder
path_input_PTC = path_input + "/PerTargetCoverage"
if not os.path.exists(path_input_PTC): os.makedirs(path_input_PTC)
#Command to move all PTC files to folder
os.system("mv %s/*.txt %s " %(path_input, path_input_PTC))







table = """<table>
<tr>
<th>Specimen Name</th>
<th>Total Reads</th>
<th>Aligned Reads</th>
<th>Percent Aligned</th>
<th>Average Target Base Coverage</th>
<th>Percent Coverage at 10x</th>
<th>Percent Coverage at 20x</th>
<th>Percent Coverage at 30x</th>
</tr>
"""
avg_10 = []
avg_20 = []

#Creating table with information from sheets
for stats, bamname in zip(summary_stats_values, name_bams):
    table += "<tr>\n"
    table += "<td>"+bamname+"</td>"
    avg_10.append(stats[5])
    avg_20.append(stats[6])
    for stat in stats[1:]:
        table+= "<td>"+stat+"</td>\n"

    table+= "</tr>\n"
table += "</table>"

coverage_20 = reduce(lambda x, y: float(x) + float(y), avg_20) / len(avg_20)
coverage_10 = reduce(lambda x, y: float(x) + float(y), avg_10) / len(avg_10)

int(coverage_20)


ptc_html = """"""

for ptc, bamname in zip(ptc_stats_values, name_bams):
    ptc_html += "\n\n\n<h3>"+bamname+"</h3>\n"+ " <hr /><pre>" + ptc + "</pre><hr />"



table_genes = """<table>
<tr>
<th>Genes That Passed - %d </th>
<th>Genes That Failed - %d </th>
</tr>
""" % (good_gene_count, bad_gene_count)

if len(bad_input) is len(good_input):
     print "regular table"


elif len(bad_input) > len(good_input):
    space_range = len(bad_input) - len(good_input)
    for space in range(0,space_range):
        good_input.append(" ")

elif len(good_input) > len(bad_input):
    space_range = len(good_input) - len(bad_input)
    for space in range(0,space_range):
        bad_input.append(" ")
    
else:
    pass


for bad_gene, good_gene in zip(bad_input, good_input):
    table_genes += "<tr><td>"+good_gene+"</td><td>"+bad_gene+"</td></tr>"

table_genes += "</table>"

style = """
div.statTable, th, td {
border: 1px solid black;

}


Table {
border-collapse:collapse;
width: 100%
text-align: left;

}

th {
height: 40px;
background-color:orange;
color:white; 
}
td {
padding: 7px;
background-color:#FFFF;
}

h2 { }

body {background-color:#fdfdfd;
min-width: 960px;
padding-bottom: 20px;
height: auto;
}

#lh1, #lpre{
float: right;
}

#genes {
font-size: x-large;
font-variant: small-caps;
font-weight: bold;
}


"""

final_summary = """<?xml version=\u201d1.0\u201d encoding=\u201dUTF-8\u201d?>
<!DOCTYPE html PUBLIC \u201c-//W3C//DTD XHTML 1.1//EN\u201d
\u201chttp://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\u201d>
<html xmlns=\u201dhttp://www.w3.org/1999/xhtml\u201d xml:lang=\u201den\u201d>

<head>
<title>Panel:{0} | Exome Validation Coverage</title>
<!--  Style Starts -->
<STYLE type="text/css">
{11} <!-- Import style variable into html -->
</STYLE> <!-- End of Styling the page -->
</head> <!-- End of Header -->

"""


#Creating HTML File in directory
html_path = path_input + panel_head +"_Summary.html"
final_html = open(html_path, "w")
final_html.write(final_summary)
final_html.close()

print "Opening the html file for the panel: %s .  Look to your firefox browser as it has dispayed the summary information" % (panel_head[1:])

#Opening the Summary Sheet
#os.system("firefox %s" % html_path)


