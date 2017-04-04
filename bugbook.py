import click
import json
import os.path
import sys
from difflib import SequenceMatcher

@click.group()
def cli():
	click.echo('Thanks for using!')

@click.command()
@click.argument('title')
@click.argument('category')
@click.argument('tech')
@click.argument('problemnotes')
@click.argument('solutionnotes')


def add(title, category, tech, problemnotes, solutionnotes):
	if os.path.isfile('data.txt'):
		click.echo('file exists')
		with open('data.txt') as json_file:
			data = json.load(json_file)
			data['bugs'].append({
			    'title': title,
			    'type': category,
			    'problemNotes': problemnotes,
			    'tech': tech,
			    'solutionNotes': solutionnotes
			})
			with open('data.txt', 'w') as outfile:  
				json.dump(data, outfile)
	else:
		click.echo('file doesnt exist')
		data = {}
		data['bugs'] = []
		data['bugs'].append({
		    'title': title,
		    'type': category,
		    'problemNotes': problemnotes,
		    'tech': tech,
		    'solutionNotes': solutionnotes
		})
		with open('data.txt', 'w') as outfile:  
			json.dump(data, outfile)


@click.command()
@click.argument('category')
@click.argument('tech')
@click.argument('problemnotes')

def search(category, tech, problemnotes):
	with open('data.txt') as json_file:
		data = json.load(json_file)
		maxsim = 0.0
		bestMatchCategory = ""
		bestMatchTech = ""
		bestMatchProblemNotes = ""
		#click.echo(len(data['bugs']))
		bestMatchTech = ""
		bestMatchCategory = ""
		bestMatchProblemNotes = ""
		bestMatchSolution = ""
		maxMatchingScore = 0.0
		for b in data['bugs']:
			#calculate match score. each matching tech is one point, problemNotes similar * 2, category match + 1.5, no matching tech -1, no matching category -1
			
			#Calculate tech score 
			searchTech = tech.split(" ")
			techMatches = 0 
			anyTechMatches = False
			aaa = 0
			for uuu in searchTech:
				bbb = 0
				holdem = b['tech'].split(" ")
				for vvv in holdem:
					if searchTech[aaa] == holdem[bbb]:
						techMatches = techMatches + 1
						anyTechMatches = True
					bbb = bbb + 1
				aaa = aaa + 1
			techScore = techMatches
			if anyTechMatches:
				techScore = techScore - 1.0

			#Calculate category score:
			categoryScore = 0.0
			if category == b['type']:
				categoryScore = 1.5

			#Calculate problem notes score
			problemNotesScore = similar(problemnotes, b['problemNotes']) * 2.0

			totalScore = techScore + categoryScore + problemNotesScore
			#click.echo("-------------")
			#click.echo('total score for:')
			#click.echo(b['type'] + " " + b['tech'] + " " + b['problemNotes'] + " is:")
			#click.echo(totalScore)
			#click.echo("tech score: " + str(techScore))
			#click.echo("type score: " + str(categoryScore))
			#click.echo("problem notes score: " + str(problemNotesScore))

			if totalScore > maxMatchingScore:
				maxMatchingScore = totalScore
				bestMatchTech = b['tech']
				bestMatchCategory = b['type']
				bestMatchProblemNotes = b['problemNotes']
				bestMatchSolution = b['solutionNotes']
		click.echo("=====================================================================")
		click.echo("Best Match")
		click.echo("\n")
		click.echo("Tech used: " + bestMatchTech)
		click.echo("\n")
		click.echo("Type of error: " + bestMatchCategory)
		click.echo("\n")
		click.echo("Problem notes: " + bestMatchProblemNotes)
		click.echo("\n")
		click.echo("Soltuion: " + bestMatchSolution)
		click.echo("\n")

cli.add_command(add)
cli.add_command(search)




def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == '__main__':
    cli()
