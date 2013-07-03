#require './hello_world'
require 'jrjackson'

#run Sinatra::Application
#run lambda { |env| [200, {"Content-Type" => "application/json"}, ['{"message":"Hello World!"}']] }
app = lambda { |env| [200, {'Content-Type' => 'application/json'}, [JrJackson::Json.dump({:message => 'Hello World!'})]] }

run app
