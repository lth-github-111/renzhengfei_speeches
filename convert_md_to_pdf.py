# -*- coding: utf-8 -*

# author     ：lth
# date       : 2019-09-01
# description：将 md 文件转为 pdf

from pathlib import Path
import os
import pdfkit
import sys
import time

html_template = """
<!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
</head> 
<body> 
{content} 
</body> 
</html> 
"""

g_work_path = r'D:\Users\xxx\Downloads\renzhengfei-master' #所下载的 md 文件夹路径
g_output_html_dir = '\output_html'
g_output_pdf_dir  = '\output_pdf'

# md 文件转换 html
def convert_to_file_html(md_file_name):
	if md_file_name.endswith('.md'):
		pdf_file_name = md_file_name.replace('.md', '.html')
		pdf_file_name = pdf_file_name.replace(g_work_path, g_work_path + g_output_html_dir)
		
		#创建目录
		tmp_path = os.path.dirname(pdf_file_name)
		if not os.path.exists(tmp_path):
			os.makedirs(tmp_path)
		
		print("1:", pdf_file_name)
		cmd = "pandoc " + md_file_name + " -o " + pdf_file_name #我的微云盘上上有 pandoc 安装包
		os.system(cmd)

# 将指定目录下所有 md 文件转换 html（包含子目录）
def convert_to_path_html(src_path):
	for maindir, subdir_list, file_name_list in os.walk(src_path):
		# print("1:",maindir) #当前主目录
		# print("2:",subdir_list) #当前主目录下的所有目录
		# print("3:",file_name_list)  #当前主目录下的所有文件
		for filename in file_name_list:
			md_file_name = os.path.join(maindir, filename)#合并成一个完整路径
			convert_to_file_html(md_file_name)

		for subdir in subdir_list:
			convert_to_path_html(subdir) #递归

# html 文件转换 pdf
def convert_to_file_pdf(html_file_name):
	if html_file_name.endswith('.html'):
		pdf_file_name = html_file_name.replace('.html', '.pdf')
		pdf_file_name = pdf_file_name.replace(g_work_path + g_output_html_dir, g_work_path + g_output_pdf_dir)
		
		#创建目录
		tmp_path = os.path.dirname(pdf_file_name)
		if not os.path.exists(tmp_path):
			os.makedirs(tmp_path)
		
		print("1:", pdf_file_name)
		path_wk = r'D:\xxx\wkhtmltopdf.exe' # wkhtmltopdf安装位置
		config = pdfkit.configuration(wkhtmltopdf = path_wk)
		with open(html_file_name, 'r', encoding='utf-8') as f:
			html = f.read()
			html = html_template.format(content=html) 
			pdfkit.from_string(html, pdf_file_name, configuration=config)
			time.sleep(0.05)

# 将指定目录下的所有 html 文件转换 pdf（包含子目录）
def convert_to_path_pdf(src_path):
	print(src_path)
	for maindir, subdir_list, file_name_list in os.walk(src_path):
		for filename in file_name_list:
			html_file_name = os.path.join(maindir, filename)#合并成一个完整路径
			convert_to_file_pdf(html_file_name)

		for subdir in subdir_list:
			convert_to_path_pdf(subdir) #递归
					
def main():
	convert_to_path_html(g_work_path)
	convert_to_path_pdf(g_work_path + g_output_html_dir)
		

if __name__ == '__main__':
	main()
	
		
		
		
	