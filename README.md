# MongoDB
NoSQL database
- MongoDB 7.0以上版本，添加一個稱為可查詢加密（Queryable Encryption）功能，顧名思義，當MongoDB啟用Queryable Encryption功能，就能使加密資料不事先解密，就可以對其進行查詢。此項MongoDB內建加密功能，使組織能夠在資料受保護的情況下，查詢和使用敏感資料，在高度敏感的應用程式工作流程，諸如財務交易和分析醫療紀錄，降低資料外洩風險。
## 參考書籍
- GOTOP : MongoDB 5.x 實戰應用
- [Book Resource GitHub_link](https://github.com/kirkchu/mongodb)

## 先行準備
- 必須下載 : mongoDB shell
  1. 開啟CMD(記得cd變換路徑)
  2. 在設定安裝目錄中(ex我是在user/user下面)新建資料夾data下面建立資料庫名稱db
  ```
  mongod --dbpath data/db
  ```
  3. 可以開啟MongoDB主畫面進行操作
  4. 左側面板打開選取資料表，並進行建立等一系列操作
  5. 選擇connect可以使用，並且透過mongosh來做輸入
  
- 後續另開CMD操作mongosh程序
  1. 輸入並執行
  ```
  mongosh (enter)
  ```
  2. 顯示連接通道 : 預設port  27017
  3. 切換管理員模式
  ```
  use admin
  ```
  5. 關閉程序有以下3種，再用ctrl+c跳出階段步驟或是cls清空
  ```
  quit
  exit()
  ```
  6. 直接關掉可能會導致正在運行的部分程序損毀消失，所以不要直接按關閉視窗
