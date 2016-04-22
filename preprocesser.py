#!/usr/bin/python

import xml.sax
import re
import time

def lp(content):
	#get links from text of page
	r=re.findall(r'\[\[(.+?)\]\]',content)
	#for loop removes links to files and links in the form of [[test|test page]]
	tmp = []
	for t in r:
		tmp2 = t.split("|")
		if not "File" in tmp2[0]: 
			tmp.append(tmp2[0].replace(" ","_"))
	return tmp

class pp(xml.sax.ContentHandler):
	def __init__(self):
		self.title_list = {}
		self.link_list = [] 
		self.title = ""
		self.count=0
		self.flagtitle = False
		self.flagcontent = False
		self.adfile = open('adlist.txt','w')
		self.content=""
		file1=open('simplewiki-20160305-all-titles','r')
		ind = 1
		for l in file1:
			self.title_list[l.strip().lower()] = ind
			ind+=1

	def startElement(self, name, attrs):
		#reads in the opening tag and sets flags for reading in stuff between tags
		#if title tag set title flag to true
		if name == "title":
			self.flagtitle = True
		#if text tag set content flag to true
		elif name == "text":
			self.flagcontent=True
	
	def endElement(self, name):
		#parse content, generate adjacency list, and reset everything
		if self.flagcontent:
			self.link_list=lp(self.content)
			print self.count
			self.count+=1
			for l in self.link_list:
				tmp = l.encode('ascii','ignore').lower() 
				tmp2 = self.title.encode('ascii','ignore').lower() 
				if tmp in self.title_list and tmp2 in self.title_list:
					self.adfile.write(str(self.title_list[tmp2]))
					self.adfile.write(" ")
					self.adfile.write(str(self.title_list[tmp]))
					self.adfile.write("\n")
			self.content=""
			self.link_list=[]
		self.flagtitle=False
		self.flagcontent=False

	def characters(self, content):
		#read in title if title tag
		if self.flagtitle:
			self.title=content
		#read in content if content tag
		elif self.flagcontent:
			self.content+=content

parser=xml.sax.make_parser()
parser.setContentHandler(pp())
parser.parse(open("simplewiki-20160305-pages-articles.xml","r"))
