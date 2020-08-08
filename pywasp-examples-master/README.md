# **pywasp examples**

This repository contains [pywasp](https://gitlab-internal.windenergy.dtu.dk/WAsP/WAsP/pywasp) examples provided as [jupyter](https://jupyter.org/) notebooks. The repository is a submodule of [pywasp](https://gitlab-internal.windenergy.dtu.dk/WAsP/WAsP/pywasp). The purpose of the examples are to familiarize users with [pywasp](https://gitlab-internal.windenergy.dtu.dk/WAsP/WAsP/pywasp) and enable them to quickly build there own workflows with [pywasp](https://gitlab-internal.windenergy.dtu.dk/WAsP/WAsP/pywasp). The examples cover typical usage of [pywasp](https://gitlab-internal.windenergy.dtu.dk/WAsP/WAsP/pywasp) and they are provided as 4 tutorials.


## **Tutorial 1: mapping of wind resources**
This [tutorial](./tutorial_1) introduces the basic functionalities of `pywasp`, such as:

  - Opening and inspecting wind climate files
  - Opening and inspecting terrain data (i.e., subset of [SRTM](https://www2.jpl.nasa.gov/srtm/) dataset)
  - Opening and inspecting roughness data (i.e., subset of [CORINE](https://land.copernicus.eu/pan-european/corine-land-cover) Land Cover dataset)
  - Calculating and inspecting site effects from the terrain and roughness data
  - Creating a generalized wind climate from the observed wind climate
  - Creating a resource map by downscaling the generalized wind climate

The users will be also introduce to [xarray](http://xarray.pydata.org), a powerful high level package for labelled multi-dimensional arrays.

## **Tutorial 2: analysis of roughness change model response**
One of the aims of this [tutorial](./tutorial_2) is to show how straightforward is to configure and run series of simulations using `pywasp`. For that purpose, the tutorial explores the sensitivity of WAsP roughness change induced speedups to various parameters of a single roughness change line. The users will learn how to:
 - Create a single roughness change line
 - Create a series of test cases for the analysis of roughness change model response of a single roughness change line
 - Execute the series of test cases
 - Present the results of the test cases

In this tutorial we will touch upon [pandas](https://pandas.pydata.org/), python's main package for manipulation of tabular data. [pandas](https://pandas.pydata.org/) will be used to create the test case series.

## **Tutorial 3: comparison of predicted and measured power density**
In this [tutorial](./tutorial_3) users will get to know how to:
  - Work with tab files from two different met masts
  - Work with roughness maps ([CORINE](https://land.copernicus.eu/pan-european/corine-land-cover) Land Cover dataset)
  - Provide more elaborate roughness description using a lookup table
  - Work with terrain data from lidar scans ([Geodatastyrelsen](https://eng.gst.dk/) dataset)
  - Create a generalized wind climate from the observed wind climate
  - Downscale generalized wind climate
  - Compare downscaled and measured power density

## **Tutorial 4: wind farm AEP calculation**
This [tutorial](./tutorial_4) represnts a `pywasp` adaptation of the classical `WAsP` step-by-step example from the `WAsP` help. In the tutorial users will work through a complete wind turbine siting operation, starting with some measured wind data and ending up with a prediction of the power yield from erecting a turbine at a specific site. Similar to the [first tutorial](./tutorial_1), the users will get to know how to :
 - Load and work with observed wind climate (i.e., met mast data from a Portuguese site)
 - Load vector map file which contains both the roughness and terrain data
 - Load power curve of a wind turbine
 - Calculate and inspect site effects from the terrain and roughness data
 - Create a generalized wind climate from the observed wind climate
 - Downscale the generalized wind climate to the wind turbine locations
 - Calculate AEP of a single and multiple wind turbines


## **Tutorial 5: importing objects from wwh files**
In this [tutorial](./tutorial_5) users will get to know how to:
 - Import different objects from `wwh` (WAsP WorkSpace file)
 - Use the imported objects to generate predicted wind climate over an uniform grid
 - Export various `pywasp` `xarray` datasets as `NetCDF` files

