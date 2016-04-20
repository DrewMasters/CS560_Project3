#!/usr/bin/python

import xml.sax

class pp(xml.sax.ContentHandler):
	def __init__(self):
		self.title_list = []
		file1=open('simplewiki-20160305-all-titles','r')
		for l in file1:
			self.title_list.append(l.rstrip())
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
		self.flagtitle=False
		self.flagcontent=False

	def characters(self, content):
		if self.flagtitle:
			self.title=content
			print self.title
		elif self.flagcontent:
			self.content=content
			print "content"



parser=xml.sax.make_parser()
parser.setContentHandler(pp())
parser.parse(open("simplewiki-20160305-pages-articles.xml","r"))
