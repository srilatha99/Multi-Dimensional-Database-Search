import graphene
import mysql.connector as mysql
class collegefacttable(graphene.ObjectType):
    name = graphene.String()
    url = graphene.String()
    publicOrPrivate=graphene.Int()
    region=graphene.List(graphene.Int)
    state=graphene.List(graphene.Int)
    focus=graphene.List(graphene.Int)
    collegeType=graphene.List(graphene.Int)
    setting=graphene.List(graphene.Int)
    collegeSize=graphene.Int()
    SATAvg=graphene.Int()
    collegeRanking=graphene.Int()
    sportsTradition=graphene.Int()
    studentFacultyRatio=graphene.Int()
    cost=graphene.Int()
    collegeAge=graphene.Int()
class user(graphene.ObjectType):
    userid=graphene.String()
class userbookmark(graphene.ObjectType):
    userid=graphene.String()
    domainName=graphene.String()
    bname=graphene.String()
    bookmark=graphene.String()
class autofacttable(graphene.ObjectType):
    autoId = graphene.String()
    url = graphene.String()
    color=graphene.Int()
    age=graphene.Int()
    fuelType=graphene.Int()
    make=graphene.Int()
    bodyStyle=graphene.Int()
    luxurySeats=graphene.Int()
    mileage=graphene.Int()
    priceRange=graphene.Int()
    sellerType=graphene.Int()
    sunroof=graphene.Int()
    transmission=graphene.Int()
    usedOrNew=graphene.Int()
class domain(graphene.ObjectType):
    domainName = graphene.String()
    facttablename = graphene.String()
class property(graphene.ObjectType):
    domainName=graphene.String()
    propertyName = graphene.String()
    propertyQuestion = graphene.String()
    displayOrder = graphene.String()
    propertyDisplayType = graphene.String()
'''lass propertyDetail(graphene.ObjectType):
    domainName=graphene.String()
    propertyName = graphene.String()
    allowedValue = graphene.String()
    allowedValueCode = graphene.String()'''
class propertyDetail1(graphene.ObjectType):
    domainName=graphene.String()
    propertyName = graphene.String()
    propertyQuestion = graphene.String()
    displayOrder = graphene.String()
    propertyDisplayType = graphene.String()
    allowedValue = graphene.String()
    allowedValueCode = graphene.String()

    

