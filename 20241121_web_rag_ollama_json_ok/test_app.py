import unittest
import os
import json
from gradio_app import (
    verify_json_data,
    generate_source_data,
    build_context,
    get_data_file_path
)

class TestRAGChatbot(unittest.TestCase):
    def setUp(self):
        self.test_query = "Microsoft latest financial results"
        
    def test_data_directory_exists(self):
        """Test if data directory exists"""
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        self.assertTrue(os.path.exists(data_dir))
        
    def test_generate_source_data(self):
        """Test if source data generation works"""
        ddg_data, gnews_data, wiki_data = generate_source_data(self.test_query)
        
        # Check if data was retrieved
        self.assertIsInstance(ddg_data, list)
        self.assertIsInstance(gnews_data, list)
        self.assertIsInstance(wiki_data, dict)
        
        # Check if data files were created
        self.assertTrue(os.path.exists(get_data_file_path("ddg.json")))
        self.assertTrue(os.path.exists(get_data_file_path("gnews.json")))
        self.assertTrue(os.path.exists(get_data_file_path("wikipedia.json")))
        
    def test_json_verification(self):
        """Test JSON verification functionality"""
        test_data = {"test": "data"}
        test_file = "test.json"
        
        # Save test data
        with open(get_data_file_path(test_file), 'w') as f:
            json.dump(test_data, f)
            
        # Verify the data
        self.assertTrue(verify_json_data(test_data, test_file))
        
        # Clean up
        os.remove(get_data_file_path(test_file))
        
    def test_context_building(self):
        """Test context building functionality"""
        context = build_context(self.test_query)
        
        # Check if context contains essential components
        self.assertIn("Current Date and Time:", context)
        self.assertIn("User Query:", context)
        self.assertIn("DuckDuckGo Search Results:", context)
        self.assertIn("Recent News:", context)
        
    def tearDown(self):
        """Clean up any test artifacts"""
        pass

if __name__ == '__main__':
    unittest.main()
