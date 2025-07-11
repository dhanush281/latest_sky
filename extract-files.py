#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sky',
    'hardware/qcom-caf/sm8450',
    'hardware/qcom-caf/sm8450/audio/agm/ipc/HwBinders/legacy',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.dpmservice@1.1',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccvndhal@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'com.qualcomm.qti.dpm.api@1.0',
    ): lib_fixup_vendor_suffix,
    (
        'libagm',
        'libagmclient',
        'libagmmixer',
        'libar-pal',
        'libpalclient',
        'libsndcardparser',
        'libwpa_client',
        'vendor.qti.hardware.pal@1.0-impl',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/libnfc-nxp-pnscr.conf': blob_fixup()
        .regex_replace(
	    'NXP_T4T_NFCEE_ENABLE=0x01', 'NXP_T4T_NFCEE_ENABLE=0x00'
	),
    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    'system_ext/lib64/libwfdservice.so': blob_fixup()
        .replace_needed(
            'android.media.audio.common.types-V2-cpp.so',
            'android.media.audio.common.types-V4-cpp.so',
        )
        .replace_needed(
            'android.hardware.common-V2-ndk_platform.so',
            'android.hardware.common-V2-ndk.so',
        ),
    (
        'vendor/bin/hw/android.hardware.security.keymint-service-qti',
        'vendor/lib64/libqtikeymint.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.security.keymint-V1-ndk_platform.so',
            'android.hardware.security.keymint-V1-ndk.so',
        )
        .replace_needed(
            'android.hardware.security.secureclock-V1-ndk_platform.so',
            'android.hardware.security.secureclock-V1-ndk.so',
        )
        .replace_needed(
            'android.hardware.security.sharedsecret-V1-ndk_platform.so',
            'android.hardware.security.sharedsecret-V1-ndk.so',
        )
        .add_needed('android.hardware.security.rkp-V1-ndk.so'),
    'vendor/bin/qcc-trd': blob_fixup()
        .replace_needed(
            'libgrpc++_unsecure.so', 'libgrpc++_unsecure_prebuilt.so'
        ),
    'vendor/lib64/hw/fingerprint.fpc.default.so': blob_fixup()
        .replace_needed(
            'com.fingerprints.extension@1.0.so', 'com.fingerprints.extension@1.0_vendor.so'
        ),
    'vendor/lib64/hw/fingerprint.goodix.default.so': blob_fixup()
        .fix_soname(),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed(
            'vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'
        ),
    'vendor/lib64/libhme.so': blob_fixup()
        .replace_needed(
            'libstdc++.so', 'libstdc++_vendor.so'
        ),
    'vendor/lib64/libimp.so': blob_fixup()
        .replace_needed(
            'libjnigraphics.so', 'libjnigraphics_prebuilt.so'
        ),
    'vendor/lib64/libopencv_java4.so': blob_fixup()
        .replace_needed(
            'libjnigraphics.so', 'libjnigraphics_prebuilt.so'
        ),
    'vendor/etc/media_codecs_ravelin.xml': blob_fixup()
        .regex_replace('.+media_codecs_(google_audio|google_c2|google_telephony|vendor_audio).+\n', ''),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/etc/seccomp_policy/c2audio.vendor.ext-arm64.policy': blob_fixup()
        .add_line_if_missing('setsockopt: 1'),
    'vendor/etc/seccomp_policy/wfdhdcphalservice.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libhidlbase_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'sky',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
