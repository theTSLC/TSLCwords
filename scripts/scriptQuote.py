#!/usr/bin/env python
#Importing quotes for TSLCwords database
#resource: http://www.dreamsyssoft.com/python-scripting-tutorial/intro-tutorial.php

import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-a', '--author', help='Author\'s name')
parser.add_option('-q', '--quote', help='Quote')

(options, args) = parser.parse_args()

if options.author is None:
		options.author = raw_input('Enter author\'s name:')

if options.quote is None:
		options.quote = raw_input('Enter the quote:')

confirmIn = 'Here is your input: ' + options.author + ' once said ' + options.quote

thankYou = 'Thank you for your input. Please check back later for full database import functionality'

print confirmIn, '\n', thankYou