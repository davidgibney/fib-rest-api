fib-rest-api
=============

"fib-rest-api" is a RESTful web service that accepts a number _n_ as input and returns the first _n_ Fibonacci numbers, starting from 0. As an example, given n=5, appropriate output would represent the sequence [0, 1, 1, 2, 3].
c.f. https://en.wikipedia.org/wiki/Fibonacci_number#List_of_Fibonacci_numbers

If given a negative number, it will respond with an appropriate error.

If given a large number, it will respond with an error, until we can later optimize the function.

Version
--------
Version 0.1.1


Build
------

``` bash
docker build -t "fib-rest-api:latest" .
```


Deploy
-------

``` bash
docker run -d -p 80:80 -t fib-rest-api
```


Test
-----
There is a Python unittest for the function that calculates the Fibonacci numbers.
``` bash
./test-fib-calc.py
```

Otherwise, you can build the docker image, deploy it as a container, and then send requests to the RESTful web service.

Example with curl:

```bash
fib-rest-api git:master ❯ curl http://localhost/fib\?n\=5          
[0,1,1,2,3,5]%
fib-rest-api git:master ❯ curl http://localhost/fib\?n\=25
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]%
```

You can also load an HTTP request in your web browser: `http://localhost/fib?n=10`


Dependencies
-------------
* Docker
* Python 3
* Flask


Other things
-------------

### Leonardo Pisano Bigollo

Read about Fibonacci:
* https://en.wikipedia.org/wiki/Fibonacci_number
* https://en.wikipedia.org/wiki/Fibonacci


### To Do

To make this project better, I have some ideas:

* Add a NoSQL database to this Flask application.  The database could contain the first 10,000 records of Fibonacci numbers, and the application could read from the database instead of calculating the numbers for each request.
* Add a caching server (memcached, redis) in front of the web server to cache the responses
* Not that the data is private information, but if we wanted it to be secure, we could put the web server(s) (containers) behind a load balancer and terminate SSL/TLS at the LB.
* As I've written it, the function that calculates the Fibonacci numbers is a linear function with O(n) time (slow).  I should rewrite the function to use the "Power series" generating function (I think it is something to do with a matrix of power operations, and maybe it is O(log n) time). c.f. https://en.wikipedia.org/wiki/Fibonacci_number#Power_series
* Extend the app to also provide which of the numbers returned are Prime numbers (Fibonacci primes)
* Extend the app to let you choose not just an index to end with (n), but an index to start with (a), such that if a=3 and n=6, return the Fibonacci numbers between the third Fibonacci number and the sixth Fibonacci number, inclusive.
* Decide on version of Flask to lock onto in `requirements.txt` and use it in Dockerfile
* For fun, rewrite the calc_fib function as a recursive function. Well,

``` python
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)
```


### code for fun

Seems like this is a common code project, but this is my take on it.  

Despite ample coding opportunities at my day job, in my own time I like to practice other challenges found online.  I especially like the following websites for code challenges:
* hackerrank.com
* codingame.com
* projecteuler.net

