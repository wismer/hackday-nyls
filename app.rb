require 'sinatra'
require 'json'

class BikeApp < Sinatra::Base; end

class BikeApp
  get "/" do
    erb :index
  end

  get "/data.?:format" do
    File.read("data.json")
  end
end