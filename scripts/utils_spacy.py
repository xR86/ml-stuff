# general
import spacy
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob

# term extraction
from pyate import cvalues, basic, combo_basic, weirdness, term_extractor

# keyword extraction
from textacy.ke.textrank import textrank
from textacy.ke.yake     import yake
from textacy.ke.scake    import scake
from textacy.ke.sgrank   import sgrank


def test_pyate(string, peek_len=3):
	typer = {
		'Cvalues': cvalues,
		'basic': basic,
		'combo_basic': combo_basic,
		'weirdness': weirdness,
		'term_extractor': term_extractor,
	}

	for algo_name, algo in typer.items():
		print(f'\n{"-" * 10}{algo_name}{"-" * 10}')
		print(algo(string).sort_values(ascending=False).head(peek_len))

def test_textacy(string, peek_len=3):
	typer = {
		'noun_chunks':    lambda xstr: list(nlp(xstr).noun_chunks)[:peek_len],
		'noun_phrases':   lambda xstr: TextBlob(xstr).noun_phrases[:peek_len],
		'textrank':       lambda xstr: textrank(nlp(xstr), window_size=2)[:peek_len],
		'yake':           lambda xstr: yake(nlp(xstr))[:peek_len],
		'scake':          lambda xstr: scake(nlp(xstr))[:peek_len],
		'sgrank':         lambda xstr: sgrank(nlp(xstr))[:peek_len],
	}

	for algo_name, algo in typer.items():
		print(f'\n{"-" * 10}{algo_name}{"-" * 10}')
		print(algo(string))


if __name__ == '__main__':
	string = 'The Enron Center garage will be opening very soon.Employees who work \
		for business units that are scheduled to move to the new building and \
		currently park in the Allen Center or Met garages are being offered a \
		parking space in the new Enron Center garage.'
	test_pyate(string)
	test_textacy(string)
