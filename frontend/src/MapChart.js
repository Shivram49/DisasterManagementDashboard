import React from "react";

import {
  ComposableMap,
  Geographies,
  Geography,
  Marker
} from "react-simple-maps";

const geoUrl =
  "https://raw.githubusercontent.com/deldersveld/topojson/master/world-continents.json";

const projection = geoMercator()
  .scale(100)
  .translate([800 / 2, 450 / 2])
  .center([0, 0]); // add this line to include center property


const MapChart = () => {
  return (
    <ComposableMap projection="geoRobinson">
      <Geographies geography={geoUrl}>
        {({ geographies }) => {
          console.log(geographies);
          geographies.map((geo) => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              fill="#DDD"
              stroke="#FFF"
            />
          ))
        }}
      </Geographies>
      <Marker coordinates={[-74.006, 40.7128]}>
        <circle r={8} fill="#F53" />
      </Marker>
    </ComposableMap>
  );
};

export default MapChart;
