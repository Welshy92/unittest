import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.student = Student("Jacob", "Welsh")


    def tearDown(self):
        print("tearDown")

    
    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "Jacob Welsh")


    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_student_email(self):
        print("test_student_email")
        self.assertEqual(self.student.email_address, "jacob.welsh@email.com")


    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

if __name__ == "__main__":
    unittest.main()