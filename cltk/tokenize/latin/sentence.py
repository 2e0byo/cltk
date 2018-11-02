""" Code for sentence tokenization: Latin
"""

__author__ = ['Patrick J. Burns <patrick@diyclassics.org>']
__license__ = 'MIT License.'

import os.path
from cltk.tokenize.sentence2 import BaseSentenceTokenizer
from cltk.utils.file_operations import open_pickle
from nltk.tokenize.punkt import PunktLanguageVars
#from nltk.metrics.scores import accuracy, precision, recall, f-score


class LatinLanguageVars(PunktLanguageVars):
    _re_non_word_chars = PunktLanguageVars._re_non_word_chars.replace("'",'')


class SentenceTokenizer(BaseSentenceTokenizer):
    """ Base class for sentence tokenization
    """

    def __init__(self):
        """
        :param language : language for sentence tokenization
        :type language: str
        """
        BaseSentenceTokenizer.__init__(self, 'latin')
        self.model = self._get_model()


    def tokenize(self, text, model=None):
        """
        Method for tokenizing sentences. This method
        should be overridden by subclasses of SentenceTokenizer.
        """
        if not self.model:
            model = self.model

        tokenizer = open_pickle(self.model)
        tokenizer._lang_vars = LatinLanguageVars()

        return tokenizer.tokenize(text)

        #return type(tokenizer), dir(tokenizer)
        #return tokenizer.sentences_from_text(text, realign_boundaries=True)


    def _get_model(self):
        model_file = '{}.pickle'.format(self.language)
        model_path = os.path.join('~/cltk_data',
                                self.language,
                                'model/' + self.language + '_models_cltk/tokenizers/sentence')  # pylint: disable=C0301
        model_path = os.path.expanduser(model_path)
        model_path = os.path.join(model_path, model_file)
        assert os.path.isfile(model_path), \
            'Please download sentence tokenization model for {}.'.format(self.language)
        return model_path


if __name__ == "__main__":
    sentences = """Sed hoc primum sentio, nisi in bonis amicitiam esse non posse; neque id ad vivum reseco, ut illi qui haec subtilius disserunt, fortasse vere, sed ad communem utilitatem parum; negant enim quemquam esse virum bonum nisi sapientem. Sit ita sane; sed eam sapientiam interpretantur quam adhuc mortalis nemo est consecutus, nos autem ea quae sunt in usu vitaque communi, non ea quae finguntur aut optantur, spectare debemus. Numquam ego dicam C. Fabricium, M'. Curium, Ti. Coruncanium, quos sapientes nostri maiores iudicabant, ad istorum normam fuisse sapientes. Quare sibi habeant sapientiae nomen et invidiosum et obscurum; concedant ut viri boni fuerint. Ne id quidem facient, negabunt id nisi sapienti posse concedi."""
    tokenizer = SentenceTokenizer()
    sents = tokenizer.tokenize(sentences)
    print(sents)
