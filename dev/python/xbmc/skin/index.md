# XBMC skin script

Made this in 2004 or so with the IRC thingy. Download it [here](./py_skin.zip)

## Docs follow...

xbmc skin reader script 0.1 by bitplane


A nice little thing to make your scripts skinnable. This is pretty much hacked together, but it works okay.

info for skinners:
------------------

My skins work a little differently from normal ones...

1) Control and window <id>s can be text, makes the place look tidier. The IDs aren't the same as the ones used by XBMC, but they should be unique or you'll lose references to controls.

2) a controls <label> can be numers or text. If it is a number, it will be replaced by the appropriate string from the current language file.

3) they can contain python expressions and variables. Variables are created for each of the tags in the root of the <window> section, and are called by putting brackets around their name. Presently, only (width) and (height) variables are included by default.
Here's an example:

<window>
  <id>my_window</id>
  <middlex>(width)*0.50</middlex>
  <controls>
  </controls>
</window>

NOTES: 

* Variables are ONLY evaluated in the <window> section and in the <posx>, <posy>, <width> and <height> of a control. So you can't use them to make up labels, fonts, colours, or other strings (yet).
* Variables are evaluated as soon the script reads the line in the xml, so you can't reference a variable before it's been created.
* You can change variables as you go along, so you can use temp values for any big or confusing calculations that you need to do. In the following XML, the background image will fall short of the screen height by 10%

<window>
  <id>my_window</id>
  <x>(height)*0.10</x>  <!-- x is 10% of the screens height     !-->
  <x>(height)-(x)</x>   <!-- x is now 90% of the screens height !-->
  <controls>
	<control>
		<description>background image</description>
		<type>image</type>
		<id>imgbackground</id>
		<posX>0</posX>
		<posY>0</posY>
		<width>(width)</width>
		<height>(x)</height>
		<texture>background.png</texture>
	</control>
  </controls>
</window>

If you're not familliar with programming, it's worth noting that "10+4*2" is 18, not 28 as you might expect- multiplication and division are handled before addition and subtraction. use brackets to clarify: "(10+4)*2" is 28. Unfortunately, in a script this would probably look more like "((z)+(x))*(y)", its worth splitting ugly expressions over a few lines and commenting them like in the example above.

GET PAPER AND A PENCIL!

Sketch your screen on the paper and make it look pretty, then give each offset a meaningful name, and work out where about it should be...

<topborder>(height)*0.10</topborder>
<widthofabutton>100</widthofabutton>
<heightofabutton>30</heightofabutton>
<spacebetweenbuttons>15</spacebetweenbuttons>
<nextbutton>(heightofabutton)+(spacebetweenbuttons)</nextbutton>
<topofallbuttons>(topborder)+(spacebetweenbuttons)</topofallbuttons>
<button1posy>(topofallbuttons)</button1posy>
<button2posy>(topofallbuttons)+(nextbutton)</button2posy>
<button3posy>(topofallbuttons)+((nextbutton)*2)</button3posy>
<button4posy>(topofallbuttons)+((nextbutton)*3)</button4posy>

Then use the variables to position your controls like in the examples above. You can put big complicated calculations in the controls, but its best to set them up beforehand so you can change your entire layout by editing one value at the top of the xml. Cool huh?

Of course you don't need to use variables if you don't want to, but then you'll need a new script file for every screen mode. haha.


4) Windows within windows. <group>groupname</group>
The <group> tag is attached to a control to separate visible parts of a window at a given time, I thought it was easier than having loads of different window instances. Skinners can add graphics and text to submenus in the program, and coders can easily add new controls to a specific section without having to butcher the code.

If no group is set, or if it's empty or "-", then no group is assumed and the control is visible at all times.
If a group is set, it won't be visible until the group is active. 

If set, the window's <defaultcontrol> says which control in the "empty" group will get the focus, like so: <defaultcontrol>btnconnect</defaultcontrol>

Alternatively, you can set the window's <defaultgroup>, and give one of the controls in the group a <default> tag. This is best left to the coder though.

<window>
  <defaultgroup>group1</defaultgroup>
  <controls>
    <control>
      <type>button</type>
      <id>btnhelloworld</id>
      <posX>100</posX>
      <posY>100</posY>
      <width>100</width>
      <height>32</height>
      <label>Hello World!</label>
      <group>group1</group>
      <default>Yes sir, we have a default tag that isn't empty</default>
    </control>
  </controls>
</window>



Info for coders:
----------------

The main class is XBMC_SKIN, which is derived from xbmcgui.Window
So to use it, just subclass it like a normal xbmc.Window.
When you override the onAction method, you'll need to get the control's ID string from the xml. like so:

  def onAction(self, control):
    id = self.getcontrolid(control)

    if id == "btnprivatefiles":
      print "dummy button activated! We have a nosey bastard"


the XBMC_SKIN_CONTROL class doesn't inherrit anything, it links to the control by it's "control" variable - you'll need to remember this when you're referencing the it in the code. 
It's:
  self.controls["lbloutput"].control.setText("Push off nosey")

NOT:
  self.controls["lbloutput"].setText("Push off nosey")

Perhaps it should be, and I might change this in future. To be honest I couldn't be arsed with the agro of debugging my first attempt at multiple class inherritance on the xbox.



Class XBMC_SKIN(xbmcgui.Window)

  functions:
    loadskin("filename")          # loads the skin. the full path must be given
    getoption("option")           # returns the window option from .options if it exists
                                  # or "" if not, without raising error.
    showgroup("group")            # shows all controls with the group name "group" or ""
    getcontrolid(xbmcgui.Control) # gets the ID of the specified control


  variables:
    path                      # path to the skin, for getting images
    options                   # dictionary of strings containing variables and window 
                              # settings, (like window "id")
    controls                  # dictionary of skin controls by ID
                              # ie) controls["id"] = XBMC_SKIN_CONTROL
    group                     # string containing name of last set group


Class XBMC_SKIN_CONTROL()

  functions:
    getoption("option")           # returns the window option from .options if it exists
                                  # or "" if not, without raising error.

  variables:
    owner                    # back reference to the window
    control                  # reference to the actual xbmcgui.Control
    options                  # the tags from the xml, ie) if x.options["width"] == 51



# a very short demo...

import xbmcskin

x = xbmcskin.XBMC_SKIN_CONTROL()
x.loadskin("e:\\test.xml")
x.doModal()
