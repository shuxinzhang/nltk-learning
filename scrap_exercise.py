import urllib2 as ulib
from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import os

def get_exercise_section(chapter_num):
	full_url = "http://www.nltk.org/book/ch"+chapter_num
	page = requests.get(full_url)
	html_content = page.text
	processed_content = BeautifulSoup(html_content)
	exercises = processed_content.find("div",{"id":"exercises"})
	# exercises = processed_content.find_all("ol.li")
	exercises_list = exercises.ol.children
	exercises = []

	for ex in exercises_list:
		if isinstance(ex,NavigableString):
			continue
		else:
			exercises.append(ex.text)
	return exercises

get_exercise_section("01")

def write_to_file(text,chapterNum,exNum):
	fileName = chapterNum + '-' + str(exNum+1)+".py"
	f = open(fileName,"w+")
	f.write(text)
	f.close()

def main(chapterNum):
	directory = "Chapter "+chapterNum
	print directory
	if not os.path.exists(directory):
		os.makedirs(directory)
		os.chdir(directory)
	else:
		os.chdir(directory)
	exercises = get_exercise_section(chapterNum)
	for i in range(0,len(exercises)):
		write_to_file(
			'import nltk \n \'\'\'\n'+ \
			exercises[i].encode('utf8')+ \
			'\'\'\'\n',chapterNum,i)
	os.chdir("..")
main("01")
main("02")
main("03")
main("04")
main("05")
main("06")
main("07")
main("08")
main("09")
main("10")
main("11")

