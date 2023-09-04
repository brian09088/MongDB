import datetime as dt
import sqlalchemy #for panda + CX_ORacle
from sqlalchemy.exc import SQLAlchemyError
import cx_Oracle
import pandas as pd
import os
import socket
import pyodbc
import pymssql





class DB_Connection:
    UserName=''
    PassWord=''
    Database=''
    MSSQLDatabase=''

# attribute announce ways...
    def __inti__(self):
        self.UserName = ''
        self.PassWord = ''
        self.Database = ''
        self.MSSQLDatabase=''


    def as_dict(self):
        return {
                 'UserName':self.UserName
                ,'PassWord':self.PassWord
                ,'Database':self.Database
                ,'MSSQLDatabase':self.MSSQLDatabase
               }

class TXN_Message:
    ErrorMessage=''
    ErrorCode=''
    ProcessFunction=''
    State=''
    CurrentDataFlowName=''
    MachineName=socket.gethostname()
    IPAddress=socket.gethostbyname(socket.gethostname())
    Memo=''

    def ErrorPrintOut(self):  
        error_PrintOutMessage ="""
            CurrentDataFlowName: %s 
            State: %s 
            ProcessFunction :%s  
            ErrorMessage :%s
            MachineName :%s
            IPAddress :%s
            Memo:'%s'
            """%(self.CurrentDataFlowName,self.State,self.ProcessFunction,self.ErrorMessage,self.MachineName,self.IPAddress,self.Memo)      
        print(error_PrintOutMessage)

    def OKPrintOut(self):        
        print("CurrentDataFlowName: %s State: %s ProcessFunction %s"%(self.CurrentDataFlowName,self.State,self.ProcessFunction))
    def OKInit(self):      
            self.ErrorMessage=''
            self.ErrorCode=''  
            self.State='OK'
      
           
        
