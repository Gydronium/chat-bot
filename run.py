from kutana import *
from vk.manager import vk_manager

# Create application
app = Kutana()

# Create and add VKManager to application
app.add_manager(vk_manager)

# Load and register plugins
app.register_plugins(load_plugins("plugins/"))

# Run application
app.run()
