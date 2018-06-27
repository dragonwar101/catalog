from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create user
user1 = User(name="Owner", email="student@udacity.com",
             picture="""http://voice4thought.org/wp-content/uploads
/2016/08/default1.jpg""")
session.add(user1)
session.commit()

# Items for smartphones
category1 = Category(name="smartphones", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="samsung Galaxy S9", user_id=1, description="""Launch : 2017, September <-->
Platform: Android 8.0 (Oreo)<-->
Memory: 64/128/256 GB, 4 GB RAM <-->
PrimaryCamera: 12 MP (f/1.5-2.4, 26mm, 1/2.5", 1.4 , Dual Pixel PDAF)<-->
FrontCamera: 8 MP (f/1.7, 25mm, 1/3.6", 1.22 )<-->
Battery: Non-removable Li-Ion 3000 mAh battery (11.55 Wh)<-->
Features:Iris scanner, fingerprint (rear-mounted), accelerometer, gyro, proximity, compass, barometer, heart rate, SpO2""", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="apple iPhone X", user_id=1,  description="""Launch : 2017, September <-->
Platform: iOS 11.1.1 <-->
Memory: 64/256 GB, 3 GB RAM <-->
PrimaryCamera: Dual: 12 MP (f/1.8, 28mm) + 12 MP (f/2.4, 52mm) <-->
FrontCamera: 7 MP (f/2.2, 32mm) <-->
Battery: Non-removable Li-Ion 2716 mAh battery (10.35 Wh) <-->
Features: Face ID, accelerometer, gyro, proximity, compass, barometer""", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Huawei P20 Pro", user_id=1, description="""Launch : 2018, March <-->
Platform: Android 8.1 (Oreo) <-->
Memory: 128 GB, 6 GB RAM <-->
PrimaryCamera: Triple: 40 MP (f/1.8, 27 mm, 1/1.7", OIS) + 20 MP (f/1.6, 27 mm) + 8 MP (f/2.4, 80 mm) <-->
FrontCamera: 24 MP, f/2.0, 720p<-->
Battery: Non-removable Li-Po 4000 mAh battery <-->
Features:Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, color spectrum""", category=category1)

session.add(item3)
session.commit()

item4 = CategoryItem(name="Google Pixel 2", user_id=1, description="""Launch : 2017, October <-->
Platform: Android 8.0<-->
Memory: 64/128 GB, 4 GB RAM<-->
PrimaryCamera: 12.2 MP (f/1.8, 27mm, 1/2.6", 1.4 , Dual Pixel PDAF) <-->
FrontCamera: 8 MP (f/2.4, 27mm, 1/3.2", 1.4 ) <-->
Battery: Non-removable Li-Ion 2700 mAh battery <-->
Features: Fingerprint (rear-mounted), accelerometer, gyro, proximity, compass, barometer""", category=category1)

session.add(item4)
session.commit()

# Items for tablets
category2 = Category(name="tablets", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="""Huawei MediaPad T1 10""", user_id=1, description="""Launch : 2015, March <-->
DisplaySize : 9.6 inches <-->
DisplayRez: 800 x 1280 pixels 16:10 ratio <-->
Platform: Android 4.4.4 (KitKat) <-->
Memory: 8 GB, 1 GB RAM""", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="""Lenovo Yoga Tablet 10 HD+""", user_id=1,  description="""Launch : 2014, February <-->
DisplaySize : 10.1 inches <-->
DisplayRez: 1200 x 1920 pixels, 16:10 ratio <-->
Platform: Android 4.3 (Jelly Bean) <-->
Memory: 16/32 GB, 2 GB RAM""", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="""Samsung Galaxy Tab Pro 10.1""", user_id=1, description="""Launch : 2014, January <-->
DisplaySize : 10.1 inches <-->
DisplayRez: 2560 x 1600 pixels, 16:10 ratio <-->
Platform: Android 4.4 (KitKat) <-->
Memory: 16/32 GB, 2 GB RAM""", category=category2)

session.add(item3)
session.commit()

# Items for 
category3 = Category(name="Accessories", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Sony SmartWatch 3 SWR50", user_id=1, description="""Launch : 2014, February <-->
Build: Stainless Steel <-->
Resolution: 320 x 320 pixels <-->
Memory: 4 GB, 512 MB RAM <-->
Features: Accelerometer, gyro, compass <-->
Battery: Non-removable Li-Po 420 mAh battery""", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Samsung Gear S3 classic LTE", user_id=1, description="""Launch : 2017, March <-->
Build: Stainless Steel 316L <-->
Resolution: 360 x 360 pixels <-->
Memory: 4 GB, 768 MB RAM <-->
Features: Accelerometer, gyro, heart rate, barometer <-->
Battery: Non-removable Li-Ion 380 mAh battery""", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Apple Watch Series 3", user_id=1, description="""Launch : 2017, September<-->
Build: Stainless Steel/Ceramic back<-->
Resolution: 390 x 312 pixel<-->
Memory: 16 GB, 768 MB RAM<-->
Features: Accelerometer, gyro, heart rate, barometer<-->
Battery: Non-removable Li-Ion 279 mAh battery (1.07 Wh) - 38mm version""", category=category3)

session.add(item3)
session.commit()

# Items for 
category4 = Category(name="Normal phones", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Nokia 3310 4G", user_id=1, description="""Launch : 2018, January <-->
Resolution : 240 x 320 pixels <-->
PrimaryCamera : 2 MP, LED flash <-->
FrontCamera : NONE <-->
Features : StrongBody , SMS , some built-in games <-->
Battery: Removable Li-Ion 1200 mAh battery (BL-4UL)""", category=category4)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