class DB_TXN_Adopter:   
    def QuicklyCleanDF(importDF):   
        importDF=importDF.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna(''))   
        return importDF 
    def GetOracle_DF(Auth:DB_Connection,SQL,txn_Message:TXN_Message):
        DataSet_DF=pd.DataFrame()
        txn_Message.ProcessFunction='GetOracle_DF'
        try:
            NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
            engine_ERP = sqlalchemy.create_engine("oracle+cx_oracle://"+Auth.UserName+":"+Auth.PassWord+"@" +Auth.Database)

            with engine_ERP.connect() as con:
                con.execute(NLS_LANG_TO_American)
                DataSet_DF= pd.read_sql(SQL, con)   
            txn_Message.OKInit()
            
          

        except SQLAlchemyError as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.ErrorPrintOut()
        #dataframe 做Insert 要做資料清洗...    
        DataSet_DF=DataSet_DF.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna(''))    
        # change columns upper for DB object usually is uppercase
        DataSet_DF.columns=[w.upper() for w in DataSet_DF] 
        return DataSet_DF
    def GetOracleWithInPolicy_DF(Auth:DB_Connection,SQL,SeesionOUID,txn_Message:TXN_Message):
        DataSet_DF=pd.DataFrame()
        txn_Message.ProcessFunction='GetOracle_DF'
        try:
            NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
            SessionPolicySQL="""begin APPS.MO_GLOBAL.SET_POLICY_CONTEXT('S', %s); end;"""%(SeesionOUID)
            engine_ERP = sqlalchemy.create_engine("oracle+cx_oracle://"+Auth.UserName+":"+Auth.PassWord+"@" +Auth.Database)

            with engine_ERP.connect() as con:
                con.execute(NLS_LANG_TO_American)
                con.execute(SessionPolicySQL)                                
                DataSet_DF= pd.read_sql(SQL, con)   
            txn_Message.OKInit()
            
          

        except SQLAlchemyError as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.ErrorPrintOut()
        #dataframe 做Insert 要做資料清洗...    
        DataSet_DF=DataSet_DF.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna(''))    
        # change columns upper for DB object usually is uppercase
        DataSet_DF.columns=[w.upper() for w in DataSet_DF] 
        return DataSet_DF

    def GetOracleWithInPolicyBug_DF(Auth:DB_Connection,SQL,SeesionOUID,txn_Message:TXN_Message):        
        DataSet_DF=pd.DataFrame()
        txn_Message.ProcessFunction='GetOracle_DF'        
        NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
        SessionPolicySQL="""begin APPS.MO_GLOBAL.SET_POLICY_CONTEXT('S', %s); end;"""%(SeesionOUID)
        engine_ERP = sqlalchemy.create_engine("oracle+cx_oracle://"+Auth.UserName+":"+Auth.PassWord+"@" +Auth.Database)
        with engine_ERP.connect() as con:
            con.execute(NLS_LANG_TO_American)
            con.execute(SessionPolicySQL)   
            #for used SET_POLICY_CONTEXT has some exception in first time query ,need hard pass with first query
            try:
                DataSet_DF= pd.read_sql(SQL, con)   
            except :
                #no meaning,just let code can compile pass
                a=1
            finally:
                try:
                    DataSet_DF= pd.read_sql(SQL, con) 
                    txn_Message.OKInit()
                except SQLAlchemyError as e:
                    txn_Message.ErrorMessage=e    
                    txn_Message.State='Fail'
                    txn_Message.ErrorPrintOut()
            

        #dataframe 做Insert 要做資料清洗...    
        DataSet_DF=DataSet_DF.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna(''))    
        # change columns upper for DB object usually is uppercase
        DataSet_DF.columns=[w.upper() for w in DataSet_DF] 
        return DataSet_DF

    def GetMSSQL_DF(Auth:DB_Connection,SQL,txn_Message:TXN_Message):
        DataSet_DF=pd.DataFrame()
        txn_Message.ProcessFunction='GetMSSQL_DF'
        try:
            #NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
            con = pymssql.connect(server =Auth.Database,database ="",  user=Auth.UserName,password =Auth.PassWord)
            DataSet_DF=pd.read_sql(SQL,con) 
            txn_Message.OKInit()            
          

        except SQLAlchemyError as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.ErrorPrintOut()
        #dataframe 做Insert 要做資料清洗...    
        DataSet_DF=DataSet_DF.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna(''))    
        # change columns upper for DB object usually is uppercase
        DataSet_DF.columns=[w.upper() for w in DataSet_DF] 
        return DataSet_DF   
        # https://dbrang.tistory.com/1236 for Dataframe to MSSQL

    def CallOracle_Procedure(Auth:DB_Connection,ProcName:str,ParaMeter:list,txn_Message:TXN_Message):
        NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
        txn_Message.ProcessFunction='CallOracle_Procedure'
        try:

            with cx_Oracle.connect(user=Auth.UserName, password=Auth.PassWord, dsn=Auth.Database) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(NLS_LANG_TO_American)
                    cursor.callproc(ProcName,ParaMeter)
                    connection.commit()              
                    txn_Message.OKInit()   

        except cx_Oracle.Error as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.ErrorPrintOut()
    def CallOracle_Function(Auth:DB_Connection,FunctionName:str,ParaMeter:list,ReturnType,txn_Message:TXN_Message):
        #https://cx-oracle.readthedocs.io/en/latest/api_manual/module.html#types ReturnType REF
        NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
        txn_Message.ProcessFunction='CallOracle_Function'
        try:

            with cx_Oracle.connect(user=Auth.UserName, password=Auth.PassWord, dsn=Auth.Database) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(NLS_LANG_TO_American)
                    returnValue=cursor.callfunc(FunctionName,ReturnType,ParaMeter)            
                    txn_Message.OKInit()
                    return returnValue   

        except cx_Oracle.Error  as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'  
            txn_Message.ErrorPrintOut()                          

    def QueryOracle_WithPureSQL(Auth:DB_Connection,SQL:str,txn_Message:TXN_Message):
        NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
        txn_Message.ProcessFunction='QueryOracle_WithPureSQL'
        try:

            with cx_Oracle.connect(user=Auth.UserName, password=Auth.PassWord, dsn=Auth.Database) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(NLS_LANG_TO_American)
                    cursor.execute(SQL)  
                    connection.commit()          
                    txn_Message.OKInit()   

        except cx_Oracle.Error as e:
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.Memo=SQL
            txn_Message.ErrorPrintOut()

    def BulkInsert(importDF,target_auth:DB_Connection,insert_SQL,txn_Message:TXN_Message):
        try:
            txn_Message.ProcessFunction='BulkInsert'
        # establish a new connection
            with cx_Oracle.connect(user=target_auth.UserName, password=target_auth.PassWord, dsn=target_auth.Database) as connection:
        # create a cursor
                with connection.cursor() as cursor:
            # execute the insert statement               
                #for index, row in stock_MaxDF1000.iterrows():
                    cursor.executemany(insert_SQL, importDF.values.tolist())                    
                # commit work  
                    connection.commit()
            
            txn_Message.OKInit()
            
       
        except cx_Oracle.Error as error:  
            error_obj, = error.args          
            txn_Message.ErrorCode=error_obj.code           
            txn_Message.ErrorMessage=error_obj.message                        
            txn_Message.State='Fail'
            txn_Message.Memo=insert_SQL
            txn_Message.ErrorPrintOut()
    
    def BulkInsertwithSlice(importDF,target_auth:DB_Connection,insert_SQL,txn_Message:TXN_Message,SliceSize):
        # 建議先用Bulkinsert確定無Oracle端錯誤後 ,在使用Bulkinsertkwith slice 不然無法偵錯
        txn_Message.ProcessFunction='BulkInsert'
        # recommend 10000
        try:
            countDF =len(importDF) 
            print("Count: %s"%(countDF))           
            sliceDF=pd.DataFrame()
            beginIndex=0
            EndingIndex=0
            PeriodCount=SliceSize
            while EndingIndex<=countDF:
                if EndingIndex+PeriodCount< countDF:
                    EndingIndex=EndingIndex+PeriodCount
                    sliceDF =importDF[beginIndex:EndingIndex]
                    DB_TXN_Adopter.BulkInsert(sliceDF,target_auth,insert_SQL,txn_Message)
                    beginIndex=EndingIndex
                else :        
                    sliceDF =importDF[EndingIndex:countDF]
                    DB_TXN_Adopter.BulkInsert(sliceDF,target_auth,insert_SQL,txn_Message)
                    EndingIndex=EndingIndex+PeriodCount
            txn_Message.OKInit()                    
                        
        except Exception as error:               
            txn_Message.State='Fail'
    #一個地雷 相對路徑/ 後面第一個字母命名不能叫r (/R)會被當特殊符號= = ..
    #SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
    #這Case需要在一開始Call function就補 r"\u" 都會錯誤..要先補R在你參數入參才能處理
    #正解 用這Function前面將R"" ex:ReadSQLByRelationPath(r"abc\rabc\DD.sql")
    def ReadSQLByRelationPath(SQLRelationPath):
        SQLPath=os.path.join(os.getcwd(),SQLRelationPath)
        query =open(SQLPath, 'r',encoding="utf-8")
        SQLtxt=query.read()
        return SQLtxt        
    def ReadInsertSQLframe(importTBName,importDF):
        DFcolumnrow=importDF.shape[1]
        DFlist=importDF.columns.tolist()
        valuearray=[]
        for valueloop in range(1,DFcolumnrow+1):
            vtostr=str(valueloop)
            vnewstr=":"+vtostr
            valuearray+=[vnewstr]  
        sqltxt="""INSERT INTO %s %s values %s"""%(importTBName,DFlist,valuearray)
        sqltxt=sqltxt.replace("'","")
        sqltxt=sqltxt.replace("]",")")
        sqltxt=sqltxt.replace("[","(")
        return sqltxt   

    def ReadInsertmssqlSQLframe(importTBName,importDF):
        DFcolumnrow=len(importDF.columns)
        sqltxt="""INSERT INTO [dbo].[%s]  VALUES ("""%(importTBName)
                  
        appendTxt="%s"
        for columns in range(1,DFcolumnrow):        
            appendTxt=appendTxt+", %s "
        sqltxt=sqltxt+appendTxt +")"
        return sqltxt  

    def MSSQLInsert(importDF,target_auth:DB_Connection,insert_SQL,txn_Message:TXN_Message): 
        
        txn_Message.ProcessFunction='MSSQLInsert' 
        try:
            #NLS_LANG_TO_American="""ALTER SESSION SET NLS_LANGUAGE= 'AMERICAN'""" #  這一定要下避免一下奇怪SP組Key issue 語系會有問題 乾
            con = pymssql.connect(server =target_auth.Database,database =target_auth.MSSQLDatabase,  user=target_auth.UserName,password =target_auth.PassWord)
            cur = con.cursor()            
            sql_data = tuple(map(tuple, importDF.values))  
            cur.executemany(insert_SQL, sql_data)          
            con.commit()
            cur.close()
            con.close()            
            txn_Message.OKInit()

        except pymssql.DatabaseError as e:
            
            txn_Message.ErrorMessage=e            
            txn_Message.State='Fail'
            txn_Message.ErrorPrintOut()
            