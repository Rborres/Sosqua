# SOSQUA
_**Harvest Beyond Food**_

<div style="text-align:center"> <img src="Sosqua_Logo.jpeg" width="100%"> </div>

## Table of Contents
<!--ts-->
   * [Description of the Problem](#description-of-the-problem)
   * [Solution Brief](#solution)
   * [Pilot Test](#pilot-test)
      * [Choose a Place](#choose-a-place)
      * [Sentinel and Planet Imgery](#sentinel-and-planet-imagery)
      * [Pre-Processing](#pre-processing)
      * [Mask](#mask)
      * [Processing](#processing)
      * [Results](#results)
      * [WebApp](#webapp)
   * [Future](#tests)
<!--te-->

## Description of the problem

Family farmers are core suppliers of food & nutrition. Around 60 million people work as smallholder family farmers in Latino America and the Caribbean, who produce 80% of the agriculture sector, which represents almost 40% of the sector GDP (FAO). Only in Colombia, there are 9.4 million of family farmers on the frontline keeping the food supply chain running during the COVID19 crisis. However, restrictions on movement and non-perishables preference are keeping 90% of these families from selling products. This has triggered price speculation and food losses in addition to the  9.76 million tons of food lost every year.

## Solution Brief

A way to support family farmers during and in the post-COVID crisis is by connecting them to local markets. Answering where, when and what products are going to be available and demanded in advance to starting up the supply chains. Monitoring crop status from the space by using vegetation indices allow us to track and account.

## Pilot Test

In order to contuct a concept study, a pilot test was developed for 4 farms for the last 6 months.

### Choose a Place

The criteria aspects in the selection of the place were:

- Existence of family farming: Based in official data from Rural Agricultural Planning Unit (UPRA) of Colombia: https://sipra.upra.gov.co/
- Kind of cultive: Cultives with more visual channge were prefered
- Availability of datasets for the place (Area coverage > 90%, Cloud cover < 45%)
- Closeness to cities: Closer places were prefered due to transport facilities

Given these criteria facts it was selected a zone on the edge of the Tota's Lake (Laguna de Tota) which include the municipality of Cuitiva. This zone is framed within the following coorners:

-72.9711983508027373,5.5625967687025044 : -72.9368196774082804,5.5930036243900689


### Sentinel and Planet Imagery

Both Sentinel 2A and PlanetScope Ortho Tiles imagery were used inthe pilot test.
<p align="center">
<img src="P_20200526.png" width="35%">
<br> 
PlanetScope Imagery - 26/May/2020
</p>
<p align="center">
<img src="S_20191217.png" width="35%">
<br> 
Sentinel 2A Imagery - 17/Dec/2019
</p>

### Pre-Processing
### Mask
### Processing
### Results
### WebApp







## Future

### Getting the data
The Sentinel and Planet data sets will be used as the source for data analysis. Images will be automatically sought, activated, and downloaded using either Planet Data API for Planet and Sentinel data or Aria2 only for Sentinel. As an example of this proccess a flowchart is shown below.
<p align="center">
<img src="Sosqua_General.png" width="35%">
</p>

### Pre-Processing and Processing

<p align="center">
<img src="Sosqua Pre-Processing Code.png" width="35%">             <img src="Sosqua Processing Code.png" width="35%">
</p>

### WebApp
