import pywapi
import string
import sys

#this requires pywapi which can be installed from https://code.google.com/p/python-weather-api/
#If in the US 00000 should be your area code
#If in Britian, try using the BBC weather scripts found here: https://github.com/duncanj/voice_scripts

result = pywapi.get_weather_from_weather_com(str(sys.argv[1]))
cond = string.lower(result['current_conditions']['text'])
temp = str(int(1.8*int(result['current_conditions']['temperature']))+32)

print "It is " + cond + " and " + temp + "degrees now."

today_high = str(int(1.8*int(result['forecasts'][0]['high']))+32)
today_low = str(int(1.8*int(result['forecasts'][0]['low']))+32)
today_chance = result['forecasts'][0]['day']['chance_precip']

print "The high is " + today_high + ", the low is " + today_low + ", the chance of rain is " + today_chance + "%."
