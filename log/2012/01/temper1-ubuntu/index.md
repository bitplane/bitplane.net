# TEMPer1 temperature sensor in Linux

Yey! Just got my
[PCSensor TEMPer1 USB thermometer](https://web.archive.org/web/20161020072344/http://pcsensor.com/index.php?_a=viewProd&productId=7)
logging in Linux. It automatically detects and does expose USB HID profiles, but
there’s no way to access the data by holding down the CAPS key like it says in
the docs.

Thankfully, a search for the device ID (0c45:7401 Microdia) finds ruby bindings
for Temper.c by [Michitaka Ohno](https://github.com/elpeo), which conveniently
includes the reverse-engineered USB protocol. So I’ve
[forked this on GitHub](https://github.com/bitplane/temper), removed the Ruby
bits, edited the unit test wrapped it up in a little script that logs the time
and temperature to a CSV file. It currently only supports one device, which will
change if I ever get another one of these devices (spoiler: I probably will)

To start logging your TEMPer1′s data in Ubuntu just

```shell
 # install dependencies
 $ sudo apt-get install git build-essential libusb-0.1.4 libusb-0.1.4-dev
 # clone the logger
 $ git clone git://github.com/bitplane/temper.git
 # build it
 $ cd temper
 $ make clean
 $ make
 # start logging!
 $ sudo ./log.sh > temperature.log
```

Now I’m just waiting for my USB clip-on-mic to arrive. Once it does I can log
the bubbles from the airlock on my beverages along with the temperature, and
make some pretty graphs.

Watch this space!