class Queries(graphene.ObjectType):
    domain = graphene.List(domain)  
    property = graphene.List(property)
    autofacttable = graphene.List(autofacttable,color=graphene.Int(),age=graphene.Int(),bodyStyle=graphene.List(graphene.Int),make=graphene.List(graphene.Int),fuelType=graphene.List(graphene.Int),luxurySeats=graphene.Int(),mileage=graphene.Int(),priceRange=graphene.Int(),sellerType=graphene.Int(),sunroof=graphene.Int(),transmission=graphene.Int(),usedOrNew=graphene.List(graphene.Int))
    #propertyDetail=graphene.List(propertyDetail)
    collegefacttable = graphene.List(collegefacttable,publicOrPrivate=graphene.Int(),region=graphene.List(graphene.Int),state=graphene.List(graphene.Int),focus=graphene.List(graphene.Int),collegeType=graphene.List(graphene.Int),setting=graphene.List(graphene.Int),collegeSize=graphene.Int(),SATAvg=graphene.Int(),collegeRanking=graphene.Int(),sportsTradition=graphene.Int(),studentFacultyRatio=graphene.Int(),cost=graphene.Int(),collegeAge=graphene.Int())
    propertyDetail1=graphene.List(propertyDetail1)
    userbookmark=graphene.List(userbookmark,userid=graphene.String())
    #tablefilter=graphene.List(tablefilter)
    #url1= graphene.Field(collegefacttable) 
    print("Test Queries")
    def resolve_domain(self, info):
        print("Test")
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )        
        query = "select domainName,facttablename from domain"
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(domain(domainName=record[0], facttablename=record[1]))
            print(record)
        return buildings
    '''def resolve_property(self,info):
        print("Test")
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )        
        query = "select domainName,propertyName,propertyQuestion,displayOrder,propertyDisplayType from property"
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(property(domainName=record[0],propertyName=record[1],propertyQuestion=record[2], displayOrder=record[3],propertyDisplayType=record[4]))
            print(record)
        return buildings
    def resolve_propertyDetail(self,info):
        print("Test")
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )        
        query = "select pTable.domainName, pTable.propertyName, pTable.propertyQuestion, pTable.propertyDisplayType, pTable.displayOrder,  group_concat(pdTable.allowedValueCode SEPARATOR '*'),group_concat(pdTable.allowedValue SEPARATOR '*') from property as pTable ,propertydetail as pdTable where pTable.domainName = pdTable.domainName and pTable.propertyName = pdTable.propertyName group by pTable.domainName, pTable.propertyQuestion, pTable.propertyDisplayType, pTable.propertyname, pTable.displayOrder order by pTable.displayOrder ASC;"
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print(records[0])
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(propertyDetail1(domainName=record[0],propertyName=record[1],propertyQuestion=record[2],propertyDisplayType=record[3],displayOrder=record[4],allowedValueCode=record[6],allowedValue=record[5]))
            print(record)
        return buildings'''
    def resolve_autofacttable(self,info,color,age,fuelType,make,bodyStyle,luxurySeats,mileage,priceRange,sellerType,sunroof,transmission,usedOrNew):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        ) 
        flag=0
        print("color")
        print(color,age,fuelType,bodyStyle)
        l1=[color,age,luxurySeats,mileage,priceRange,sellerType,sunroof,transmission]
        l2=['color','age','luxurySeats','mileage','priceRange','sellerType','sunroof','transmission']
        l3=[]
        l4=[]
        for i in range(0,len(l1)):
            if(l1[i]>0):
                l3.append(l1[i])
                l4.append(l2[i])
        
        query = "select autoId,url from autofacttable where "
        for i in range(0,len(l3)):
            query=query +l4[i]+" = "+str(l3[i])
            if(i!=len(l3)-1):
                query+=" AND "
    
        
        #query = query + "color="+str(color)+ " AND age="+str(age)+" AND luxuryseats="+str(luxuryseats)+" AND mileage="+str(mileage) +"AND sellerType="+str(sellerType)+" AND sunroof="+str(sunroof)+"AND transmission="+str(transmission)
        if(len(bodyStyle)!=0):
            flag=1
            l=[]
            query=query+" AND bodyStyle IN ( "
            for i in range(0,len(bodyStyle)):
                query=query+str(bodyStyle[i])+ " ) " if i==len(bodyStyle)-1 else query+str(bodyStyle[i])+ " , "
        if(len(fuelType)!=0):
             flag=1
             l=[]
             query=query+" AND fuelType IN ( "
             for i in range(0,len(fuelType)):
                 query= query+str(fuelType[i])+ " ) " if i==len(fuelType)-1 else query+str(fuelType[i])+ " , "
        if(len(make)!=0):
             l=[]
             flag=1
             query=query+" AND make IN ("
             for i in range(0,len(make)):
                query= query+str(make[i])+ " ) " if i==len(make)-1 else query+str(make[i])+ " , "
        if(len(usedOrNew)!=0):
             l=[]
             flag=1
             query=query+" AND usedOrNew IN ("
             for i in range(0,len(usedOrNew)):
                query= query+str(usedOrNew[i])+ " ) " if i==len(usedOrNew)-1 else query+str(usedOrNew[i])+ " , "
        print(query)
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(autofacttable(autoId=record[0],url=record[1]))
            print(record)
        return buildings
    def resolve_collegefacttable(self,info,publicOrPrivate,region,state,focus,collegeType,setting,collegeSize,SATAvg,collegeRanking,sportsTradition,studentFacultyRatio,cost,collegeAge):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        ) 
        flag=0
        #print("color")
        #print(color,age,fuelType,bodyStyle)
        l1=[publicOrPrivate,collegeSize,SATAvg,collegeRanking,sportsTradition,studentFacultyRatio,cost,collegeAge]
        l2=['publicOrPrivate','collegeSize','SATAvg','collegeRanking','sportsTradition','studentFacultyRatio','cost','collegeAge']
        l3=[]
        l4=[]
        for i in range(0,len(l1)):
            if(l1[i]>0):
                l3.append(l1[i])
                l4.append(l2[i])
        
        query = "select name,url from collegefacttable where "
        for i in range(0,len(l3)):
            query=query +l4[i]+" = "+str(l3[i])
            if(i!=len(l3)-1):
                query+=" AND "
        if(len(region)!=0):
            flag=1
            l=[]
            query=query+" AND region IN ( "
            for i in range(0,len(region)):
                query=query+str(region[i])+ " ) " if i==len(region)-1 else query+str(region[i])+ " , "
        if(len(state)!=0):
             flag=1
             l=[]
             query=query+" AND state IN ( "
             for i in range(0,len(state)):
                 query= query+str(state[i])+ " ) " if i==len(state)-1 else query+str(state[i])+ " , "
        if(len(focus)!=0):
             l=[]
             flag=1
             query=query+" AND focus IN ("
             for i in range(0,len(focus)):
                query= query+str(focus[i])+ " ) " if i==len(focus)-1 else query+str(focus[i])+ " , "
        if(len(collegeType)!=0):
             l=[]
             flag=1
             query=query+" AND collegeType IN ("
             for i in range(0,len(collegeType)):
                query= query+str(collegeType[i])+ " ) " if i==len(collegeType)-1 else query+str(collegeType[i])+ " , "
        if(len(setting)!=0):
             l=[]
             flag=1
             query=query+" AND setting IN ("
             for i in range(0,len(setting)):
                query= query+str(setting[i])+ " ) " if i==len(setting)-1 else query+str(setting[i])+ " , "
        print(query)
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(collegefacttable(name=record[0],url=record[1]))
            print(record)
        return buildings
    def resolve_propertyDetail1(self,info):
        print("Test")
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )        
        query = "select pTable.domainName, pTable.propertyName, pTable.propertyQuestion, pTable.propertyDisplayType, pTable.displayOrder,  group_concat(pdTable.allowedValueCode SEPARATOR '*'),group_concat(pdTable.allowedValue SEPARATOR '*') from property as pTable ,propertydetail as pdTable where pTable.domainName = pdTable.domainName and pTable.propertyName = pdTable.propertyName group by pTable.domainName, pTable.propertyQuestion, pTable.propertyDisplayType, pTable.propertyname, pTable.displayOrder order by pTable.displayOrder ASC;"
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print(records[0])
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(propertyDetail1(domainName=record[0],propertyName=record[1],propertyQuestion=record[2],propertyDisplayType=record[3],displayOrder=record[4],allowedValueCode=record[5],allowedValue=record[6]))
            #print(record)
        return buildings
    def resolve_userbookmark(self, info,userid):
        print("Test")
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )        
        query = "select bname,domainName from userbookmark where userid = '"+userid+"'"
        print(query)
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        buildings = []
        for record in records:
            buildings.append(userbookmark(bname=record[0],domainName=record[1]))
            print(record)
        return buildings

