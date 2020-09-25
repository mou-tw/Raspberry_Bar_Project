'''
execute this python file by shell script daily, upload yesterday pictures to hdfs 
'''

import pyhdfs


client = pyhdfs.HdfsClient(hosts="10.120.26.200",user_name="spark")

# print (client.get_home_directory())
# print (client.listdir("/"))
# print (client.listdir("/Pi"))

file = os.listdir('./pic/')
for pic in file:
    client.copy_from_local("./pic/{}".format(pic),"/Pi/{}".format(pic))