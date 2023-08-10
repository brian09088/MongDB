![image](https://github.com/brian09088/MongoDB/assets/72643996/df8b2c44-e184-46cc-a802-dc2e3f962c91)# 安裝教學與基礎設定
主要在MongoDB 6.0版本上運行，社群基本版，下載封裝檔(.msi)
- 從(https://www.mongodb.com/try/download/community)  安裝下載
- 雲端數據資料庫(MongoDB Atlas)-免費試用版(512MB~5GB)
- 軟體與相關套件
  - MongoDB Compass (官方全功能開源管理工具)
  - Studio 3T
  - Nosql booster for mongodb
- 目前版本配置
  - MongoDB : 6.0.6
  - MongoDB Compass : 1.38.2
  - Mongosh:1.9.1)
------
## 在POSIX系統上安裝(Linux & Mac OS)
1. 建立目錄，變更使用者
```
$ mkdir –p /data/db
$ chown –R $USER:$USER /data/db
```
2. Mongo DB Download Center Try MongoDB Atlas Products | MongoDB 下載.tar.gz檔案
```
$ tar zxf mongodb-linux-x86_64-enterprise-rhe162-4.2.0.tgz
$ cd mongodb-linux-x86_64-enterprise-rhe162-4.2.0
$ bin/mongod
$ bin/mongod –dbpath ~/db
```
3. 使用mongod –dbpath.exe –help提示
------
## 在Windows系統上安裝
1. 可以在此編寫連線資訊(advanced connection options任何變更都會在url這裡呈現)
例如可以改變驗證機制或是建立安全連線等
![image](https://github.com/brian09088/MongoDB/assets/72643996/dc2f8127-7880-4c13-8b9d-cc7b571986b7)
2. localhost 預設本地端連線，只能從該電腦去做連線 (0.0.0.0為通用連線)
也可以從mongod.config文件中修改達成遠端連線，修改BIND-ip(預設127.0.0.1後面可新增其他ip)，修改後重新啟動才會生效，服務要關閉自動開啟，架設好之後便改成手動開啟避免自動關閉。
![image](https://github.com/brian09088/MongoDB/assets/72643996/01b521b4-bf08-42c4-b3f1-29dfbd862252)
![image](https://github.com/brian09088/MongoDB/assets/72643996/08f47789-d1b9-4b5c-800d-792359ec5b68)

<另解> 下指令:
```
mongod  --dbpath data/db --bind_ip_all
```
3. 建立服務:
CMD 輸入(根據你的config檔案位置):
```
mongod --config C:\Program Files\MongoDB\Server\6.0\bin\mongod.cfg -install
```
4. 啟動服務:
![image](https://github.com/brian09088/MongoDB/assets/72643996/ad638bf7-ab95-4b72-9fd7-b46358bea5c7)
- Windows搜尋服務
- 找到mongodb server
![image](https://github.com/brian09088/MongoDB/assets/72643996/b0e8812f-056a-4b7b-b32b-b75d10e6d509)
- 右鍵點選內容並啟動服務
![image](https://github.com/brian09088/MongoDB/assets/72643996/3e7bb2d2-e7b4-4f1d-ad6d-198bb21ba941)

5. 開啟連線方法:
- Cmd執行
```
mongodb  --dbpath data/db
```
- 另開cmd視窗執行
```
mongosh
```
- 開啟mongosh  輸入
```
mongodb://localhost:27017(開啟即會有提示)
```
<另解> 直接透過MongoDB Compass去連線
- *使用msi 封裝下載而不是使用7-zip 建議MongoDB 使用6.x.x以上
Install MongoDB Compass UI介面 1.38.2*

6. 當成功安裝後，可以在命令提示字元執行mongosh指令顯示連線資訊
並可以從測試區跳出test>
![image](https://github.com/brian09088/MongoDB/assets/72643996/8031bf9d-45a2-40c1-a437-b2af6fd9e11d)

7. 關閉連線:
```
 client.close() //關閉連線
```
- <直觀解法> MongoDB Compass : disconnect
![image](https://github.com/brian09088/MongoDB/assets/72643996/0964bc5c-216f-4f81-9c6c-48b853a1d748)

8. 停止伺服器:
```
(test> 游標出現後輸入) 
use admin
db.shutdownServer()
```
- 可執行指令(如ctrl+c, exit() ,quit 離開畫面)
如果直接關閉視窗或是關機重啟，會導致之後再也無法連接，將會需要重新安裝或是修理，所以務必小心

9. 修復(異常關閉、記憶體不足強制退出、執行連線中斷線等情形)
- 至msi封裝檔案(下載時的位置)點選開啟選擇next之後按下repair
![image](https://github.com/brian09088/MongoDB/assets/72643996/68fa77dc-0f3d-4c5c-a818-4358c6a031d9)





