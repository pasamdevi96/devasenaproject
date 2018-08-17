from subprocess import PIPE, Popen, call, check_output, CalledProcessError
import os

class OrthoRectification:
    orthoCmd = ""
    mergeCmd = ""
    def __init__(self):
        self.orthoCmd = "otbApplicationLauncherCommandLine OrthoRectification -io.in "
        print (self.orthoCmd)

    def OrthoRectifyDEM(self, input_tiff, out_dir, dem_dir):
        epsg = "4326"
        tiff_name = self.ParseTiffName(input_tiff)
        self.orthoCmd = self.orthoCmd +"\""+ input_tiff +"\""+ " -map epsg -map.epsg.code "+ epsg + " -outputs.mode autosize -outputs.default 0 -elev.dem " + dem_dir + " -interpolator bco -interpolator.bco.radius 2 -opt.ram 128 -opt.gridspacing 4 -io.out \"" + out_dir + tiff_name+"\"" + " uint16"
        try:
            check_output(self.orthoCmd,shell = True)
            print ("Orthorectification successful")
        except CalledProcessError:
            print ("An Unexpected Error occurred in processing the file: "+tiff_name[1:])
            print ("Please check if "+tiff_name[1:]+" exists")

    def OrthoRectifyEPSG(self, input_tiff, out_dir):
        epsg = "4326"
        tiff_name = self.ParseTiffName(input_tiff)
        self.orthoCmd = self.orthoCmd +"\""+ input_tiff +"\""+ " -map epsg -map.epsg.code "+ epsg + " -outputs.mode autosize -outputs.default 0 -elev.default 0 -interpolator bco -interpolator.bco.radius 2 -opt.ram 128 -opt.gridspacing 4 -io.out \"" + out_dir + tiff_name+"\"" + " uint16"
        #s = check_output(self.orthoCmd,stdout=PIPE,stderr=PIPE,shell=True)
        #stdout, stderr = s.communicate()
        #print stdout, stderr
        try:
            check_output(self.orthoCmd,shell = True)
            print ("Orthorectification successful")
        except CalledProcessError:
            print ("An Unexpected Error occurred in processing the file: "+tiff_name[1:])
            print ("Please check if "+tiff_name[1:]+" exists")
    def ParseTiffName(self, tiff_name):
        i = tiff_name.rfind('/')
        tiff_name = tiff_name[i:]
        return (tiff_name)

    def MergeBands(self, outputdir, BandsList):
        #OrthoRectified Band output filenames are of the format "BAND#_ORTHO.tif"
        #Generate a MergeCommand for merging of bands
        os.chdir(outputdir)
        print(os.getcwd())
        self.mergeCmd = "otbApplicationLauncherCommandLine ConcatenateImages -il "
        for band in BandsList:
            self.mergeCmd = self.mergeCmd + band + " "
        self.mergeCmd = self.mergeCmd +"-out ORTHO_Output.tif" + " uint16"
        print (self.mergeCmd)
        try:
            s=check_output(self.mergeCmd,shell = True)
            print ("Merge successful")
        except:
            print(s)
            print ("An Unexpected Error occurred while merging the bands")
