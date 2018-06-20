from unittest import TestCase
from src.utils import copytree
import os
import shutil

class TestUtils(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.original_test_path = '/media/joaojdneves_1/Trabalho/personal/multimedia-files-management/tests/mock_original'
        cls.destination_test_path = '/media/joaojdneves_1/Trabalho/personal/multimedia-files-management/tests/mock_original_temp'

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.exists(self.destination_test_path):
            shutil.rmtree(self.destination_test_path)

    def test_utils_existing_dir(self):
        """copytree should copy an entire directory to the specified destination"""
        copytree(self.original_test_path, self.destination_test_path)
        self.assertTrue(os.path.exists(self.destination_test_path))

    def test_utils_non_existing_dir(self):
        """copytree should raise a FileNotFoundError trying to copy a non existing directory"""
        with self.assertRaises(FileNotFoundError):
            copytree(os.path.join(self.original_test_path, 'temp'), self.destination_test_path)
