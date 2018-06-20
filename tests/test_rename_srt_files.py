from unittest import TestCase
from src.rename_srt_files import rename_srt_files
import glob
import os
import shutil
from src.utils import copytree

class RenameSrtFilesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.original_test_path = '/media/joaojdneves_1/Trabalho/personal/multimedia-files-management/tests/mock_original'
        cls.test_dir = 'mock_original_temp'
        cls.destination_test_path = os.path.join('/media/joaojdneves_1/Trabalho/personal/multimedia-files-management/tests', cls.test_dir)
        copytree(cls.original_test_path, cls.destination_test_path)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.exists(self.destination_test_path):
            shutil.rmtree(self.destination_test_path)

    def test_rename_srt_files_por(self):
        rename_srt_files(self.destination_test_path, 'por')
        
        expected_result = {
            'tests/mock_original_temp/root/bar/season1/bar-eng.srt',
            'tests/mock_original_temp/root/bar/season1/bar-pob.srt',
            'tests/mock_original_temp/root/bar/season1/bar.srt',
            'tests/mock_original_temp/root/bar/season2/bar-eng.srt',
            'tests/mock_original_temp/root/bar/season2/bar.srt',
            'tests/mock_original_temp/root/bar/season2/bar.srt',
            'tests/mock_original_temp/root/foo/season1/foo-eng.srt',
            'tests/mock_original_temp/root/foo/season1/foo.srt',
            'tests/mock_original_temp/root/foo/season1/foo.srt',
            'tests/mock_original_temp/root/foo/season2/foo-eng.srt',
            'tests/mock_original_temp/root/foo/season2/foo.srt',
            'tests/mock_original_temp/root/foo/season2/foo.srt'
        }

        result_dir = '**/' + self.test_dir + '/**/*.srt'
        result = set(glob.glob(result_dir, recursive=True))

        self.assertSetEqual(expected_result, result)


    