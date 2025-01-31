"""Test sensor platform for Home Assistant."""
from datetime import datetime, timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the test sensor."""
    async_add_entities([GasPriceTestSensor()], True)

class GasPriceTestSensor(SensorEntity):
    """Representation of a Test Gas Price Sensor."""
    
    def __init__(self):
        """Initialize the sensor."""
        self._name = "Gas Price Test"
        self._state = None
        self._attributes = {
            "last_updated": None
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    @Throttle(timedelta(minutes=1))
    def update(self):
        """Update the sensor value every minute."""
        now = datetime.now()
        minutes_decimal = now.minute / 1  # Gets current minute (0-59)
        self._state = 2 + (minutes_decimal / 100)  # Format: 1.35 for 35 minutes
        self._attributes["last_updated"] = now.isoformat()