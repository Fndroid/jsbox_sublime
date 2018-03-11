import json
import sublime
import sublime_plugin
import urllib
import os
import requests
import re
import shutil

SETTINGS_FILE = 'Jsbox.sublime-settings'


class JsboxsyncfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings(SETTINGS_FILE)
		host = settings.get('host')

		file_name = os.path.abspath(self.view.file_name())
		directory = os.path.dirname(file_name)

		is_package = False
		# print(directory)
		while directory:
			print(directory)
			needed_files = ['assets', 'scripts', 'strings', 'config.json', 'main.js']
			directory_files = os.listdir(directory)
			legal_dir = all([i in directory_files for i in needed_files])
			if legal_dir or os.path.dirname(directory) == directory:
				is_package = legal_dir
				break
			directory = os.path.dirname(directory)

		print("是否安装包:{}".format(is_package))

		if is_package:
			output_path = os.path.join(directory, '.output')
			if not os.path.exists(output_path):
				os.mkdir(output_path)
			zipfile_name = os.path.basename(directory)
			print("目录名称: {}, 文件名: {}".format(output_path, directory))
			file_name = shutil.make_archive(os.path.join(output_path, "shuangpin"), 'zip', root_dir=directory, base_dir=None)
			print("压缩文件名: {}".format(file_name))
			# file_name = name

		def upload():
			url = 'http://{}/upload'.format(host)
			files = {'files[]': open(file_name, 'rb')}
			r = requests.post(url, files=files)
			print(r.status_code)
			if r.status_code != 200:
				sublime.error_message('fail')
		sublime.set_timeout_async(upload, 0)

class JsboxdownloadfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		new_file = window.new_file()
		settings = sublime.load_settings(SETTINGS_FILE)
		host = settings.get('host')
		url = 'http://{}/list?path=/'.format(host)
		resp = requests.get(url)
		resp.encoding = 'utf-8'
		scripts = resp.json()
		# print(map(lambda x: x['name'], resp.json()))
		def load(x):
			downloadurl = 'http://{}/download?path={}'.format(host, scripts[x]['path'])
			resp2 = requests.get(downloadurl)
			resp2.encoding = 'utf-8'
			new_file.insert(edit, 0, resp2.text)
			new_file.set_name(scripts[x]['name'])
			new_file.set_line_endings('Unix')
		new_file.show_popup_menu(list(map(lambda x: x['name'], scripts)), load)


class JsboxEventListener(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		filename = view.file_name()
		# print(os.path.basename(filename))
		if filename.endswith('.js') or filename.endswith('.json'):
			# print('文件以js或json结尾')
			view.run_command('jsboxsyncfile')
