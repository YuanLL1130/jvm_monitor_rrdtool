#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-09 10:13:56
# @Author  : LiHongyuan (hy.li@8win.com)

import requests
import json


data = {"Process_Name": "service_account", "jvmType": "JAVA_S0_S1_Eden_Metadata", "GCT_avg": "0.010", "S1_max": "4194304.00", "S1_ratio": "0.00", "Old_max": "20971520.00", "Heap_max": "62914560.00", "YGCT_avg": "0.010", "FGCT_avg": "0", "FGC": "0", "Metadata_used": "15324364.80", "Heap_used": "26282803.20", "Eden_max": "33554432.00", "Old_used": "10134630.40", "Eden_used": "15132364.80", "YGC": "6", "ipaddress": "1102356884", "YGCT": "0.060", "Eden_ratio": "69.94", "S0_used": "0.00", "Metadata_max": "15990784.00", "FGCT": "0.000", "Old_ratio": "48.33", "Heap_ratio": "41.78", "S0_ratio": "87.26", "S1_used": "1015808.00", "S0_max": "4194304.00", "Metadata_ratio": "97.30", "GCT": "0.060"}
data = json.dumps(data)
res = requests.post("http://127.0.0.1:5000/upload/",data=data)
print res.text
