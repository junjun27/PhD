import wikipediaapi
import csv
import pandas

wiki_wiki = wikipediaapi.Wikipedia('fr')

# If we import skills from file.csv
def load_data(file):
	Skill = []
	data = pandas.read_csv(file)
	col = ['Skill_name']
	data.columns = col
	print("data shape", data.shape)
	Skill_name = data.Skill_name.values
	Skill_name = list(set(Skill_name))

	Skill_num = len(Skill_name)
	Pages = []
	for i in range(0,Skill_num):
		Pages.append(wiki_wiki.page(Skill_name[i]))

	return Pages, Skill_name, Skill_num



def print_categories(page):
        categories = page.categories
        for title in sorted(categories):
        	if (title.__contains__('Article') or title.__contains__('Bon article en') or title.__contains__('Page')):
        		categories.pop(title)
        for title in sorted(categories.keys()):
        	print("%s" % (title))

def main():
	Skill_name = ['A+ (langage)', 'C++ (langage)', 'C (langage)', 'Java (langage)']
	Skill_num = len(Skill_name)
	Pages = []
	for i in range(0,Skill_num):
		Pages.append(wiki_wiki.page(Skill_name[i]))
	for i in range(Skill_num):
		print("Page - Title: %s" % Pages[i].title)
		print("Page - Exists: %s" % Pages[i].exists())
		print("Page - Summary: %s" % Pages[i].summary.split('.')[0]+'.')
		print_categories(Pages[i])

		print("===================================================")
	
				

if __name__ == "__main__":
#	Pages, Skill_name, Skill_num = load_data('skills.csv')
	main()


