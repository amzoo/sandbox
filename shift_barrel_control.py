""" 
Calculate shortest angle between two angles, direction, and if it crosses zero

As a test only using one shift barrel with 6 gear positions

"""

# Steps per rev
steps_rev = 1000

# Define angle positions of each gear, which should always be constant
gear_1_pos = 180
gear_2_pos = 252
gear_3_pos = 308
gear_4_pos = 12
gear_5_pos = 74
gear_6_pos = 123

gear_pos = [gear_1_pos, gear_2_pos, gear_3_pos, gear_4_pos, gear_5_pos, gear_6_pos]


def shift(current_gear, target_gear):
	# Get angle position from gear index
	current_gear_pos = gear_pos[current_gear-1]
	target_gear_pos = gear_pos[target_gear-1]

	# Determine shift direction
	shift_dir = 0
	if target_gear is not current_gear:
		shift_dir = int((target_gear - current_gear) / abs(target_gear - current_gear))

	# Calculate raw distance between two points, mod 360 to remove multiple rotations, then determine the shortest angle
	raw_dist = (target_gear_pos - current_gear_pos) * shift_dir
	mod_dist = raw_dist % 360
	short_dist = mod_dist
	if mod_dist >= 180:
		short_dist = 360 - mod_dist

	steps = int(short_dist / 360 * steps_rev)

	# Check if travel passes through 0
	cross_zero = False
	if current_gear_pos + short_dist * shift_dir > 360 or current_gear_pos + short_dist * shift_dir < 0:
		cross_zero = True 

	return short_dist, steps, shift_dir, cross_zero


if __name__ == "__main__":
	# Test up shift
	for i in range(1,6,1):
		print("Shifting from {} to {}".format(i, i+1))
		print("Angle to Target, Steps to Target, Direction, Passes through Zero")
		print(shift(i,i+1))
		print("\n")

	# Test down shift
	for i in range(6,1,-1):
		print("Shifting from {} to {}".format(i, i-1))
		print("Angle to Target, Steps to Target, Direction, Passes through Zero")
		print(shift(i,i-1))
		print("\n")

	"""
	Shifting from 1 to 2
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(72, 200, 1, False)


	Shifting from 2 to 3
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(56, 155, 1, False)


	Shifting from 3 to 4
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(64, 177, 1, True)


	Shifting from 4 to 5
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(62, 172, 1, False)


	Shifting from 5 to 6
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(49, 136, 1, False)


	Shifting from 6 to 5
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(49, 136, -1, False)


	Shifting from 5 to 4
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(62, 172, -1, False)


	Shifting from 4 to 3
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(64, 177, -1, True)


	Shifting from 3 to 2
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(56, 155, -1, False)


	Shifting from 2 to 1
	Angle to Target, Steps to Target, Direction, Passes through Zero
	(72, 200, -1, False)

	"""