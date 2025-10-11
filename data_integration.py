"""
data_integration.py

Real-world data integration module for Nomimi.
Provides connectors for CSV/JSON (local), REST (HTTP), and MQTT/WebSocket (stubs).
"""

import csv
import json
import os


class DataIngestor:
    """
    Handles data ingestion from various sources.
    
    TODO: Add error handling and validation for all data sources.
    TODO: Implement retry logic for network calls.
    TODO: Add authentication support for REST APIs.
    TODO: Implement real MQTT/WebSocket connections when needed.
    """
    
    def __init__(self):
        self.loaded_data = []
    
    def load_csv(self, filepath):
        """
        Load data from a CSV file.
        
        Args:
            filepath: Path to the CSV file
            
        Returns:
            list: List of dictionaries representing CSV rows
        """
        if not os.path.exists(filepath):
            print(f"[DataIngestor] CSV file not found: {filepath}")
            return []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                self.loaded_data.extend(data)
                print(f"[DataIngestor] Loaded {len(data)} records from CSV")
                return data
        except Exception as e:
            print(f"[DataIngestor] Error loading CSV: {e}")
            return []
    
    def load_json(self, filepath):
        """
        Load data from a JSON file.
        
        Args:
            filepath: Path to the JSON file
            
        Returns:
            dict or list: Parsed JSON data
        """
        if not os.path.exists(filepath):
            print(f"[DataIngestor] JSON file not found: {filepath}")
            return {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"[DataIngestor] Loaded JSON data")
                return data
        except Exception as e:
            print(f"[DataIngestor] Error loading JSON: {e}")
            return {}
    
    def fetch_rest(self, url, method='GET', headers=None, data=None):
        """
        Fetch data from a REST API endpoint.
        
        Args:
            url: API endpoint URL
            method: HTTP method (GET, POST, etc.)
            headers: Optional HTTP headers
            data: Optional request body data
            
        Returns:
            dict: Example/dummy data when offline or for stub implementation
            
        TODO: Implement actual HTTP requests using requests library (optional dependency)
        TODO: Add response caching mechanism
        TODO: Implement rate limiting
        """
        # Stub implementation - return example data
        print(f"[DataIngestor] REST stub: {method} {url}")
        return {
            "status": "stub",
            "message": "REST API integration not yet implemented",
            "url": url,
            "method": method,
            "sample_data": [
                {"id": 1, "value": "Example record 1"},
                {"id": 2, "value": "Example record 2"}
            ]
        }
    
    def subscribe_topic(self, broker_url, topic):
        """
        Subscribe to an MQTT or WebSocket topic (stub implementation).
        
        Args:
            broker_url: MQTT broker or WebSocket server URL
            topic: Topic to subscribe to
            
        Returns:
            dict: Stub message indicating feature not implemented
            
        TODO: Implement MQTT connection using paho-mqtt (optional dependency)
        TODO: Implement WebSocket connection using websocket-client (optional dependency)
        TODO: Add message buffering and callback mechanisms
        """
        print(f"[DataIngestor] MQTT/WebSocket stub: subscribing to {topic} at {broker_url}")
        return {
            "status": "stub",
            "message": "MQTT/WebSocket integration not yet implemented",
            "broker": broker_url,
            "topic": topic
        }


class DataPipeline:
    """
    Processes and validates ingested data.
    
    TODO: Add schema validation using jsonschema or similar
    TODO: Implement data transformation pipelines
    TODO: Add data quality metrics
    """
    
    def __init__(self):
        self.processed_records = []
        self.errors = []
    
    def normalize(self, records):
        """
        Normalize data records to a consistent format.
        
        Args:
            records: List of data records
            
        Returns:
            list: Normalized records
        """
        normalized = []
        for record in records:
            # Simple normalization: ensure all keys are lowercase
            normalized_record = {k.lower(): v for k, v in record.items()}
            normalized.append(normalized_record)
        
        self.processed_records.extend(normalized)
        print(f"[DataPipeline] Normalized {len(records)} records")
        return normalized
    
    def validate(self, records, required_fields=None):
        """
        Validate data records against requirements.
        
        Args:
            records: List of data records
            required_fields: List of required field names
            
        Returns:
            tuple: (valid_records, invalid_records)
        """
        if required_fields is None:
            required_fields = []
        
        valid = []
        invalid = []
        
        for idx, record in enumerate(records):
            missing_fields = [f for f in required_fields if f not in record]
            if missing_fields:
                invalid.append((idx, record, f"Missing fields: {missing_fields}"))
                self.errors.append(f"Record {idx}: missing {missing_fields}")
            else:
                valid.append(record)
        
        print(f"[DataPipeline] Validated: {len(valid)} valid, {len(invalid)} invalid")
        return valid, invalid
    
    def get_summary(self):
        """
        Get a summary of data pipeline processing.
        
        Returns:
            dict: Summary statistics
        """
        return {
            "total_processed": len(self.processed_records),
            "errors": len(self.errors),
            "error_details": self.errors[:10]  # First 10 errors
        }
