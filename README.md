## SCSU River Data Sound Art Installation

This project is a proof-of-concept and plan for a sonification-based sound art installation designed for the St. Cloud State University campus. Live audio is synthesized based on hydrophonic sound and flow data collected from three Raspberry Pi river buoys, and played back at several locations on campus, to sonically bridge the divide between campus and the adjacent section of the Mississippi river.

**river.pdf** contains a description of the project and rough outline of the plan.

**riverreadmidi.py** is unfinished, untested example code to run onboard the buoy, demonstrating how local sensor data and live data from USGS could be gathered and output to a virtual MIDI loopback port.

**HydrophoneTest.wav** is a sample hydrophonic recording taken from the river, as a stand-in for the live audio that would be captured onboard the buoy.

**SamplePatch.vcv** is a patch for VCV Rack 1.1.6 with an example "algorithm" for the synthesized sound, in which flow rate and gage height data, input via MIDI, are used to control root frequency and structure of a resonator applied to the hydrophonic audio. In this example, a recording is substituted for live hydrophonic audio. For testing and demonstration, an external control surface can be substituted for the loopback virtual MIDI interface.

**SamplePatchOutput.wav** demonstrates how the example patch might sound over an extended period, with multiple days worth of artificial data compressed into three minutes.
