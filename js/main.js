import dataSet from "./data";

document.addEventListener( 'DOMContentLoaded', function () {
    new Splide( '#image-carousel', {
        width : '100vw',
		height: '100vh',
        pagination: false,  // Hide pagination
        arrows: false,      // Hide arrows
        autoplay: true,     // Enable autoplay
        interval: 3000,     // Set the interval (in milliseconds) for changing slides
    } ).mount();
} );

anychart.onDocumentReady(function () {});

var chart = anychart.treeMap(dataSet, "as-tree");

chart.title("Armenia");
chart.container("container");
chart.background("#27252A");
// chart.header().background("#3E3D40");
chart.normal().fill('#B46FC2');
chart.hovered().fill('#44008B', 0.8);
chart.selected().fill('#0A0068', 0.8);
chart.selected().hatchFill("forward-diagonal", '#282147', 2, 20);
chart.labels().useHtml(true);
chart.labels().format(
  "<span style='font-size: 24px; color: #fff'>{%name}</span><br>{%value}"
);

chart.draw();
