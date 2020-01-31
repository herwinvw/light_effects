"""The light effects component."""
from .blink import blink_setup


DEPENDENCIES = ["group", "light"]


async def async_setup (hass, config):
	await blink_setup(hass)
	return True
