# MongoDB
NoSQL database

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
