# 安裝教學與基礎設定
主要在MongoDB 6.0版本上運行，社群基本版(.msi)
雲端數據資料庫(MongoDB Atlas)-免費試用版(512MB~5GB)
- 可配合安裝幾個軟體
  - MongoDB Compass
  - Studio 3T
  - Nosql booster for mongodb
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
1.	可以在此編寫連線資訊(advanced connection options任何變更都會在url這裡呈現)
例如可以改變驗證機制或是建立安全連線等
![image](https://github.com/brian09088/MongoDB/assets/72643996/49d3f390-2b8a-4b2b-ba1f-e90e51b043b2)

