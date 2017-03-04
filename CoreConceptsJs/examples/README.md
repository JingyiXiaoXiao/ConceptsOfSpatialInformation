Core Concepts of Spatial Information - JavaScript usage examples
=============================================

Abstract: Usage examples for JavaScript implementation of the core concepts.

Contents
----------------------

- `nightlight.html`: a nighttime lights case study which can be viewed as a field-based question. This question is raised
 by Matt Lowe who use night lights as a proxy to measure the level of economic activities (Lowe 2014). Instead of procedural
 steps that Lowe uses to answer his spatial question, this example shows how we address it using core concepts solution.

Core concepts solutions
-----------------------------------------

### Example 1: Night lights
#### Spatial data involved in this example:
- two global night lights maps (url_lights_F10, and url_lights_F12);
- a map of roads in mainland China(url_china_roads);
- a map of gas flares (url_china_flares).

Lowe's question can be summarised as "What was the night time luminosity for the year 1994, near roads in mainland China,
excluding gas flares, on a 0.1 degree grid?" The problem-solving process involves translating spatial questions into the
core concepts of spatial information and operations applied to them.
- Conceptualize luminosity as a **`field`**
- restrict the field **`domain`**: *inside* 0.5 degrees from China roads, *outside* gas flares
- state the field **`granularity`**: 0.1 degree

#####(1) Interpret luminosity data as fields; roads and gas flares as objects
```
lights_F10 = new CcField(url_lights_F10);
lights_F12 = new CcField(url_lights_F12);
roads = new CcObject(url_china_roads);
gas_flares = new CcObject(url_china_flares);
```
#####(2) What is the luminosity for the year 1994, within 0.5 degrees from China roads, excluding gas flares?
```
average_luminosity = lights_F10.local(lights_F12, "average");
roads.buffer(0.5, "degree").then(function(buffered_geometry){
       average_luminosity.restrictDomain(buffered_geometry,"inside");
   });
gas_flares.getGeometry().then(function(flares_geometry）{
       average_luminosity.restrictDomain(flares_geometry,"outside");
   });
```
#####(3) What is the mean luminosity in a 0.1 by 0.1 degree area?
```
average_luminosity.coarsen(0.1, 0.1);
```
References
----------
- Lowe, M. (2014). *Night lights and ArcGis: A brief guide.* Avaliable online: http://economics. mit. edu/files/8945 (accessed on 3 March 2017).