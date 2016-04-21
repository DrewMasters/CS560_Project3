#!/usr/bin/python

import xml.sax
import re

def lp(content):
	#get links from text of page
	return re.findall(	
	

class pp(xml.sax.ContentHandler):
	def __init__(self):
		self.title_list = {}
		self.link_list = {}
		self.title_count = 0
		self.title = ""
		self.flagtitle = False
		self.flagcontent = False
		self.number = 0
		self.adfile = open('adlist.txt','w')
		self.content=""

	def startElement(self, name, attrs):
		if name == "title":
			self.flagtitle = True
		elif name == "text":
			self.flagcontent=True
	
	def endElement(self, name):
		self.link_list[self.title]=lp(self.content)
		self.flagtitle=False
		self.flagcontent=False
		self.content=""

	def characters(self, content):
		if self.flagtitle:
			self.title=content
			self.title_list[self.title]=self.title_count
			self.link_list[self.title]=[]
			self.title_count+=self.title_count
			print self.title
		elif self.flagcontent:
			self.content+=content
	
	def endDocument():
		#generate adjacency list
		print "finished document"

parser=xml.sax.make_parser()
parser.setContentHandler(pp())
parser.parse(open("simplewiki-20160305-pages-articles.xml","r"))
