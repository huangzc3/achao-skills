# Broadband API Reference

本文档提供所有宽带报障相关 API 的详细参考信息。

## API 基础信息

- **Base URL**: `http://127.0.0.1:8080`
- **请求格式**: JSON
- **响应格式**: JSON
- **通用参数**: 所有接口都需要 `callId` 参数（通话流水号）

## API 列表

### 1. 本地本网判断

**接口地址**: `/query_roam_is_telecom`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deviceNum | string | 是 | 号码 |
| callId | string | 是 | 通话流水号 |

**响应数据**:
```json
{
  "code": 200,
  "message": "SUCCESS",
  "data": {
    "isTelecom": "1"
  }
}
```

### 2. 非本网宽带信息获取

**接口地址**: `/get_broadband_list_by_dif_network`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| accNbr | string | 是 | 号码 |
| callId | string | 是 | 通话流水号 |

**响应数据**:
```json
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
```

### 3. 根据手机/固话获取名下宽带信息

**接口地址**: `/get_broadband_list_by_accNbr`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| accNbr | string | 是 | 号码 |
| callId | string | 是 | 通话流水号 |

### 4. 根据身份证获取名下宽带信息

**接口地址**: `/get_broadband_list_by_id`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | string | 是 | 身份证号 |
| callId | string | 是 | 通话流水号 |

### 5. 根据宽带账号获取名下宽带信息

**接口地址**: `/getBroadbandListByDeviceNum`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deviceNum | string | 是 | 宽带账号 |
| callId | string | 是 | 通话流水号 |

### 6. 根据宽带账号查询属性

**接口地址**: `/query_broadband_device_group`  
**请求方式**: GET

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deviceNum | string | 是 | 宽带账号 |
| callId | string | 是 | 通话流水号 |

**响应数据**:
```json
{
  "code": 200,
  "message": "SUCCESS",
  "data": {
    "isCampusNet": "0",
    "isEnterpriseGov": "0",
    "isSpecialScene": "0",
    "haveP6": "0",
    "isHalt": "0",
    "routCode": ""
  }
}
```

### 7. 根据宽带账号查询是否拥有在途订单

**接口地址**: `/sh_getP6ByDevice`  
**请求方式**: POST

**请求参数**:
```json
{
  "accNbr": "",
  "callId": ""
}
```

**响应数据**:
```json
{
  "code": 200,
  "message": "SUCCESS",
  "data": {
    "isFault": "0"
  }
}
```

### 8. 根据宽带账号进行宽带诊断

**接口地址**: `/sh_testKD`  
**请求方式**: POST

**请求参数**:
```json
{
  "deviceNum": "",
  "callId": ""
}
```

### 9. 对某个宽带进行重启

**接口地址**: `/sh_serverRestart`  
**请求方式**: POST

**请求参数**:
```json
{
  "accNbr": "",
  "accType": "",
  "callId": ""
}
```

accType 参数说明：0-移动，1-固话，2-宽带，3-IPTV

### 10. 对某个宽带进行派修

**接口地址**: `/appealinsys`  
**请求方式**: POST

**请求参数**:
```json
{
  "startTime": "",
  "dirNum": "",
  "tel": "",
  "callId": ""
}
```

### 11. 对某个宽带进行记录结案

**接口地址**: `/sh_recordFault_original`  
**请求方式**: POST

**请求参数**:
```json
{
  "dirNum": "",
  "tel": "",
  "caller": "",
  "callId": ""
}
```

### 12. 对某个宽带进行取消派修

**接口地址**: `/sh_cancelRepairRequest`  
**请求方式**: POST

**请求参数**:
```json
{
  "accNbr": "",
  "callId": ""
}
```

### 13. 对某个宽带进行改约

**接口地址**: `/change_broadband_appointment`  
**请求方式**: POST

**请求参数**:
```json
{
  "dirNum": "",
  "begin": "",
  "callId": ""
}
```

### 14. 对某个宽带进行催修

**接口地址**: `/sh_urgentRepair`  
**请求方式**: POST

**请求参数**:
```json
{
  "accNbr": "",
  "callId": ""
}
```

### 15. 对某个宽带进行修改联系电话号码

**接口地址**: `/sh_updateTel`  
**请求方式**: POST

**请求参数**:
```json
{
  "dirNum": "",
  "newTel": "",
  "callId": ""
}
```

### 16. 上人工

**接口地址**: `/artificial`  
**请求方式**: POST

**请求参数**:
```json
{
  "caller": "",
  "routCode": "",
  "callId": ""
}
```

## 工具函数

Python 脚本 `broadband_api.py` 提供以下工具函数：

- `get_current_time()` - 获取当前时间，格式为 "yyyy-mm-dd hh:mm:ss"
- `get_broadband_count(res)` - 获取宽带个数
- `check_address_similarity(res)` - 宽带地址是否相近
- `judge_phone_type(phone)` - 号码位数判断

号码类型返回值：
- `mobile` - 手机号
- `landline` - 固话
- `broadband` - 宽带号
- `invalid` - 无效号码
