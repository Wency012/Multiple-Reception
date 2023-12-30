#!/usr/bin/env python
# -*- coding: latin-1 -*-xyer

import struct
import random

# 模拟生成随机的RTK数据
def generate_rtk_data():
    # 假设的GPS修正数据范围
    min_latitude = 37.00#经度
    max_latitude = 38.00
    min_longitude = -122.00#纬度
    max_longitude = -121.00
    min_altitude = 0.0#海拔高度
    max_altitude = 100.0
    min_correction = -0.5# 假设的GPS修正值
    max_correction = 0.5


    # RTCM消息类型 1005: GPS系统和天线类型
    msg_type = 1005
    # RTCM版本 3
    version = 3
    # 参考站ID范围
    min_reference_station_id = 1000
    max_reference_station_id = 2000

    # 生成随机的GPS修正数据
    latitude = random.uniform(min_latitude, max_latitude)
    longitude = random.uniform(min_longitude, max_longitude)
    altitude = random.uniform(min_altitude, max_altitude)
    correction = random.uniform(min_correction, max_correction)

    reference_station_id = random.randint(min_reference_station_id, max_reference_station_id)

    # 构造RTCM消息
    msg = struct.pack('>HHH', msg_type, version, reference_station_id)
    msg += struct.pack('>I', int(latitude * 10000))
    msg += struct.pack('>q', int(longitude * 10000))
    msg += struct.pack('>I', int(altitude * 100))
    # 将修正值拆分成两个较小的整数，然后分别打包
    correction_int = int(correction * 100)
    correction_low = correction_int & 0xFF
    correction_high = (correction_int >> 8) & 0xFF
    msg += struct.pack('>HH', correction_low, correction_high)

    return msg

if __name__ == "__main__":
    num_samples = 10000  # 要生成的数据集样本数量

    rtcm_data_set = []
    for _ in range(num_samples):
        rtcm_data = generate_rtk_data()
        rtcm_data_set.append(rtcm_data)

    # 保存数据集到文件
    with open("generate_rtcm.bin", "wb") as file:
        for data in rtcm_data_set:
            file.write(data)

    #print(f"Generated {num_samples} RTCM data samples and saved to 'rtcm_data_set.bin'.")

