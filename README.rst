============
robopython
============


.. image:: https://img.shields.io/pypi/v/robopython.svg
        :target: https://pypi.python.org/pypi/robopython

.. image:: https://img.shields.io/travis/JonRobo/robopython.svg
        :target: https://travis-ci.org/JonRobo/robopython

.. image:: https://readthedocs.org/projects/robopython/badge/?version=latest
        :target: https://robopython.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Robo Wunderkind Python API - BLED112 USB Dongle Required


* Free software: Apache Software License 2.0
* Documentation: https://robopython.readthedocs.io.


Features
----------

* New Module integration such as Line Tracker
* MQTT Wi-Fi networking
* Fuzzy Logic Filter for Sensors/States

Getting Started
-----------------
* Install with: pip install robopython

* Create an instance of Robo object by doing: my_robo = Robo("<BLE Name>")

* Test Functionality by playing a sound with: my_robo.System.play_sound(0)

Troubleshooting
------------------
If you get an error saying No BGAPI compatable device is detected please insert the BLED112 USB dongle or switch USB ports
If problem persists you can identify the COM port explicitley with my_robo = Robo("<BLE Name>", COM PORT)
