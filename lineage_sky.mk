#
# Copyright (C) 2023 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/sky

# Configure core_64_bit.mk
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)

# Configure full_base_telephony.mk
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit common lineage configurations
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

$(call inherit-product, vendor/lineage/config/BoardConfigReservedSize.mk)

# Inherit device configurations
$(call inherit-product, $(DEVICE_PATH)/device.mk)

# Inherit from the proprietary version
$(call inherit-product, vendor/xiaomi/sky/sky-vendor.mk)

# Define rear camera specs (multiple sensors supported)
AXION_CAMERA_REAR_INFO := 50,2  # Example: 50MP + 2MP

# Define front camera specs
AXION_CAMERA_FRONT_INFO := 8  # Example: 8MP

# Maintainer name (use "_" for spaces, e.g., "rmp_22" → "rmp 22" in UI)
AXION_MAINTAINER := Dhanush_x_Ashwani

# Processor name (use "_" for spaces)
AXION_PROCESSOR := Snapdragon®_4_gen_2

TARGET_BOOT_ANIMATION_RES := 1080
TARGET_ENABLE_BLUR := false

AXION_CPU_SMALL_CORES     := 0,1,2,3,4,5
AXION_CPU_BIG_CORES       := 6,7
AXION_CPU_UNLIMIT_UI      := 0-7
AXION_CPU_BG              := 0-3
AXION_CPU_FG              := 0-6
AXION_CPU_LIMIT_BG        := 0-2
AXION_CPU_LIMIT_UI        := 0-5

# Wether to enable debugging for adb logcat purposes
AXION_DEBUGGING_ENABLED := false

## Device identifier
PRODUCT_DEVICE := sky
PRODUCT_NAME := lineage_sky
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 23076RN4BI
PRODUCT_MANUFACTURER := Xiaomi

# GMS
PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
