More actions
# Get rid of that by overriding it in /product on any builds
PRODUCT_PRODUCT_PROPERTIES += \
    ro.secure=0 \
    ro.adb.secure=0