class createUser(graphene.Mutation):
    # define output of mutation here
    userid = graphene.String()
    # define data to be sent to server as part of insert
    class Arguments:
        userid = graphene.String()
    # code to modify database
    def mutate(self, info, userid):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )
        query = "insert into user values ('"+userid+"')"
        print(query)
        cursor = db.cursor()
        try:
            cursor.execute(query)
            db.commit()
            print(query)
            cursor.close()
            db.close()
            return createUser(userid=userid)
        except Exception as e:
            #print(sql)
            #print(e)
            db.rollback()
            cursor.close()
            db.close()
            return createUser(userid="")
class createUserbookmark(graphene.Mutation):
    # define output of mutation here
    userid = graphene.String()
    domainName = graphene.String()
    bname = graphene.String()
    bookmark = graphene.String()
    # define data to be sent to server as part of insert
    class Arguments:
        userid = graphene.String()
        domainName = graphene.String()
        bname = graphene.String()
        bookmark = graphene.String()
    # code to modify database
    def mutate(self, info, userid,domainName,bname,bookmark):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )
        query = "insert into userbookmark values ('"+userid+"','"+domainName+"','"+bname+"','"+bookmark+"')"
        print(query)
        cursor = db.cursor()
        try:
            cursor.execute(query)
            db.commit()
            print(query)
            cursor.close()
            db.close()
            return createUserbookmark(userid=userid,domainName=domainName,bname=bname,bookmark=bookmark)
        except Exception as e:
            db.rollback()
            cursor.close()
            db.close()
            return createUser(userid="",domainName="",bname="",bookmark="")
class deleteUser(graphene.Mutation):
    # define output of mutation here
    userid = graphene.String()
    # define data to be sent to server as part of insert
    class Arguments:
        userid = graphene.String()
    # code to modify database
    def mutate(self, info, userid):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )
        query = "delete from user "+" where userid = '"+userid+"'"
        print(query)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        print(query)
        cursor.close()
        db.close()
        return deleteUser(userid=userid)
class deleteUserbookmark(graphene.Mutation):
    # define output of mutation here
    userid = graphene.String()
    bname=graphene.String()
    domainName=graphene.String()
    # define data to be sent to server as part of insert
    class Arguments:
        userid = graphene.String()
        bname=graphene.String()
        domainName=graphene.String()
    # code to modify database
    def mutate(self, info, userid,bname,domainName):
        db = mysql.connect(
            host="localhost",
            database="test_db",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password'
        )
        query = "delete from userbookmark "+" where userid = '"+userid+"' and bname = '"+bname+"' and domainName = '"+domainName+"'"
        print(query)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        print(query)
        cursor.close()
        db.close()
        return deleteUserbookmark(userid=userid,bname=bname,domainName=domainName)


class Mutations(graphene.ObjectType):
    create_user = createUser.Field()
    create_userbookmark = createUserbookmark.Field()
    delete_user = deleteUser.Field()
    delete_userbookmark=deleteUserbookmark.Field()

schema1 = graphene.Schema(query = Queries,mutation=Mutations)
result = schema1.execute(Queries,Mutations)
#print(result)
print("Test File")