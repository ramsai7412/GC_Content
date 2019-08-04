import os
import sys
in_file = sys.argv[1]
file_name = os.path.basename(in_file).split('.')[0]
file_path = os.path.abspath(os.path.dirname(in_file))
try:
	with open(in_file, "r") as fa:
	    lines=fa.read().split('\n')
	    header = lines[0][1:]
	    seq = lines[1:]
	    seq = ''.join(seq).upper()
	    print ("\nInput Sequence Id\t:\t"+header)
	    Acnt = seq.count("A")
	    Tcnt = seq.count("T")
	    Gcnt = seq.count("G")
	    Ccnt = seq.count("C")
	    gc_content = round(float(Gcnt+Ccnt)/float(Acnt+Tcnt+Gcnt+Ccnt)*100,2)
	    result = str(gc_content)+"%"
	print ("\nGC content for the given DNA sequence is "+str(gc_content)+"%\n")
	out_file=open(file_path+"/"+file_name+"_GC_content.txt", "w")
	out_file.write("Sequence ID\t:\t"+header+"\n\nCounts of A\t:\t"+str(Acnt)+"\n\nCounts of T\t:\t"+str(Tcnt)+"\n\nCounts of G\t:\t"+str(Gcnt)+"\n\nCounts of C\t:\t"+str(Ccnt)+"\n\nGC Content\t:\t"+result)
	out_file.close()
except:
	sys.exit("Opps..either file is not present or file format is not correct")