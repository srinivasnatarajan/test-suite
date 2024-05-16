import argparse
import os
from datetime import datetime
from pathlib import Path

import pytest
import requests
from test_suite.src.Constants.constant import Constant
from test_suite.src.initializer_set_up import BaseSetup
from test_suite.src.utilities.logger import Logger
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

def execute_suite(args):
    try:
        path = Constant.TEST_FOLDER
        report_path = Constant.REPORT_FOLDER + "/report.html"
        pytest.main(
            [
                path,
                "-m " + Constant.config['type'],
                "--tb=line",
                "-v",
                "--html=" + report_path,
                "--self-contained-html",
                "-k " + Constant.config["testFilter"],
            ]
        )

    except Exception as e:
        print("failure path message: ", e)


def send_report():
    file_name = str(Path(Constant.REPORT_FOLDER) / "report.html")
    dt_string = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    try:
        with open(f"{file_name}", 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        total_cases_element = soup.select_one('.run-count')
        passed_cases_element = soup.select_one('.passed')
        failed_cases_element = soup.select_one('.failed')
        skipped_cases_element = soup.select_one('.skipped')


        # Create a table for test case counts
        table_html = f"<table style='border-collapse: collapse; width: 100%;'>" \
                     f"<tr><th style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>Category</th>" \
                     f"<th style='border: 1px solid #dddddd; text-align: left; padding: 8px;'>Count</th></tr>" \
                     f"<tr><td style='border: 1px solid #dddddd; padding: 8px;'>Total Cases Run</td>" \
                     f"<td style='border: 1px solid #dddddd; padding: 8px;'>{total_cases_element.text}</td></tr>" \
                     f"<tr><td style='border: 1px solid #dddddd; padding: 8px;'>Passed Cases</td>" \
                     f"<td style='border: 1px solid #dddddd; padding: 8px; color: green;'>{passed_cases_element.text}</td></tr>" \
                     f"<tr><td style='border: 1px solid #dddddd; padding: 8px;'>Failed Cases</td>" \
                     f"<td style='border: 1px solid #dddddd; padding: 8px; color: red;'>{failed_cases_element.text}</td></tr>" \
                     f"<tr><td style='border: 1px solid #dddddd; padding: 8px;'>Skipped Cases</td>" \
                     f"<td style='border: 1px solid #dddddd; padding: 8px; color: orange;'>{skipped_cases_element.text}</td></tr></table>"

        response = requests.post(
            f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
            auth=("api", f"{os.getenv('MAILGUN_API_KEY')}"),
            files=[("attachment", open(f"{file_name}"))],
            data={"from": f"QA Automation <{os.getenv('SENDER_EMAIL')}>",
                  "to": f"{os.getenv('TO_EMAIL')}",
                  "cc": f"{os.getenv('SENDER_EMAIL')}",
                  "subject": f"Rewards Automation Regression Report - {datetime.now().strftime('%d/%m/%Y')}",
                  "text": "Automation Report",
                  "html": f"Automation Report for {dt_string} <br>"
                          f"{table_html}"})
        #curl_command = curlify.to_curl(response.request)
        #Logger.log(curl_command)
        Logger.log(response.status_code)
        Logger.log(response.text)
    except (FileNotFoundError) as e:
        Logger.log(f"Error getting file from path: {e}")


def argument_parser():
    if not os.path.exists(Constant.REPORT_FOLDER):
        os.makedirs(Constant.REPORT_FOLDER)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", help="Please mention the environment", default="staging")
    parser.add_argument(
        "-f", help="Add filter to run specific case", default="")
    parser.add_argument(
        "-t", help="Specify the type of test (api or ui)", default="api")
    return parser.parse_args()


args = argument_parser()
if args.t.lower() not in ["ui", "api"]:
    print("Please specify either 'ui' or 'api' for the test type.")
else:
    execute_suite(args)
    BaseSetup.initialize_base(argument_parser())
    execute_suite(argument_parser())
    send_report()
