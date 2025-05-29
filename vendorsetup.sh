# BCR
git clone https://github.com/suvojit213/vendor_bcr.git vendor/bcr

# Clone the kernel source
echo "Cloning kernel repository..."
git clone https://github.com/dhanush281/android_xiaomi_sky_kernel.git device/xiaomi/sky-kernel

# Clone the dolby repository
git clone https://github.com/dhanush281/android_hardware_dolby hardware/dolby

# Clone the hardware repository
echo "Cloning hardware repository..."
git clone https://github.com/LineageOS/android_hardware_xiaomi.git hardware/xiaomi

# Clone the agm repository
echo "cloning agm repository..."
rm -rf hardware/qcom-caf/sm8450/audio/agm && git clone https://github.com/dhanush281/agm.git hardware/qcom-caf/sm8450/audio/agm

echo "done"

rm -rf hardware/qcom-caf/sm8450/audio/pal && git clone https://github.com/lostark13/arpal-lx hardware/qcom-caf/sm8450/audio/pal

echo "done"