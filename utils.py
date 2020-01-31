import copy

LIGHT_ATTRIBUTES = {"rgb_color", "color_name", "hs_color", "xy_color","color_temp","kelvin","white_value","brightness","brightness_pct","profile"}
PROFILE_ATTRIBUTE = "profile"
COLOR_ATTRIBUTE = "rgb_color"
WHITE_AMBIANCE_ATTRIBUTE = "color_temp"
WHITE_ATTRIBUTE = "brightness"

DOMAIN = 'light_effects'

def get_light_attributes(att):
	"""
	get a new dict with the light attributes of att
	"""
	light_attributes = dict()
	for la in LIGHT_ATTRIBUTES:
		if la in att:
			light_attributes[la] = att[la]
	return light_attributes

def get_start_attributes(state_atts):
	"""
	get a new dict to restore state from the changed atts. The new dict is a deep copy
	"""
	if PROFILE_ATTRIBUTE in state_atts:
		return {PROFILE_ATTRIBUTE: state_atts[PROFILE_ATTRIBUTE]}
	
	#color light
	if COLOR_ATTRIBUTE in state_atts:
		return {COLOR_ATTRIBUTE: copy.deepcopy(state_atts[COLOR_ATTRIBUTE])}
	
	#white ambience light
	light_attributes = dict()
	if WHITE_AMBIANCE_ATTRIBUTE in state_atts:
		light_attributes[WHITE_AMBIANCE_ATTRIBUTE] = state_atts[WHITE_AMBIANCE_ATTRIBUTE]
	
	#white (ambience) light
	light_attributes[WHITE_ATTRIBUTE] = state_atts[WHITE_ATTRIBUTE]
	return light_attributes
