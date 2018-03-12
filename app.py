#!/usr/local/bin/python3
"""
Fibonacci REST API with Flask
"""

import json
import logging
import sys
import os
import time

from flask import Flask, request
app = Flask(__name__)

LOGGER = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


####################################
############# CALC FIB #############
####################################
def calc_fib(n):
    """ Take a number, n, and return a list of the first n Fibonacci numbers """
    if n < 0:
        LOGGER.error("- ERROR: Cannot accept a negative number")
        return "ERROR: Cannot accept a negative number"

    if n > 3000:
        LOGGER.error("- ERROR: Input number is too large; dev needs to optimize \
the Fibonacci calculation function (currently a slow O(n) function.)")
        return "ERROR: Input number is too large; dev needs to optimize \
the Fibonacci calculation function (currently a slow O(n) function.)"

    _ = 0
    __ = 1
    result = [0,1]

    while len(result) <= n:
        _   = _ + __
        __  = _ + __
        result.extend([_, __])

    LOGGER.info("- INFO: Computed Fn for n = %s: %s", str(n), str(result[:n+1]))
    return result[:n+1]


#################################
############# FLASK #############
#################################
@app.route('/')
def home():
    return 'Please see the project README.md for instructions on usage.'

@app.route('/fib')
def flask_fib():
    n = int(request.args.get('n'))
    return str(calc_fib(n))


##################################
############## MAIN ##############
##################################
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=80)

    except Exception as oops:
        LOGGER.error(oops)
        LOGGER.error(str(sys.exc_info()[0]))
        raise oops

