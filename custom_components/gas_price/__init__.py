"""The Gas Prices integration."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Gas Prices component."""
    return True