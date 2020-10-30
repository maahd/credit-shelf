// https://stackoverflow.com/questions/50977913/google-maps-shows-for-development-purposes-only
// Initialize and add the map
function initMap() {
  // The location of Uluru
  const ny = { lat: 40.7128, lng: -74.0060 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: ny,
  });
  // Crash location of cyclists
  var crashes = [
    [40.78617500, -73.94570000],
    [40.71515700, -74.00212000],
    [40.77031300, -73.99141000],
    [40.71153600, -73.98675000]
  ]
  var marker, crash;
  for (let i = 0; i < crashes.length; i++) {
    crash = { lat: crashes[i][0], lng: crashes[i][1] };
    marker = new google.maps.Marker({
      position: crash,
      map: map,
    });
  }
}

function boroughChanged() {
  var x = document.getElementById("boroughs").value;
  console.log(x);
}
