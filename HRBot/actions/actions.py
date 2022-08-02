import csv
import os
from typing import Any, Text, Dict, List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, Content)
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import date


class ActionSearchCSV(Action):

    def name(self) -> Text:
        return "action_search_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        data = []
        with open("Emp_Record.csv") as csvf:
            readfile = csv.reader(csvf)
            for row in readfile:
                data.append(row)
        col = [x[1] for x in data]
        if name in col:
            dispatcher.utter_message(text="Your name is present in employee records. You can now proceed on.")
            dispatcher.utter_message(text = "I can help with:\n"
                                            "1. Requesting a bonafide certificate\n"
                                            "2. Answer Policy Related Questions\n"
                                            "Kindly provide me with your purpose.")
        else:
            dispatcher.utter_message(text="Your name is not present in employee records. Please contact HR for "
                                          "authentication.")
        return []


class ActionSendEmail(Action):
    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        purpose = tracker.get_slot('purpose')
        currentdate = date.today()
        data = []
        with open("Emp_Record.csv") as csvf:
            readfile = csv.reader(csvf)
            for row in readfile:
                data.append(row)
        col = [x[1] for x in data]
        if name in col:
            for x in range(1, len(data)):
                if name == data[x][1]:
                    address = data[x][2]
                    tenure = data[x][3]
                    designation = data[x][4]
                    emp_manager = data[x][5]
                    recv_email = data[x][6]
            message = """From:
                         <br>{emp_manager}
                         <br>{designation}
                         <br>XYZ Company Pvt. Ltd.
                         <br>Kerala
                         <br>{currentdate}<br> 
                         <br>To Whomsover It May Concern</b><br>
                         <br>This is to certify that <b>{name}</b> residing at {address} has been associated with XYZ Company Pvt. Ltd. 
                         <br>He/She has been working as {designation} for the past {tenure}.
                         <br><br>In his/her association of last {tenure}, he/she has been a dedicated and loyal employee of the company. His/Her commitment
                         <br>towards work makes him/her a valuable employee of the company.              
                         <br><br>This certificate has been issued for the purpose of {purpose}.
                        """


            message = Mail(
                from_email='hrxbot@gmail.com',
                to_emails=recv_email,
                subject='Request for Bonafide Certifcate',
                html_content=message.format(purpose=purpose, name=name, address=address, tenure=tenure,
                                            designation=designation,emp_manager=emp_manager, currentdate=currentdate)
            )
            mail_json = message.get()
            dispatcher.utter_message(text="Your request mail has been sent to your HR Manager.")
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.client.mail.send.post(request_body=mail_json)
        else:
            dispatcher.utter_message(text="Your name isn't verified. Cannot identify employee")
        return []


class ActionHandleFeedback(Action):
    def name(self) -> Text:
        return "action_handle_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any], ):
        samples = ['satisfied','very much','yes','yeah']
        feedback = tracker.get_slot('feedback')
        if feedback in samples:
            dispatcher.utter_message(text="If there is anything else you want me to do, please mention the task")
        else:
            dispatcher.utter_message(
                text="I am sorry for that !\nIf you want further assistance, kindly mail at hrbot.gmail.com.\n You "
                     "will be followed up soon")
        return []


class ActionCheckLeaveBalance(Action):

    def name(self) -> Text:
        return "action_check_leavebalance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot('name')
        data = []
        with open("Emp_Record.csv") as csvf:
            readfile = csv.reader(csvf)
            for row in readfile:
                data.append(row)
        col = [x[1] for x in data]
        if name in col:
            dispatcher.utter_message(text="Searching records...")
            for x in range(1, len(data)):
                if name == data[x][1]:
                    leaves = data[x][7]
                    dispatcher.utter_message(response="utter_leavebalance", leave_bal=leaves)
        else:
            dispatcher.utter_message(text="Your name isn't verified. Cannot identify employee")

        return []

