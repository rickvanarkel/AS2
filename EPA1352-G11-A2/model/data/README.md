# Data description for Model Generation in MESA

Created by: EPA1352 Group 11*

|      Name      | Student Number |
|:--------------:|:---------------|
| Rick van Arkel | 4974859        | 
|  Laura Drost   | 5066034        |
|   Inge Faber   | 4457617        |
| Daan de Jager  | 4702972        |
| Susan Ruinaard | 4650441        |

## Introduction

This README gives a short overview to the data used in the model. The original data is provided by the course EPA1352 Advanced Simulation course Assignment 2.
The file [preparing_data.py] takes an `csv` and 'xlxs' input data file and specifies the infrastructure model components to be generated. The data format used is described here. 

## Format

| Column    | Description   |
|----------:|:--------------|
| road      | On which road does the component belong to |
| id        | **Unique ID** of the component |
| model_type| Type (i.e. class) of the model component to be generated|
| name      | Name of the object |
| lat       | Latitude in Decimal Degrees|
| lon       | Longitude in Decimal Degrees |
| length    | Length of the object in meters |

The column `road` is used by the model generation to classify model components by roads, i.e., on which road does a component belong to. The model generation assumes that the infrastructure model components of the same road is ordered sequentially. This means component `100000` is connected to component `100001`, that is connected to component `100002`, that is connected to component `100003`, etc., all of which are on road `N1`. 

The column `model_type` is used by the model generation to identify which class of components to be generated. The `model_type` labels used in this column must be consistent with the labels in the `generate_model` routine. 

The rest of the information is used to instantiate the components (objects). 
  

(*The basis are constructed by the course author)