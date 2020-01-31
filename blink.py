import asyncio
from .utils import get_light_attributes, get_start_attributes, DOMAIN

async def blink_setup(hass):
	async def blink(call):
		"""
		Blink a light, then reset it to its original state
		"""
		entity_id = call.data['entity_id']
		blinks = call.data.get('blinks', 2)
		blink_on = call.data.get('blink_on', 1.0)
		blink_off = call.data.get('blink_off', 1.0)
		trans_on = call.data.get('trans_on', 1.0)
		trans_off = call.data.get('trans_off', 1.0)
		blink_attributes = get_light_attributes(call.data)
		
		state = hass.states.get(entity_id)
		start_state = state.state
		start_attributes = get_start_attributes(state.attributes)
		blink_attributes['entity_id'] = entity_id
		blink_attributes['transition'] = blink_on * trans_on
		start_attributes['entity_id'] = entity_id
		start_attributes['transition'] = 0
		
		for _ in range(blinks):
			await hass.services.async_call('light', 'turn_on', blink_attributes, True)
			await asyncio.sleep(blink_on)
			await hass.services.async_call('light', 'turn_off', {'entity_id':entity_id, 'transition':trans_off*blink_off}, True)
			await asyncio.sleep(blink_off)
		
		await hass.services.async_call('light', 'turn_on', start_attributes, True)	
		if start_state == 'off':
			await hass.services.async_call('light', 'turn_off', {'entity_id':entity_id, 'transition':0}, True)	
	
	hass.services.async_register(DOMAIN, 'blink', blink)
	