"""The full unit test suite, testing every available model for every language."""

import unittest

import numpy

from cltkv1 import NLP
from cltkv1.languages.example_texts import get_example_text
from cltkv1.core.data_types import Doc, Word
from cltkv1.embeddings.embeddings import FastTextEmbeddings


class TestStringMethods(unittest.TestCase):

    def test_embeddings_fasttext(self):
        embeddings_obj = FastTextEmbeddings(iso_code="ang", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="mōnaþ")[0][0]
        self.assertEqual(most_similar_word, "hāliȝmōnaþ")

        embeddings_obj = FastTextEmbeddings(iso_code="arb", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="بعدها")[0][0]
        self.assertEqual(most_similar_word, "وبعدها")

        embeddings_obj = FastTextEmbeddings(iso_code="arc", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="ܒܠܚܘܕ")[0][0]
        self.assertEqual(most_similar_word, "ܠܒܪ")

        embeddings_obj = FastTextEmbeddings(iso_code="got", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="𐍅𐌰𐌹𐌷𐍄𐌹𐌽𐍃")[0][0]
        self.assertEqual(most_similar_word, "𐍅𐌰𐌹𐌷𐍄𐍃")

        embeddings_obj = FastTextEmbeddings(iso_code="lat", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="amicitia")[0][0]
        self.assertEqual(most_similar_word, "amicitiam")

        embeddings_obj = FastTextEmbeddings(iso_code="pli", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="anattamanā")[0][0]
        self.assertEqual(most_similar_word, "kupitā")

        embeddings_obj = FastTextEmbeddings(iso_code="san", interactive=False, overwrite=False, silent=True)
        most_similar_word = embeddings_obj.get_sims(word="निर्माणम्")[0][0]
        self.assertEqual(most_similar_word, "निर्माणमपि")

    def test_embeddings_word2vec(self):
        pass


if __name__ == "__main__":
    unittest.main()
