import os
import time


# show raspberry temperature,CPU,memory


def getCPUtemp():
    temp = os.popen('vcgencmd measure_temp').readline()
    tempfloat = str(temp.replace('temp=', '').replace('\'C\n', ''))
    print('CPU Temperature is now %.1f Centigrade' % tempfloat)
    if tempfloat > 60:
        print('CPU Temperature is too high, pls cool it down')
    return tempfloat

# def getCPUusage():
#     #calculate CPU with two short time, time2 - time1
#     time1 = os.popen('cat /proc/stat').readline().split()[1:5]
#     time.sleep(0.2)
#     time2 = os.popen('cat /proc/stat').readline().split()[1:5]
#     deltaUsed = int(time2[0])-int(time1[0])+int(time2[2])-int(time1[2])
#     deltaTotal = deltaUsed + int(time2[3])-int(time1[3])
#     cpuUsage = float(deltaUsed)/float(deltaTotal)*100
# 	print('CPU Usage is now {}'.format(cpuUsage) +'%')


# def getRAM():
# 	#get RAM as list,list[7],[8],[9]:total,used,free
# 	RAM = os.popen('free').read().split()[7:10]
# 	#convert kb in Mb for readablility
# 	RAM0 = float(RAM[0])/1024
# 	print('RAM Total is %.1f MB' %RAM0)
# 	RAM1 = float(RAM[1])/1024
# 	percent = RAM1/RAM0*100
# 	print('RAM Used  is %.1f MB, %.2f' %(RAM1,percent) +'%')
# 	RAM2 = float(RAM[2])/1024
# 	print('RAM Free  is %.1f MB' %RAM2)


# def getDisk():
# 	#get Disk information,DISK[8],[9],[10],[11]:Size, Used. free, Used %
# 	DISK = os.popen('df -h /').read().split()[8:12]
# 	print('Disk total space is %s ' %DISK[0])
# 	print('Disk Used  space is %s ' %DISK[1] +'and is %s' %DISK[3])
# 	print('Disk Free  space is %s ' %DISK[2])


# while True:
# 	print ('\n-------------SysInfo-----------------\n')
# 	getCPUtemp()
# 	getCPUusage()
# 	getRAM()
# 	getDisk()
# 	print ('\n-------------------------------------\n')
# 	time.sleep(5)

if __name__ == "__main__":
    getCPUtemp()