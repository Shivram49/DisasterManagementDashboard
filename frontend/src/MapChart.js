import React, { useState } from "react";
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker,
} from "react-simple-maps";

const geoUrl =
  "https://raw.githubusercontent.com/deldersveld/topojson/master/continents/north-america.json";

const markers = [
  {
    coordinates: [-74.006, 40.7128],
    message: "Hi, I'm stuck in New York. Please help me!",
  },
  {
    coordinates: [-121.955, 37.3541],
    message: "Hi, I'm in Santa Clara. Can you come over?",
  },
  {
    coordinates: [-122.3321, 47.6062],
    message: "Hi, I'm in Seattle. I need your help!",
  },
];

const MapChart = () => {
  const [tooltipContents, setTooltipContents] = useState(
    new Array(markers.length).fill("")
  );

  const handleMarkerClick = (index) => {
    setTooltipContents((prev) =>
      prev.map((content, i) => (i === index ? markers[index].message : content))
    );
  };

  const handleMarkerLeave = (index) => {
    setTooltipContents((prev) =>
      prev.map((content, i) => (i === index ? "" : content))
    );
  };

  const Tooltip = ({ content, x, y }) => (
    <foreignObject x={x + 15} y={y - 20} width={200} height={100}>
      <div
        style={{
          backgroundColor: "#fff",
          border: "1px solid #999",
          borderRadius: "5px",
          padding: "5px",
          color: "#444",
          fontSize: "14px",
        }}
      >
        {content}
      </div>
    </foreignObject>
  );

  return (
    <ComposableMap
      projection="geoAlbers"
      projectionConfig={{
        rotate: [96, 0, 0],
        scale: 400,
      }}
      zoom={1.2}
      center={[-100, 40]}
    >
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              fill="#DDD"
              stroke="#FFF"
            />
          ))
        }
      </Geographies>
      {markers.map((marker, index) => (
        <Marker
          key={index}
          coordinates={marker.coordinates}
          onClick={() => handleMarkerClick(index)}
          onMouseLeave={() => handleMarkerLeave(index)}
        >
          <circle r={8} fill="#F53" />
          {tooltipContents[index] && (
            <Tooltip content={tooltipContents[index]} x={-40} y={-60} />
          )}
        </Marker>
      ))}
    </ComposableMap>
  );
};

export default MapChart;
