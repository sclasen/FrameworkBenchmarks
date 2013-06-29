require "sinatra"
require "jrjackson"

set :logging, false


get '/json' do
  [200, {'Content-Type' => 'application/json'}, JrJackson::Json.dump({:message => 'Hello World!'})]
end

