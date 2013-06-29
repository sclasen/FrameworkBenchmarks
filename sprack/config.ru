require './hello_world'

#run Sinatra::Application
run lambda { |env| [200, {"Content-Type" => "application/json"}, ['{"message":"Hello World!"}']] }
