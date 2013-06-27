# Sinatra Sprack Benchmarking Test

This is the Sinatra Sprack portion of a [benchmarking test suite](../) comparing a variety of web development platforms.

Sprack is a Rack Handler based on scala, akka, and spray.

### JSON Encoding Test
* [JSON test source](hello_world.rb)

### Data-Store/Database Mapping Test

* [Database test source](hello_world.rb)

## Infrastructure Software Versions
The tests were run with:
* [JRuby 1.7.4](http://jruby.org/)
* [Sinatra 1.3.4](http://www.sinatrarb.com/)
* [MySQL 5.5.29](https://dev.mysql.com/)

## References
* https://github.com/sclasen/sprack

## Test URLs

### JSON Encoding Test

localhost:8080/json

localhost:8080/sinatra/db?queries=5
