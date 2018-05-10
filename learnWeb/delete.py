# -*- coding:utf-8 -*-
import os
print("hahah")

root_path = 'D:\work\env1\client\AppPlay'
fs = os.listdir(root_path)
for f1 in fs:
	print(f1)
	tag_path = os.path.join(root_path, f1, 'jni\Android.mk')
	if os.path.isfile(tag_path):
		os.remove(tag_path);
#test
# root_path = 'D:\myCode\\test\\test'
# fs = os.listdir(root_path)
# for f1 in fs:
# 	print(f1)
# 	tag_path = os.path.join(root_path, f1, 'jni\Android.mk')
# 	if os.path.isfile(tag_path):
# 		os.remove(tag_path)
		




# path = 'D:\work\env1\client\AppPlay'
# for dirpath,dirnames,filenames in os.walk(path):
# 	for file in filenames:
# 		fullpath=os.path.join(dirpath,file)
# 		print fullpath

# file_target = '../test/first.txt'
# code_target = 'int j = i'
# def target_lock():
# 	try:
# 		fp = open(file_target, 'rb')
# 		s = fp.read()
# 	finally:
# 		fp.close();
	
# 	re.match(r'int j = i', s)