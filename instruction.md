Requires Python 3.9 (Otherwise stated)

*Turn on word warp to see all text.

Note: All script only works with tabs and correct ES data format

## map mover
-Enter two values: X offset and Y offset
-Read map.txt and outputs in nmap.txt

## submunition loop maker
-Prepare template file, use [replace] to mark where the number goes.
-*With square brackets.
-Requires one [replace] within "outfit" line and one within "submunition" line.
-Space before and after [replace] is REQUIRED.
-Each [replace] in submunition line will increment the the number by 1, be careful.

## submunition loop lifetime reduce
-Mostly the same as "submunition loop maker"
-Additional time delay input, each iteration of the munition will have lifetime reduced by this number.
-Lifetime of the first submunition = time delay * loop count
-Requires [replace] in lifetime line.(In place of number)

## system arrival
-Use belt value or habitable value, whichever is higher to set arrival distance then adds by offset value.
-Edit the script file with text editor and edit these at the top of the script:
	offset = 50 #Value to add
	minimalarrival = 0.
	maximumarrival = 10000.

## 0-10-7_rebalance_adj
**Requires Python 3.10+**
Optionally use sklearn library, otherwise will try to use lookup table.
Also download 0-10-7_rebal_mult_model for guessing the multiplier value
Put a data folder with ship in the same directory as this file
Output will be in "output" folder with "000 BAL-10-7" prefix

What it does:
Adjust mass, heat dissipation, and drag the same way it was done in 0.10.7 (https://docs.google.com/spreadsheets/d/1F-dPCeTjWYQfA64flG2qzKdfec9z0_YrIqBGbSOxmwI/edit?gid=1373529923#gid=1373529923)
Also add scrambling protection and resistance to ship with ion protection/resistance