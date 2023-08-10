## 基本查詢、插入、刪除指令
- 查詢所有資料
```
Db.collection.find()
```
- 只回傳第一筆資料
```
Db.collection.find_one()
```
- 插入資料
```
db.collection.insert_one()
db.collection.insert_many()
```
- 取代資料
```
db.collection.replace_one()
```
- 更新資料
```
db.collection.update_one()
db.collection.update_many()
```
- 刪除資料
```
db.collection.delete_one()
db.collection.delete_many()
```
## Aggregation 進階查詢
- $addFields(新增欄位)
- $group(群組運算)
- $project(欄位顯示處理)
- $sort(排序)
- $bucket(桶型計算-資料按照特定範圍進行群組)
- $lookup(外部尋找)
- $match(設定查詢條件)
- $redact(文件修訂)
- $out(輸出到資料表)
- $unionWith(與其他資料結合)
- $unwind(陣列解構)




















