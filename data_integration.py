"""
Data Integration Module

Handles loading data from various sources (CSV, JSON, REST APIs, message queues).
Provides data normalization and validation.

TODO: Enhance with more robust error handling and real data sources.
"""

import csv
import json
import os


class DataIngestor:
    """Load data from various sources with graceful fallbacks to example data."""
    
    def load_csv(self, path):
        """
        Load CSV data from a file.
        
        Args:
            path: File path to CSV
            
        Returns:
            list[dict]: Rows as dictionaries
        """
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        else:
            # Return example rows if file missing
            return [
                {"id": "1", "name": "Sample A", "value": "100"},
                {"id": "2", "name": "Sample B", "value": "200"},
            ]
    
    def load_json(self, path):
        """
        Load JSON data from a file.
        
        Args:
            path: File path to JSON
            
        Returns:
            dict or list: JSON data
        """
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Return example payload if file missing
            return {
                "status": "example",
                "data": [
                    {"field1": "value1", "field2": "value2"},
                    {"field1": "value3", "field2": "value4"},
                ]
            }
    
    def fetch_rest(self, url, timeout=5):
        """
        Fetch data from REST API.
        
        Args:
            url: REST endpoint URL
            timeout: Request timeout in seconds
            
        Returns:
            dict: Response data or offline status
        """
        try:
            import requests
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except ImportError:
            # requests not installed
            return {"status": "offline", "reason": "requests module not available", "url": url}
        except Exception as e:
            # Network unavailable or other error
            return {"status": "offline", "reason": str(e), "url": url}
    
    def subscribe_topic(self, topic_name):
        """
        Subscribe to a message queue topic (stub).
        
        Args:
            topic_name: Name of the topic
            
        Returns:
            str: Subscription ID
            
        TODO: Implement actual message queue subscription
        """
        return f"subscription_{topic_name}_001"


class DataPipeline:
    """Normalize and validate data."""
    
    def normalize(self, data):
        """
        Normalize data by lowercasing keys.
        
        Args:
            data: dict or list[dict]
            
        Returns:
            Normalized data
        """
        if isinstance(data, dict):
            return {k.lower(): v for k, v in data.items()}
        elif isinstance(data, list):
            return [self.normalize(item) if isinstance(item, dict) else item for item in data]
        return data
    
    def validate(self, data, required_keys=None):
        """
        Validate data has required keys.
        
        Args:
            data: dict to validate
            required_keys: list of required key names
            
        Returns:
            tuple: (ok: bool, issues: list[str])
        """
        if required_keys is None:
            return (True, [])
        
        if not isinstance(data, dict):
            return (False, ["Data is not a dictionary"])
        
        issues = []
        for key in required_keys:
            if key not in data:
                issues.append(f"Missing required key: {key}")
        
        return (len(issues) == 0, issues)
