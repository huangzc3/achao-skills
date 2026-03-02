# 关于宽带报障需要使用到的API说明

## 接口信息
1. 本地本网判断
   接口地址：http://127.0.0.1:8080/query_roam_is_telecom?deviceNum=&callId=
   请求方式：GET
   入参：
    - deviceNum：号码
    - callId：通话流水号

   出参：
    - isTelecom：是否本地本网 【0异网 1本网】

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"isTelecom":"1"}}
    ```

2. 非本网宽带信息获取
   接口地址：http://127.0.0.1:8080/get_broadband_list_by_dif_network?accNbr=&callId=
   请求方式：GET
   入参：
    - accNbr：号码
    - callId：通话流水号

   出参：
    - broadband_id：宽带账号
    - address：宽带地址

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

3. 根据手机/固话获取名下宽带信息
   接口地址：http://127.0.0.1:8080/get_broadband_list_by_accNbr?accNbr=&callId=
   请求方式：GET
   入参：
    - accNbr：号码
    - callId：通话流水号

   出参：
    - broadband_id：宽带账号
    - address：宽带地址

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

4. 根据身份证获取名下宽带信息
   接口地址：http://127.0.0.1:8080/get_broadband_list_by_id?id=&callId=
   请求方式：GET
   入参：
    - id：身份证
    - callId：通话流水号

   出参：
    - broadband_id：宽带账号
    - address：宽带地址

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

5. 根据宽带账号获取名下宽带信息
   接口地址：http://127.0.0.1:8080/getBroadbandListByDeviceNum?deviceNum=&callId=
   请求方式：GET
   入参：
    - deviceNum：宽带账号
    - callId：通话流水号

   出参：
    - broadband_id：宽带账号
    - address：宽带地址

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

6. 根据宽带账号查询属性是否属于校园网、政企、白金、欠费用户
   接口地址：http://127.0.0.1:8080/query_broadband_device_group?deviceNum=&callId=
   请求方式：GET
   入参：
    - deviceNum：宽带账号
    - callId：通话流水号

   出参：
    - isCampusNet：是否校园网【1是0否】
    - isEnterpriseGov：是否政企【1是0否】
    - isSpecialScene：是否白金【1是0否】
    - haveP6：是否在途【1是0否】
    - isHalt：是否欠费【1是0否】
    - routCode：人工编码

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"isCampusNet":"0","isEnterpriseGov":"0","isSpecialScene":"0","haveP6":"0","isHalt":"0","routCode":""}}
    ```

7. 根据宽带账号查询是否拥有在途订单
   接口地址：http://127.0.0.1:8080/sh_getP6ByDevice
   请求方式：POST
   入参：
    - accNbr：宽带账号
    - callId：通话流水号

   示例：
    ```json
    {"accNbr":"","callId":""}
    ```

   出参：
    - isFault：是否在途【0 无在途故障，1 有在途故障】

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"isFault":"0"}}
    ```

8. 根据宽带账号进行宽带诊断
   接口地址：http://127.0.0.1:8080/sh_testKD
   请求方式：POST
   入参：
    - deviceNum：宽带账号
    - callId：通话流水号

   示例：
    ```json
    {"deviceNum":"","callId":""}
    ```

   出参：
    - conId：结论id
    - conDesc：结论描述
    - testOk：测试是否正常 【0正常1需要派修-1测试失败】
    - advice：排障建议
    - dispatch：建议派单方向
    - isQZ：是否群障【1是0否】

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"conId":"118915","conDesc":"AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查","testOk":"0","conFileName":"112_testresult_nofault1.wav","advice":"AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查","dispatch":"区局（机房）","isHistoryTest":"0","isQZ":"0"}}
    ```

