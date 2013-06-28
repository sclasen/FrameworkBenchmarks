require "sinatra"
require "sinatra/json"

set :logging, false


get '/json' do
  json :message => 'Hello World!'
end

