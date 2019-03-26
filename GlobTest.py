import cv2
import glob

#The last part of the path says to read in any file that has a dot in its name
#The two stars are wildcard indicators, so as long as there is a dot in the name, 
#it will be reads
path = "/Users/naveednaqi/Dev/SHSATDiagGrader/Images/*.*"
for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    print(a)
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
    #wait for 1 second
    k = cv2.waitKey(0)
    #destroy the window
    cv2.destroyAllWindows()