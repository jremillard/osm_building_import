import urllib,os,zipfile,glob

base = "http://wsgw.mass.gov/data/gispub/shape/structures/structures_poly_"

def download():
    for i in range(1,352):
        i=str(i)
        n = i+".zip"
	localname = "massgis_structures/buildings_" + n
        b=base+n
        urllib.urlretrieve(b,localname)
        print "working " + i
        st=os.stat(localname)
        if st.st_size>0:
            z=zipfile.ZipFile(localname,"r")
            zl=z.namelist()
            z.extractall("massgis_structures/")
            z.close()
        os.remove(localname)
if __name__ == "__main__":
    download()
