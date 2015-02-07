require 'sinatra'
require 'json'

class BikeApp < Sinatra::Base; end

class BikeApp
  get "/" do
    data = File.read("data.json")
    
    erb :index, locals: { data: "<script>var data = #{data}</script>" }
  end



  get "/data.?:format" do
    File.read("data.json")
  end
end