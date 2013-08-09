#!/usr/bin/env python

import sublime, sublime_plugin, socket, re,subprocess,os

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
	path1 = os.path.join('MarkdownLive','app.js')
	path2 = os.path.join(sublime.packages_path(),path1)
	print("MarkdownLive: "+path2)
	cmd = ['node', path2]
	p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=False)

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
		print("MarkdownLive: "+'and Launching: node')
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

class MyEventListenerssd3(sublime_plugin.EventListener):
	def on_clone_async(self,view):
		if md(view):
			tcp(view)

class MyEventListener4(sublime_plugin.EventListener):
	def on_activated_async(self,view):
		if md(view):
			tcp(view)	