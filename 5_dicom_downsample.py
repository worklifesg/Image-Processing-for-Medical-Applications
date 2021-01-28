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
#***** Down sample dcm file from 512 x 512 --> 64 x 64 pixels without averaging the pixels
#******************************

import pydicom
import matplotlib.pyplot as plt 

image = pydicom.dcmread('example.dcm')

plt.imshow(image.pixel_array,cmap='gray')

#pixel information

data = image.pixel_array
print('The image has {} x {} pixels'.format(data.shape[0],data.shape[1]))

image_downsample = data[::8,::8]
print('The downsampled image has {} x {} pixels'.format(image_downsample.shape[0],image_downsample.shape[1]))

# copy back the data to dcm file
image.PixelData = image_downsample.tobytes()
#updating rows and columns
image.Rows, image.Columns = image_downsample.shape

print('The information of the dataset after downsampling is \n')
print(image)

plt.imshow(image.pixel_array,cmap='gray')
plt.show()

'''
The image has 512 x 512 pixels
The downsampled image has 64 x 64 pixels
The information of the dataset after downsampling is

Dataset.file_meta -------------------------------
(0002, 0000) File Meta Information Group Length  UL: 196
(0002, 0001) File Meta Information Version       OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID         UI: CT Image Storage
(0002, 0003) Media Storage SOP Instance UID      UI: 1.3.6.1.4.1.14519.5.2.1.7014.4598.498331662686081947685043040444
(0002, 0010) Transfer Syntax UID                 UI: Explicit VR Little Endian
(0002, 0012) Implementation Class UID            UI: 1.2.40.0.13.1.1.1
(0002, 0013) Implementation Version Name         SH: 'dcm4che-1.4.35'
-------------------------------------------------
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0008) Image Type                          CS: ['DERIVED', 'SECONDARY', 'AXIAL']
(0008, 0012) Instance Creation Date              DA: '20050726'
(0008, 0013) Instance Creation Time              TM: '091154.839000'
(0008, 0016) SOP Class UID                       UI: CT Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.3.6.1.4.1.14519.5.2.1.7014.4598.498331662686081947685043040444
(0008, 0020) Study Date                          DA: '20040303'
(0008, 0030) Study Time                          TM: '144059.877000'
(0008, 0050) Accession Number                    SH: '2819497684894126'
(0008, 0060) Modality                            CS: 'CT'
(0008, 0090) Referring Physician's Name          PN: ''
(0008, 1030) Study Description                   LO: ''
(0008, 103e) Series Description                  LO: ''
(0010, 0010) Patient's Name                      PN: 'LCTSC-Test-S1-101'
(0010, 0020) Patient ID                          LO: 'LCTSC-Test-S1-101'
(0010, 0030) Patient's Birth Date                DA: ''
(0010, 0040) Patient's Sex                       CS: 'M'
(0012, 0062) Patient Identity Removed            CS: 'YES'
(0012, 0063) De-identification Method            LO: 'Per DICOM PS 3.15 AnnexE. Details in 0012,0064'
(0012, 0064)  De-identification Method Code Sequence  8 item(s) ----
   (0008, 0100) Code Value                          SH: '113100'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Basic Application Confidentiality Profile'
   ---------
   (0008, 0100) Code Value                          SH: '113101'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Clean Pixel Data Option'
   ---------
   (0008, 0100) Code Value                          SH: '113104'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Clean Structured Content Option'
   ---------
   (0008, 0100) Code Value                          SH: '113105'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Clean Descriptors Option'
   ---------
   (0008, 0100) Code Value                          SH: '113107'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Longitudinal Temporal Information Modified Dates Option'
   ---------
   (0008, 0100) Code Value                          SH: '113108'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Patient Characteristics Option'
   ---------
   (0008, 0100) Code Value                          SH: '113109'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Device Identity Option'
   ---------
   (0008, 0100) Code Value                          SH: '113111'
   (0008, 0102) Coding Scheme Designator            SH: 'DCM'
   (0008, 0104) Code Meaning                        LO: 'Retain Safe Private Option'
   ---------
(0013, 0010) Private Creator                     LO: 'CTP'
(0013, 1010) Private tag data                    LO: 'LCTSC'
(0013, 1013) Private tag data                    LO: '70144598'
(0018, 0015) Body Part Examined                  CS: 'LUNG'
(0018, 0050) Slice Thickness                     DS: "3.0"
(0018, 0060) KVP                                 DS: None
(0018, 5100) Patient Position                    CS: 'HFS'
(0020, 000d) Study Instance UID                  UI: 1.3.6.1.4.1.14519.5.2.1.7014.4598.492964872630309412859177308186
(0020, 000e) Series Instance UID                 UI: 1.3.6.1.4.1.14519.5.2.1.7014.4598.106943890850011666503487579262
(0020, 0010) Study ID                            SH: ''
(0020, 0012) Acquisition Number                  IS: None
(0020, 0013) Instance Number                     IS: "61"
(0020, 0032) Image Position (Patient)            DS: [-249.511719, -483.011719, -457.200012]
(0020, 0037) Image Orientation (Patient)         DS: [1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000]
(0020, 0052) Frame of Reference UID              UI: 1.3.6.1.4.1.14519.5.2.1.7014.4598.171234424242155356682733155977
(0020, 1040) Position Reference Indicator        LO: 'SP'
(0020, 1041) Slice Location                      DS: "-457.200012"
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 64
(0028, 0011) Columns                             US: 64
(0028, 0030) Pixel Spacing                       DS: [0.976562, 0.976562]
(0028, 0100) Bits Allocated                      US: 16
(0028, 0101) Bits Stored                         US: 16
(0028, 0102) High Bit                            US: 15
(0028, 0103) Pixel Representation                US: 1
(0028, 0303) Longitudinal Temporal Information M CS: 'MODIFIED'
(0028, 1050) Window Center                       DS: "40.0"
(0028, 1051) Window Width                        DS: "400.0"
(0028, 1052) Rescale Intercept                   DS: "-1000.0"
(0028, 1053) Rescale Slope                       DS: "1.0"
(0028, 1054) Rescale Type                        LO: 'HU'
(7fe0, 0010) Pixel Data                          OW: Array of 8192 elements
'''