9. 对某个宽带进行重启
   接口地址：http://127.0.0.1:8080/sh_serverRestart
   请求方式：POST
   入参：
    - accNbr：业务号码
    - accType：业务类型 【0-移动，1-固话，2-宽带，3-IPTV】
    - callId：通话流水号

   示例：
    ```json
    {"accNbr":"","accType":"","callId":""}
    ```

   出参：
    - conId：结论id
    - conDesc：结论描述
    - testOk：测试是否正常 【0正常1需要派修-1测试失败】
    - advice：排障建议
    - dispatch：建议派单方向
    - isQZ：是否群障【1是0否】

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"conId":"118915","conDesc":"AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查","testOk":"0","conFileName":"112_testresult_nofault1.wav","advice":"AAA用户在线,排查无异常,请区局一键重启,如仍用户仍不好,请外线排查","dispatch":"区局（机房）","isHistoryTest":"0","isQZ":"0"}}
    ```

10. 对某个宽带进行派修
    接口地址：http://127.0.0.1:8080/appealinsys
    请求方式：POST
    入参：
    - startTime：派修时间
    - dirNum：主叫号码
    - tel：联系号码
    - callId：通话流水号

    示例：
    ```json
    {"dirNum":"","startTime":"","tel":"","callId":""}
    ```

    出参：
    - res：派修结果【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"res":"1"}}
    ```

11. 对某个宽带进行记录结案
    接口地址：http://127.0.0.1:8080/sh_recordFault_original
    请求方式：POST
    入参：
    - dirNum：设备号
    - tel：联系号码
    - caller：主叫号码
    - callId：通话流水号

    示例：
    ```json
    {"dirNum":"","tel":"","caller":"","callId":""}
    ```

    出参：
    - bookType：是否成功申告【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"bookType":"1"}}
    ```

12. 对某个宽带进行取消派修
    接口地址：http://127.0.0.1:8080/sh_cancelRepairRequest
    请求方式：POST
    入参：
    - accNbr：业务号码
    - callId：通话流水号

    示例：
    ```json
    {"accNbr":"","callId":""}
    ```

    出参：
    - result：是否成功【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"result":"1"}}
    ```

13. 对某个宽带进行改约
    接口地址：http://127.0.0.1:8080/change_broadband_appointment
    请求方式：POST
    入参：
    - dirNum：业务号码
    - begin：修改时间
    - callId：通话流水号

    示例：
    ```json
    {"dirNum":"","begin":"","callId":""}
    ```

    出参：
    - result：是否成功【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"result":"1"}}
    ```

14. 对某个宽带进行催修
    接口地址：http://127.0.0.1:8080/sh_urgentRepair
    请求方式：POST
    入参：
    - accNbr：业务号码
    - callId：通话流水号

    示例：
    ```json
    {"accNbr":"","callId":""}
    ```

    出参：
    - result：是否成功【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"result":"1"}}
    ```

