import csv
import mido
import pigpio
import time
import os

buoy = pigpio.pi()
outport = mido.open_output('') #use midi loopback driver from get_output_names()
flowRE = mido.Message('control_change', channel=2, control=2, value=127)
flowFE = mido.Message('control_change', channel=2, control=2, value=0)
flowMeterPin = 12
buoy.set_mode(flowMeterPin, pigpio.INPUT)

cbRE = buoy.callback(flowMeterPin, pigpio.RISING_EDGE, outport.send(flowRE))
cbFE = buoy.callback(flowMeterPin, pigpio.FALLING_EDGE, outport.send(flowFE))

rda = []
while True:
	os.system('wget "https://waterservices.usgs.gov/nwis/iv/?sites=05270700&parameterCd=00065&siteStatus=all&format=rdb&period=P1D" -O river.tsv')
	def decomment(csvfile):
	    for row in csvfile:
	        raw = row.split('#')[0].strip()
	        if raw: yield raw
	with open("river.tsv") as fd:
	    rd = csv.reader(decomment(fd), delimiter="\t")
	    for row in rd:
		rda.append(row)
	latestGaugeHeight = (((rda[-1][-2])-5)/3)*127
	outport.send(mido.Message('control_change', channel=2, control=3, value=latestGaugeHeight))
	time.sleep(900)
