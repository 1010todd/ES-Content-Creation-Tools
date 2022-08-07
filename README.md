# ES Content Creation Tools
 Tools (often Python scripts) I made to help with creating content for Endless Sky game. These tool are quickly made and not very robust, use carefully.
 
 All scrips are made using Python 3.9

### 2x mover:
Move @2x.png to a different directory.

### map mover:
Move everything in a map file.

* Enter two values: X offset and Y offset
* Read map.txt and outputs in nmap.txt

### submunition loop maker:
Read and create a loop of submunition.

* Prepare template file, use [replace] to mark where the number goes.(With square brackets.)
* Requires one [replace] within "outfit" line and one within "submunition" line.
* Space before and after [replace] is REQUIRED.
* Each [replace] in submunition line will increment the the number by 1, be careful.

### submunition loop lifetime reduce:
Read and create a loop of submunition with lifetime reduced or each iteration.

* Mostly the same as "submunition loop maker"
* Additional time delay input, each iteration of the munition will have lifetime reduced by this number.
* Lifetime of the first submunition = time delay * loop count
* Requires [replace] in lifetime line.(In place of number)

### system arrival:
Use belt value or habitable value, whichever is higher to set arrival distance then adds by offset value.

* Open the script file with text editor and edit these at the top of the script:
```
	offset = 50 #Value to add
	minimalarrival = 0.
	maximumarrival = 10000.
```

### system addminables
Quick script to add new mineables to systems, either random or depends on existing mineables. Edit the .py file to adjust.

### Actually helpful no drag report
Scan the folder the script is in for .txt with "ship" in the name and report any ship with zero/undefined drag and which line. Because the game gave useless warning like 
```
():
Defaulting missing "drag" attribute to 100.0
has outfits:
```
Which tells you absolutely nothing except something is wrong like giving a one star review without a comment, in fact not even which restaurant.