15. 对某个宽带进行修改联系电话号码
    接口地址：http://127.0.0.1:8080/sh_updateTel
    请求方式：POST
    入参：
    - dirNum：业务号码
    - newTel：新联系号码
    - callId：通话流水号

    示例：
    ```json
    {"dirNum":"","newTel":"","callId":""}
    ```

    出参：
    - result：是否成功【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"result":"1"}}
    ```

16. 上人工
    接口地址：http://127.0.0.1:8080/artificial
    请求方式：POST
    入参：
    - caller：主叫号码
    - routCode：人工编码
    - callId：通话流水号

    示例：
    ```json
    {"caller":"","routCode":"","callId":""}
    ```

    出参：
    - result：是否成功【1是0否】

    示例：
    ```json
    {"code":200,"message":"SUCCESS","data":{"result":"1"}}
    ```

---

## 工具函数

1. 获取当前时间
   不需要调用接口，可以使用js获取当前时间格式为"yyyy-mm-dd hh:mm:ss"

   入参：无

   出参：
    - formatted_time：格式化后的时间字符串

   示例：
    ```json
    {"formatted_time": "2026-02-27 16:30:45"}
    ```

   示例代码：
   ```javascript
   function main() {
       const now = new Date();
       const year = now.getFullYear();
       const month = String(now.getMonth() + 1).padStart(2, '0');
       const day = String(now.getDate()).padStart(2, '0');
       const hours = String(now.getHours()).padStart(2, '0');
       const minutes = String(now.getMinutes()).padStart(2, '0');
       const seconds = String(now.getSeconds()).padStart(2, '0');
       const formattedTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;

       return {
           formatted_time: formattedTime
       };
   }
   ```

2. 获取宽带个数
   不需要调用接口，判断名下宽带接口个数

   入参：
    - res：宽带列表数据（字符串或对象格式）

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

   出参：
    - count：宽带个数

   示例：
    ```json
    {"count": 2}
    ```

   示例代码：
   ```javascript
   function main({res}) {
       let count = 0;

       try {
           const resObj = typeof res === 'string' ? JSON.parse(res) : res;
           const broadbandList = resObj?.data || [];

           if (Array.isArray(broadbandList)) {
               count = broadbandList.length;
           }
       } catch (error) {
           console.error("处理数据出错：", error);
       }

       return {
           count: count
       };
   }
   ```

3. 宽带地址是否相近
   不需要调用接口，使用js。

   入参：
    - res：宽带列表数据（字符串或对象格式）

   示例：
    ```json
    {"code":200,"message":"SUCCESS","data":[{"broadband_id":"AD0000604487","address":"上海市浦东新区浦兴路街道平度路488弄4号7层703室"},{"broadband_id":"KD1128335698","address":"上海市浦东新区浦兴路街道平度路488弄4号7层702室"}]}
    ```

   出参：
    - text_p：格式化后的宽带信息文本
    - is_exist：是否存在相近地址 【1是0否】

   示例代码：
   ```javascript
   function main({res}) {
       let text = "";
       let exist = "0";

       try {
           const resObj = typeof res === 'string' ? JSON.parse(res) : res;
           const broadbandList = resObj?.data || [];

           if (Array.isArray(broadbandList) && broadbandList.length > 0) {
               const addressFeatureSet = new Set();
               let hasSameAddressFeature = false;
               const broadbandTexts = [];

               broadbandList.forEach((item, index) => {
                   const idx = index + 1;
                   const broadbandId = item.broadband_id || "";
                   const address = item.address || "";

                   const singleText = `【宽带${idx}】账号：${broadbandId} | 地址：${address}`;
                   broadbandTexts.push(singleText);

                   if (address) {
                       const addrWithoutShanghai = address.replace("上海市", "");
                       const feature = addrWithoutShanghai.match(/^([^0-9]*)/)?.[1]?.trim() || "";
                       if (feature) {
                           if (addressFeatureSet.has(feature)) {
                               hasSameAddressFeature = true;
                           } else {
                               addressFeatureSet.add(feature);
                           }
                       }
                   }
               });

               text = broadbandTexts.join("\n");
               exist = hasSameAddressFeature ? "1" : "0";
           }
       } catch (error) {
           console.error("处理数据出错：", error);
       }

       return {
           text_p: text,
           is_exist: exist
       }
   }
   ```

 4. 号码位数判断
    不需要调用接口，使用js判断

    入参：
    - phone：号码

    示例：
    ```json
    {"phone": "13812345678"}
    ```

    出参：
    - type：号码类型 【mobile-手机号，landline-固话，broadband-宽带号，invalid-无效号码】
    - length：号码长度

    示例：
    ```json
    {"type": "mobile", "length": 11}
    ```

    示例代码：
   ```javascript
   function main({phone}) {
       let type = "invalid";
       let length = 0;

       if (phone) {
           const phoneStr = String(phone).trim();
           length = phoneStr.length;

           if (/^1[3-9]\d{9}$/.test(phoneStr)) {
               type = "mobile";
           } else if (/^0\d{2,3}-?\d{7,8}$/.test(phoneStr)) {
               type = "landline";
           } else if (/^[A-Za-z]{2}\d{10}$/.test(phoneStr)) {
               type = "broadband";
           }
       }

       return {
           type: type,
           length: length
       };
   }
   ```