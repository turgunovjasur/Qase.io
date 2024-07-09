import unittest
from HtmlTestRunner import HTMLTestRunner
from test_registration import test_registration

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_registration)

    report_path = "../reports/test_report.html"
    with open(report_path, "w", encoding="utf-8") as report_file:
        runner = HTMLTestRunner(
            stream=report_file,
            title="Qase.io Registration Test Report",
            description="Test results for registration process"
        )
        runner.run(test_suite)
