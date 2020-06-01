# SOSQUA
_**Harvest Beyond Food**_

<img src="Images/Sosqua_Logo.jpeg" width="100%"> 
<br>
<p align="center">
SOSQUA is a community-supported agriculture web-app that links family farmers and local markets, based on actual food production and demand. Harvesting time per farm is estimated by monitoring growing crop cycles using optical satellite imagery-series and deriving greenness vegetation indices. Besides, a non-supervised classification is performed to identify croplands, which is validated by the farmers through the customized mobile application. This platform can be accessed by local markets to check for product availability and to contact suggested farmers, based on their location and harvesting time. Also, government institutes can access the portal to monitor harvesting dynamics and control prices.
</p>



## Table of Contents
<!--ts-->
   * [Description of the Problem](#description-of-the-problem)
   * [Solution Brief](#solution-brief)
   * [Pilot Test](#pilot-test)
      * [Choose a Place](#choose-a-place)
      * [Sentinel and Planet Imgery](#sentinel-and-planet-imagery)
      * [Pre-Processing](#pre-processing)
      * [Mask](#mask)
      * [Processing](#processing)
      * [Results](#results)
      * [WebApp](#webapp)
<!--te-->

## Description of the problem

Family farmers are core suppliers of food & nutrition. Around 60 million people work as smallholder family farmers in Latino America and the Caribbean, who produce 80% of the agriculture sector, which represents almost 40% of the sector GDP (FAO). Only in Colombia, there are 9.4 million of family farmers on the frontline keeping the food supply chain running during the COVID19 crisis. However, restrictions on movement and non-perishables preference are keeping 90% of these families from selling products. This has triggered price speculation and food losses in addition to the  9.76 million tons of food lost every year.

## Solution Brief

A way to support family farmers during and in the post-COVID crisis is by connecting them to local markets. Answering where, when and what products are going to be available and demanded in advance to starting up the supply chains. Monitoring crop status from the space by using vegetation indices allow us to track and account.

## Pilot Test

In order to contuct a concept study, a pilot test was developed for 4 farms for the last 6 months.

### Choose a Place

The criteria aspects in the selection of the place were:

- Existence of family farming: Based on official data from Rural Agricultural Planning Unit (UPRA) of Colombia: https://sipra.upra.gov.co/
- Kind of corps: Corps with more visual changes were prefered.
- Availability of datasets for the place (Area coverage > 90%, Cloud cover < 45%)
- Closeness to cities: Closer places were preferred due to transport facilities

Given these criteria facts, it was selected a zone on the edge of the Lake Tota (Laguna de Tota) which include the municipality of Cuitiva. This zone is framed within the following corners:
<p align="center">
-72.9711983508027373,5.5625967687025044 : -72.9368196774082804,5.5930036243900689
</p>

### Sentinel and Planet Imagery

Both Sentinel 2A and PlanetScope Ortho Tiles imagery were used in the pilot test.
<p align="center">
<img src="Images/P_20200526.png" width="50%">
<br> 
PlanetScope Imagery - 26/May/2020
</p>
<p align="center">
<img src="Images/S_20191217_B02.png" width="50%">
<br> 
Sentinel 2A Imagery Band 2 - 17/Dec/2019
</p>

A total of 23 datasets were downloaded.

### Pre-Processing

Each dataset was clipped using as extent the rectangle mentioned before:
<p align="center">
-72.9711983508027373,5.5625967687025044 : -72.9368196774082804,5.5930036243900689
</p>  

This operation was done using QGIS.

<p align="center">
<img src="Images/20200526_clip.png" width="35%">
<br> 
PlanetScope Imagery - 26/May/2020 - Clip
</p>

### Mask

In order to consolidate EVI averages per for the farm areas, it is necessary to create a layer specifying the farm areas. As it was mentioned before, this is a test developed for 4 farms. 
The mask was developed using the result of a supervised classification in QGIS (using the Semi-Automatic-Classification Plug-in of QGIS), a predial bounds shapefile of the zone and, finally, a shapefile of the layer "Likely for Family Agriculture"  from https://sipra.upra.gov.co/. 

<p align="center">
<img src="Images/Classification.png" width="50%">
<br> 
Classifcation using Semi-Automatic-Classification plug-in- QGIS
</p>
<p align="center">
<img src="Images/Predial.png" width="50%">
<br> 
Predial Shape file
</p>

Four farms were chosen manually. Finally was obtained a raster which contains the 4 areas. This raster can be found in Sosqua/RemoteSensing/Mask/Mask.tif
<p align="center">
<img src="Images/MaskOverMap.png" width="50%">
<br> 
Mask over the map
</p>

### Processing

A python3 code was developed to process all the datasets. This code could be found it in Sosqua/RemoteSensing/Processing(Python)/MainCodeV1.py.
The code is based in a loop In each operation is opened a dataset, calculated the EVI, Saved the EVI in a raster and finally used the Mask.tif to obtain the average of the EVI values per zone. 

<p align="center">
<img src="Images/Processing Flow Chart.png" width="50%">
<br> 
MainCodeV1.py Flowchart
</p>

### Results

The output of the MainCodeV1.py is located in: 

<p align="center">
<img src="Images/Results.png" width="50%">
<br> 
MainCodeV1.py Flowchart
</p>

### WebApp

It was designed and developed a base for the WebApp. It could be found here: https://github.com/oanlopezc/Sosqua/tree/master/maincode.sosqua



