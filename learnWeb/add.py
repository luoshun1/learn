# -*- coding:utf-8 -*-
import os,shutil
print("hahaha")

SOURCECHANNEL = 'D:\\work\\env1\\client\\AppPlay\\Proj.Android.Mini\\src\\org\\appplay\\platformsdk\\AdSDK.java'
TARGETCHANNELS = [	'Proj.Android.Mini18183',
	'Proj.Android.MiniDuoWan',
	'Proj.Android.MiniGGZS',
	'Proj.Android.MiniJieKu',
	'Proj.Android.MiniJinliYY',
	'Proj.Android.MiniJuFeng',
	'Proj.Android.MiniKubi',
	'Proj.Android.MiniLeiZheng',
	'Proj.Android.MiniNubia',
	'Proj.Android.MiniQingCheng',
	'Proj.Android.MiniQingNing',
	'Proj.Android.MiniSmartisan',
	'Proj.Android.MiniWuFan',
	'Proj.Android.MiniXianGuo',
	'Proj.Android.MiniYDMM',
	'Proj.Android.MiniYouFang',
	'Proj.Android.MiniYYH',
	'Proj.Android.MiniZhongXing',]
ROOTPATH = 'D:\\work\\env1\\client\\AppPlay'
TARGETFILE = 'src\\org\\appplay\\platformsdk\\AdSDK.java'

def deleteByTargetChannels(target):
	if os.path.isfile(target):
		os.remove(target)

def addByTargetChannels(srcfile, dstfile):
	print(srcfile, dstfile)
	shutil.copyfile(srcfile, dstfile)

def copyFileByTargetChannels(rootPath, channelList, target):
	for channel in channelList:
		tag1 = os.path.join(rootPath, channel, target)
		deleteByTargetChannels(tag1)
		# tag2 = os.path.split(tag1)[0]
		addByTargetChannels(SOURCECHANNEL, tag1)

copyFileByTargetChannels(ROOTPATH, TARGETCHANNELS, TARGETFILE)