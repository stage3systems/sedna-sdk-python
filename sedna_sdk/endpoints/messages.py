import re
import json

class MessagesAPI:
    """
    Message endpoints
    """
    def __init__(self, client):
        self.client = client

    def get_to_emails(self, to_list):
        """
        Parse the 'to' field and return a list of dictionaries with name and email.
        :param to_list: List of 'to' entries as strings
        :return: List of dictionaries with 'name' and 'email' keys
        """
        parsed_to = []
        for to_entry in to_list:
            to_entry = to_entry.strip()

            match = re.match(r'^(.*)<(.+)>$', to_entry)
            if match:
                parsed_to.append({
                    "name": match.group(1).strip(),
                    "email": match.group(2).strip(),
                })
            else:
                parsed_to.append({
                    "name": None,
                    "email": to_entry,
                })

        return parsed_to


    def create_reply_draft(self, message_id: str, user_id: str, user_team_id: str):
        """
        Create a reply draft for a message.

        :param message_id: ID of the message to reply to
        :param user_id: ID of the user creating the reply
        :param user_team_id: ID of the team the user belongs to
        :return: Mapped response with selected attributes
        """
        data = {
            "data": {
                "attributes": {
                    "fromUser"  : user_id,
                    "fromTeam"  : user_team_id,
                    "timeZone" :  "Asia/Dhaka"
                },
                "type": "message"
            }
        }
        response = self.client._request("POST", f"/message/{message_id}/reply", json=data)
        attributes = response.get('data', {}).get('attributes', {})

        mapped = {
            "id"        : response.get("data", {}).get("id", ""),
            "subject"   : attributes.get("subject", ""),
            "fromName"  : attributes.get("fromName", ""),
            "fromEmail" : attributes.get("fromEmail", ""),
            "to"        : self.get_to_emails(attributes.get("to", "")),
            "cc"        : attributes.get("cc", ""),
            "bcc"       : attributes.get("bcc", ""),
            "snippet"   : attributes.get("snippet", ""),
            "bodyText"  : attributes.get("bodyText", ""),
            "bodyHtml"  : attributes.get("bodyHtml", ""),
            "receivedAt": attributes.get("receivedAt", ""),
            "sentAt"    : attributes.get("sentAt", ""),
        }

        return mapped


    def send_reply_message(self, message_id: str, body: str, user_id: str, user_team_id: str):
        """
        Send a reply message.

        :param message_id: ID of the message to reply to
        :param body: Body of the reply message
        :param user_id: ID of the user sending the reply
        :param user_team_id: ID of the team the user belongs to
        :return: Response from the API
        """
        draft_response = self.create_reply_draft(message_id, user_id, user_team_id)
        data = {
            "data": {
                "attributes": {
                    "subject"   : draft_response['subject'],
                    "body"      : (draft_response.get('bodyHtml') or "") + "<br><br>" + body,
                    "fromName"  : draft_response['fromName'],
                    "fromEmail" : draft_response['fromEmail'],
                    "to"        : draft_response['to'],
                    "cc"        : [],
                    "bcc"       : []
                },
                "type": "message"
            }
        }
        return self.client._request("PATCH", f"/message/{draft_response['id']}/send?scanForVirus=0&sendDelay=2&currentTeamId={user_team_id}", json=data)

