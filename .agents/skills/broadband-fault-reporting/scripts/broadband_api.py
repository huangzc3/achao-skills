#!/usr/bin/env python3
"""
Broadband API Client
封装所有宽带报障相关的 API 接口调用
"""

import requests
import json
from typing import Dict, Any, List, Optional


# API 基础配置
BASE_URL = "http://127.0.0.1:8080"
TIMEOUT = 30


def _make_request(method: str, url: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
    """
    通用 HTTP 请求函数

    Args:
        method: HTTP 方法 ('GET' 或 'POST')
        url: 完整的请求 URL
        params: GET 请求的查询参数
        data: POST 请求的 JSON 数据

    Returns:
        API 响应的 JSON 数据（已解析）
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=params, timeout=TIMEOUT)
        else:
            response = requests.post(url, json=data, timeout=TIMEOUT)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "code": 500,
            "message": f"请求失败: {str(e)}",
            "data": None
        }


def query_roam_is_telecom(deviceNum: str, callId: str) -> Dict[str, Any]:
    """
    本地本网判断

    Args:
        deviceNum: 号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "isTelecom": "1"  # 1本网 0异网
            }
        }
    """
    url = f"{BASE_URL}/query_roam_is_telecom"
    params = {"deviceNum": deviceNum, "callId": callId}
    return _make_request("GET", url, params=params)


def get_broadband_list_by_dif_network(accNbr: str, callId: str) -> Dict[str, Any]:
    """
    非本网宽带信息获取

    Args:
        accNbr: 号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": [
                {
                    "broadband_id": "AD0000604487",
                    "address": "上海市浦东新区浦兴路街道平度路488弄4号7层703室"
                }
            ]
        }
    """
    url = f"{BASE_URL}/get_broadband_list_by_dif_network"
    params = {"accNbr": accNbr, "callId": callId}
    return _make_request("GET", url, params=params)


def get_broadband_list_by_accNbr(accNbr: str, callId: str) -> Dict[str, Any]:
    """
    根据手机/固话获取名下宽带信息

    Args:
        accNbr: 号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": [
                {
                    "broadband_id": "AD0000604487",
                    "address": "上海市浦东新区浦兴路街道平度路488弄4号7层703室"
                }
            ]
        }
    """
    url = f"{BASE_URL}/get_broadband_list_by_accNbr"
    params = {"accNbr": accNbr, "callId": callId}
    return _make_request("GET", url, params=params)


def get_broadband_list_by_id(id: str, callId: str) -> Dict[str, Any]:
    """
    根据身份证获取名下宽带信息

    Args:
        id: 身份证号
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": [
                {
                    "broadband_id": "AD0000604487",
                    "address": "上海市浦东新区浦兴路街道平度路488弄4号7层703室"
                }
            ]
        }
    """
    url = f"{BASE_URL}/get_broadband_list_by_id"
    params = {"id": id, "callId": callId}
    return _make_request("GET", url, params=params)


def getBroadbandListByDeviceNum(deviceNum: str, callId: str) -> Dict[str, Any]:
    """
    根据宽带账号获取名下宽带信息

    Args:
        deviceNum: 宽带账号
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": [
                {
                    "broadband_id": "AD0000604487",
                    "address": "上海市浦东新区浦兴路街道平度路488弄4号7层703室"
                }
            ]
        }
    """
    url = f"{BASE_URL}/getBroadbandListByDeviceNum"
    params = {"deviceNum": deviceNum, "callId": callId}
    return _make_request("GET", url, params=params)


def query_broadband_device_group(deviceNum: str, callId: str) -> Dict[str, Any]:
    """
    根据宽带账号查询属性（校园网、政企、白金、欠费用户等）

    Args:
        deviceNum: 宽带账号
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "isCampusNet": "0",  # 是否校园网【1是0否】
                "isEnterpriseGov": "0",  # 是否政企【1是0否】
                "isSpecialScene": "0",  # 是否白金【1是0否】
                "haveP6": "0",  # 是否在途【1是0否】
                "isHalt": "0",  # 是否欠费【1是0否】
                "routCode": ""  # 人工编码
            }
        }
    """
    url = f"{BASE_URL}/query_broadband_device_group"
    params = {"deviceNum": deviceNum, "callId": callId}
    return _make_request("GET", url, params=params)


def sh_getP6ByDevice(accNbr: str, callId: str) -> Dict[str, Any]:
    """
    根据宽带账号查询是否拥有在途订单

    Args:
        accNbr: 宽带账号
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "isFault": "0"  # 是否在途【0无在途故障，1有在途故障】
            }
        }
    """
    url = f"{BASE_URL}/sh_getP6ByDevice"
    data = {"accNbr": accNbr, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_testKD(deviceNum: str, callId: str) -> Dict[str, Any]:
    """
    根据宽带账号进行宽带诊断

    Args:
        deviceNum: 宽带账号
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "conId": "118915",
                "conDesc": "AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查",
                "testOk": "0",  # 测试是否正常【0正常1需要派修-1测试失败】
                "advice": "AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查",
                "dispatch": "区局（机房）",
                "isQZ": "0"  # 是否群障【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/sh_testKD"
    data = {"deviceNum": deviceNum, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_serverRestart(accNbr: str, accType: int, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行重启

    Args:
        accNbr: 业务号码
        accType: 业务类型【0-移动，1-固话，2-宽带，3-IPTV】
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "conId": "118915",
                "conDesc": "AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查",
                "testOk": "0",
                "advice": "AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查",
                "dispatch": "区局（机房）",
                "isQZ": "0"
            }
        }
    """
    url = f"{BASE_URL}/sh_serverRestart"
    data = {"accNbr": accNbr, "accType": accType, "callId": callId}
    return _make_request("POST", url, data=data)


def appealinsys(startTime: str, dirNum: str, tel: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行派修

    Args:
        startTime: 派修时间
        dirNum: 主叫号码
        tel: 联系号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "res": "1"  # 派修结果【1成功0失败】
            }
        }
    """
    url = f"{BASE_URL}/appealinsys"
    data = {"startTime": startTime, "dirNum": dirNum, "tel": tel, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_recordFault_original(dirNum: str, tel: str, caller: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行记录结案

    Args:
        dirNum: 设备号
        tel: 联系号码
        caller: 主叫号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "bookType": "1"  # 是否成功申告【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/sh_recordFault_original"
    data = {"dirNum": dirNum, "tel": tel, "caller": caller, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_cancelRepairRequest(accNbr: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行取消派修

    Args:
        accNbr: 业务号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "result": "1"  # 是否成功【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/sh_cancelRepairRequest"
    data = {"accNbr": accNbr, "callId": callId}
    return _make_request("POST", url, data=data)


def change_broadband_appointment(dirNum: str, begin: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行改约

    Args:
        dirNum: 业务号码
        begin: 修改时间
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "result": "1"  # 是否成功【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/change_broadband_appointment"
    data = {"dirNum": dirNum, "begin": begin, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_urgentRepair(accNbr: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行催修

    Args:
        accNbr: 业务号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "result": "1"  # 是否成功【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/sh_urgentRepair"
    data = {"accNbr": accNbr, "callId": callId}
    return _make_request("POST", url, data=data)


def sh_updateTel(dirNum: str, newTel: str, callId: str) -> Dict[str, Any]:
    """
    对某个宽带进行修改联系电话号码

    Args:
        dirNum: 业务号码
        newTel: 新联系号码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "result": "1"  # 是否成功【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/sh_updateTel"
    data = {"dirNum": dirNum, "newTel": newTel, "callId": callId}
    return _make_request("POST", url, data=data)


def artificial(caller: str, routCode: str, callId: str) -> Dict[str, Any]:
    """
    上人工

    Args:
        caller: 主叫号码
        routCode: 人工编码
        callId: 通话流水号

    Returns:
        {
            "code": 200,
            "message": "SUCCESS",
            "data": {
                "result": "1"  # 是否成功【1是0否】
            }
        }
    """
    url = f"{BASE_URL}/artificial"
    data = {"caller": caller, "routCode": routCode, "callId": callId}
    return _make_request("POST", url, data=data)


def get_current_time() -> str:
    """
    获取当前时间，格式为 "yyyy-mm-dd hh:mm:ss"

    Returns:
        格式化后的时间字符串
    """
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def get_broadband_count(res: str or Dict) -> int:
    """
    获取宽带个数

    Args:
        res: 宽带列表数据（字符串或对象格式）

    Returns:
        宽带个数
    """
    try:
        if isinstance(res, str):
            res_obj = json.loads(res)
        else:
            res_obj = res
        
        broadband_list = res_obj.get("data", [])
        if isinstance(broadband_list, list):
            return len(broadband_list)
        return 0
    except Exception as e:
        print(f"处理数据出错：{e}")
        return 0


def check_address_similarity(res: str or Dict) -> Dict[str, Any]:
    """
    宽带地址是否相近

    Args:
        res: 宽带列表数据（字符串或对象格式）

    Returns:
        {
            "text_p": "格式化后的宽带信息文本",
            "is_exist": "1"  # 是否存在相近地址【1是0否】
        }
    """
    text = ""
    exist = "0"
    
    try:
        if isinstance(res, str):
            res_obj = json.loads(res)
        else:
            res_obj = res
        
        broadband_list = res_obj.get("data", [])
        
        if isinstance(broadband_list, list) and len(broadband_list) > 0:
            address_feature_set = set()
            has_same_address_feature = False
            broadband_texts = []
            
            for index, item in enumerate(broadband_list):
                idx = index + 1
                broadband_id = item.get("broadband_id", "")
                address = item.get("address", "")
                
                single_text = f"【宽带{idx}】账号：{broadband_id} | 地址：{address}"
                broadband_texts.append(single_text)
                
                if address:
                    addr_without_shanghai = address.replace("上海市", "")
                    import re
                    feature = re.match(r"^([^0-9]*)", addr_without_shanghai)
                    if feature:
                        feature = feature.group(1).strip()
                        if feature:
                            if feature in address_feature_set:
                                has_same_address_feature = True
                            else:
                                address_feature_set.add(feature)
            
            text = "\n".join(broadband_texts)
            exist = "1" if has_same_address_feature else "0"
    except Exception as e:
        print(f"处理数据出错：{e}")
    
    return {"text_p": text, "is_exist": exist}


def judge_phone_type(phone: str) -> Dict[str, Any]:
    """
    号码位数判断

    Args:
        phone: 号码

    Returns:
        {
            "type": "mobile",  # 号码类型【mobile-手机号，landline-固话，broadband-宽带号，invalid-无效号码】
            "length": 11
        }
    """
    phone_type = "invalid"
    length = 0
    
    if phone:
        import re
        phone_str = str(phone).strip()
        length = len(phone_str)
        
        if re.match(r"^1[3-9]\d{9}$", phone_str):
            phone_type = "mobile"
        elif re.match(r"^0\d{2,3}-?\d{7,8}$", phone_str):
            phone_type = "landline"
        elif re.match(r"^[A-Za-z]{2}\d{10}$", phone_str):
            phone_type = "broadband"
    
    return {"type": phone_type, "length": length}


if __name__ == "__main__":
    import sys
    
    print("Broadband API Client - 测试脚本")
    print("=" * 60)
    
    # 测试获取当前时间
    print("\n1. 测试获取当前时间:")
    print(f"   {get_current_time()}")
    
    # 测试号码类型判断
    test_phones = ["13812345678", "021-12345678", "AD1234567890", "12345"]
    print("\n2. 测试号码类型判断:")
    for phone in test_phones:
        result = judge_phone_type(phone)
        print(f"   {phone} -> type: {result['type']}, length: {result['length']}")
    
    # 测试宽带个数计算
    test_broadband_data = {
        "code": 200,
        "message": "SUCCESS",
        "data": [
            {"broadband_id": "AD0000604487", "address": "上海市浦东新区浦兴路街道平度路488弄4号7层703室"},
            {"broadband_id": "KD1128335698", "address": "上海市浦东新区浦兴路街道平度路488弄4号7层702室"}
        ]
    }
    print("\n3. 测试宽带个数计算:")
    count = get_broadband_count(test_broadband_data)
    print(f"   宽带个数: {count}")
    
    # 测试地址相似性判断
    print("\n4. 测试地址相似性判断:")
    result = check_address_similarity(test_broadband_data)
    print(f"   格式化文本:\n{result['text_p']}")
    print(f"   是否存在相近地址: {result['is_exist']}")
