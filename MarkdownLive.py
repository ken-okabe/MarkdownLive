#!/usr/bin/env python

import sublime, sublime_plugin, socket, re,subprocess,os,sys

print("MarkdownLive: Initiated..")

def md(view):
	try:
	      return bool(re.search('.+\.md$|.+\.markdown$|.+\.mdown$|.+\.mkdn$|.+\.mkd$|.+\.mdwn$|.+\.mdtxt$|.+\.mdtext$|.+\.text$|.+\.txt$', view.file_name()))
	except:
		return False;

def tcp(view):
	TCP_IP = '127.0.0.1'
	TCP_PORT = 9998 
	MESSAGE = view.substr(sublime.Region(0, view.size()))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE.encode()) 
	s.close()

def nodeApp():
	appFile = os.path.join('MarkdownLive','app.js')
	appPath = os.path.join(sublime.packages_path(),appFile)

	try:
		print("MarkdownLive: node "+appPath)
		p = subprocess.Popen(['node', appPath],
	            shell=False,
	                            stdout=subprocess.PIPE,
	                            stderr=subprocess.PIPE,
	                            )
	except:
		from os.path import expanduser
		home = expanduser("~")
		path1 = os.path.join('MarkdownLive','nodePath.cfg')
		path2 = os.path.join(sublime.packages_path(),path1)
		context = open(path2, "rt")
		nodePath = os.path.join(home,context.read())
		context.close()

		print("MarkdownLive: "+nodePath+" "+appPath)
		p = subprocess.Popen([nodePath, appPath],
	            shell=False,
	                            stdout=subprocess.PIPE,
	                            stderr=subprocess.PIPE,
	                            )
        
def reloadServer():
	TCP_IP = '127.0.0.1'
	TCP_PORT = 9998 
	MESSAGE = 'shutdown'
	try:
		print("MarkdownLive: "+'trying node Server shutdown');
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(MESSAGE.encode()) 
		s.close()
		print("MarkdownLive: "+'found the server listening and quit; Launching: node')
		nodeApp()
	except:
		print("MarkdownLive: "+'error no Server and Launching: node')
		nodeApp()

	print("MarkdownLive: "+"Ready.")

def plugin_loaded():
	reloadServer()

class MarkdownLiveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		reloadServer()

class MyEventListener1(sublime_plugin.EventListener):
	def on_modified_async(self,view):
		if md(view):
			tcp(view)
 
class MyEventListener2(sublime_plugin.EventListener):
	def on_load_async(self,view):
		if md(view):
			tcp(view)

class MyEventListener3(sublime_plugin.EventListener):
	def on_clone_async(self,view):
		if md(view):
			tcp(view)

class MyEventListener4(sublime_plugin.EventListener):
	def on_activated_async(self,view):
		if md(view):
			tcp(view)	