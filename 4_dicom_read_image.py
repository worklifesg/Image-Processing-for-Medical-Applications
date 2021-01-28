#**********************************
#****** DICOM using python ********
#**********************************

'''
DICOM - Digital Imaging and Communications in Medicine

--> transmit, store, retrieve, print, process and display medical imaging information

--> It is the international standrad for medical images and related information. It defines
the format for medical images that can be exchanged with the data and quality necessary for 
clinical use.

--> Implemented for eadiology, cardiology, radiotherapy device (X-ray,CT,MRI)
--> It is recognized by international organization for standardizationas ISO 12052 standard
'''

#******************************
#***** Read dicom file data and plot image
#******************************

from pydicom import dcmread
from pydicom import dcmwrite
import matplotlib.pyplot as plt 

image = dcmread('example.dcm')

print(f"SOP Class ........... : {image.SOPClassUID}({image.SOPClassUID.name})")

name = image.PatientName

display_name = name.family_name + ',' + name.given_name

print (f"Patient's Name ...... :{display_name}")
print (f"Patient's ID ...... :{image.PatientID}")
print (f"Modality ...... :{image.Modality}")
print (f"Study Date ...... :{image.StudyDate}")
print (f"Image Size ...... :{image.Rows} x {image.Columns}")
print (f"Pixel Spacing ...... :{image.PixelSpacing}")

#to plot image from dcm
plt.imshow(image.pixel_array, cmap='gray')
plt.show()

''' OUTPUT
SOP Class ........... : 1.2.840.10008.5.1.4.1.1.2(CT Image Storage)
Patient's Name ...... :LCTSC-Test-S1-101,
Patient's ID ...... :LCTSC-Test-S1-101
Modality ...... :CT
Study Date ...... :20040303
Image Size ...... :512 x 512
Pixel Spacing ...... :[0.976562, 0.976562]
'''
