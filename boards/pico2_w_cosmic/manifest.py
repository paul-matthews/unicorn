include("$(PORT_DIR)/boards/manifest.py")
include("../manifest-common.py")

# Cosmic Clock infrastructure layer (frozen into firmware)
freeze("$(BOARD_DIR)/frozen")