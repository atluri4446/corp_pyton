import unittest
import requests
from Functions import URL, username

class LoginApiTests(unittest.TestCase):
    """Tests for validating the Login API responses."""
    
    def setUp(self):
        """Set up test environment before each test."""
        self.base_url = f"{URL}/api/method"
        # self.base_url = "https://stgcrm.rnit.solutions/api/method"
        
    def test_validate_login_api_response(self):
        """Test login API with correct credentials and validate the response."""
        # Prepare request payload
        payload = {
            "usr": username,
            "pwd": "Rnit@123"
        }
        
        # Send POST request to login API
        response = requests.post(f"{self.base_url}/login", json=payload)
        
        # Check if login was successful (status code)
        self.assertEqual(response.status_code, 200, "Login API should return 200 status code")
        
        # Parse response body
        response_body = response.json()
        print('🔹 Response Body:', response_body)
        
        # Validate basic authentication fields
        self.assertEqual(response_body.get('message'), 'Logged In', "Message should be 'Logged In'")
        self.assertIn('home_page', response_body, "Response should contain 'home_page'")
        self.assertIn('full_name', response_body, "Response should contain 'full_name'")
        self.assertIn('current_datetime', response_body, "Response should contain 'current_datetime'")
        self.assertEqual(response_body.get('username'), username, "Username should match the requested username")
        self.assertIn('sid', response_body, "Response should contain session ID")
        self.assertIsNotNone(response_body.get('sid'), "Session ID should not be null")
        
        # Validate employee details
        self.assertIn('emp_id', response_body, "Response should contain employee ID")
        self.assertIn('designation', response_body, "Response should contain designation")
        self.assertIn('branch', response_body, "Response should contain branch")
        self.assertEqual(response_body.get('is_enrolled'), '1', "is_enrolled should be '1'")
        
        # Validate role and menu details
        self.assertEqual(response_body.get('roleId'), '1', "roleId should be '1'")
        self.assertEqual(response_body.get('web_menu'), 'Admin', "web_menu should be 'Admin'")
        self.assertEqual(response_body.get('custom_hrms_profile'), '0', "custom_hrms_profile should be '0'")
        self.assertEqual(response_body.get('custom_crm_profile'), '0', "custom_crm_profile should be '0'")
        
        # Validate attendance data
        self.assertIn('attendnace_data', response_body, "Response should contain attendance data")
        attendance_data = response_body.get('attendnace_data')
        self.assertIn('emp_count', attendance_data, "Attendance data should contain employee count")
        self.assertIn('present_count', attendance_data, "Attendance data should contain present count")
        self.assertIn('levave_count', attendance_data, "Attendance data should contain leave count")
        self.assertIn('absent_count', attendance_data, "Attendance data should contain absent count")
        
        # Validate timestamps
        timestamp_fields = [
            'location_time_stamp', 'user_time_stamp', 'menu_time_stamp', 
            'shift_time_stamp', 'ai_const_time_stamp', 'holiday_time_stamp', 
            'leave_type_time_stamp', 'faceify_config_time_stamp', 
            'assigned_shift_time_stamp'
        ]
        
        for field in timestamp_fields:
            self.assertIn(field, response_body, f"Response should contain {field}")
        
        # Validate other configuration details
        self.assertEqual(response_body.get('user_profile'), '/mobile/myprofile', 
                         "user_profile should be '/mobile/myprofile'")
        self.assertIn('checkincheckout', response_body, "Response should contain checkincheckout")
    
    def test_validate_login_api_with_incorrect_credentials(self):
        """Test login API with incorrect credentials and validate the error response."""
        # Prepare request payload with wrong credentials
        payload = {
            "usr": "wrong_user@test.com",
            "pwd": "wrongPassword"
        }
        
        # Send POST request to login API
        response = requests.post(f"{self.base_url}/login", json=payload)
        
        # Check if login fails with correct status code
        self.assertEqual(response.status_code, 401, "Login with wrong credentials should return 401")
        
        # Parse response body
        response_body = response.json()
        print('🔹 Error Response:', response_body)
        
        # Validate error message
        self.assertEqual(response_body.get('message'), 'Invalid login credentials', 
                         "Error message should indicate invalid credentials")


if __name__ == "__main__":
    unittest.main()