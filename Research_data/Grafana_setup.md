# Grafana
- 視覺化網路應用程式平台
  - 下載: (https://grafana.com/grafana/download)
  - 安裝完成後，至browser http://localhost:3000 連接
  - 預設(account:admin/pw:admin)
  - 創建dashboard:
    - grafana metrics:
    - prometheus:
      - prometheus 2.0 stats
      - prometheus stats
      - kubernetes cluster (prometheus)
      - 前往官網開源的模板下載 [grafana dashboards](https://grafana.com/grafana/dashboards/?pg=hp&plcmt=lt-box-dashboards)
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/160f3fb7-58ca-4310-893c-ffca958734d7)
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/d93dfa31-e8bb-4160-ac0a-aa2718c5b0ac)
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/dbf4acd5-0287-4433-acb3-951a0af22e06)
      - 根據官網模板提供的id與json檔案來創建
  - 常見data source:
    - prometheus
      - 下載: (https://prometheus.io/download/)
      - 安裝完成後，在背景開啟服務，至browser http://localhost:9090 查看是否已經正確安裝
      - 確定連接成功後，至configuration -> data sources -> prometheus -> settings -> 輸入url : http://localhost:9090 -> save & test
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/45358fbe-3611-4d95-924f-28be7406461f)
    - influxDB
      - 下載: https://portal.influxdata.com/downloads/ https://docs.influxdata.com/influxdb/v2.7/install/?t=Windows
      - 安裝完成後，在背景開啟服務，至browser http://localhost:8086 查看是否已經正確安裝
      - 確定連接成功後，至configuration -> data sources -> influxDB -> settings -> 輸入url : http://localhost:8086 -> save & test
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/41d0bbcd-0ce3-439c-a46f-cb2ba605e4e8)
      - API tokens -> generate API token -> copy API code -> paste on
      - python3 influxDB 套件可以串接
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/d7134024-8701-405e-84a4-2a211ad05056)

      - ```
        import influxdb_client, os, time
        from influxdb_client import InfluxDBClient, Point, WritePrecision
        from influxdb_client.client.write_api import SYNCHRONOUS
        
        token = os.environ.get("INFLUXDB_TOKEN")
        org = "test"
        url = "http://localhost:8086"
        
        write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
        ```
      - ![image](https://github.com/brian09088/Grafana/assets/72643996/9cffa935-2f68-4374-b73f-4ca61e9919e3)
      - query language 由於版本關係，選擇flux而不是influxQL -> save & test
      - 試著連接telegraf去察看資源使用情形:
        - 安裝telegraf: https://github.com/influxdata/telegraf/releases
        - 至C:\Program Files 新建Telegraf 去把解壓縮之後的檔案複製過來
        - 在該根目錄下執行指令安裝服務
        ```
        telegraf.exe -service install
        ```
        - 去服務 -> Telegraf Data Collector Service -> 右鍵啟動服務
        - <另解>輸入指令啟動服務:
        ```
        net start telegraf
        ```
        - 目前卡關原因: 預設influxDB telegraf -> create configuration會跑出預設bucket並且可以選取system 來做系統監控(附圖為實際與比較差異)
        - ![image](https://github.com/brian09088/Grafana/assets/72643996/db29c756-c596-46f9-bf55-bc89467b44f7)
        - ![image](https://github.com/brian09088/Grafana/assets/72643996/1dc70676-a1ea-42ea-82bc-5a1b1fab2bd0)
    - loki
    - SQL
