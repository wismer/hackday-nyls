require 'sinatra'
require 'json'

class BikeApp < Sinatra::Base; end

class BikeApp
  get "/" do
    data = File.read("data.json")
    """
      <html>
        <head>
          <script src=https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true></script>
          <script src=https://code.jquery.com/jquery-2.1.3.min.js></script>
          <script type='text/javascript'>
            var data = #{data}
            function initialize() {
              var myLatlng = new google.maps.LatLng(40.712784, -74.005941);

              var mapOptions = {
                zoom: 14,
                center: myLatlng
              };

              map = new google.maps.Map(
                  document.getElementById('map-canvas'),
                  mapOptions);


              var bikeLayer = new google.maps.BicyclingLayer();
              bikeLayer.setMap(map);
            }

            google.maps.event.addDomListener(window, 'load', initialize)
          </script>
        </head>
        <body>
          <div id='map-canvas'></div>
        </body>
      </html>
    """
  end



  get "/data.?:format" do
    File.read("data.json")
  end
end