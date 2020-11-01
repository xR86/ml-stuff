import email as em

from tqdm import tqdm
tqdm.pandas()

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def load_emails(default_path='emails.csv', chunksize=10000):
	emails = pd.read_csv(default_path, chunksize=chunksize)
	emails = next(emails)
	return emails

def payload_extractor(emails):
	messages_obj_lst = []
	messages_str_lst = []

	message_metadata = {}

	for i in tqdm(range(emails.shape[0])):
		msg = em.message_from_string(emails.message[i])
		
		for msg_property in msg:
			if msg_property in message_metadata:
				message_metadata[msg_property][i] = msg[msg_property]
			else:
				message_metadata[msg_property] = ['N/A'] * emails.shape[0]
		
		payload = msg.get_payload() # decode=True
		
		messages_obj_lst.append(msg)
		messages_str_lst.append(payload) #.encode('utf-8').decode('unicode_escape')

	emails = emails.assign(message_obj = pd.Series(messages_obj_lst).values)
	emails = emails.assign(payload     = pd.Series(messages_str_lst).values)
	emails['payload'] = emails.payload.str.replace(r'\n', '')
	emails.drop('message', axis=1, inplace=True)
	
	return emails


if __name__ == '__main__':
	emails_df = load_emails(chunksize=1000)
	print(emails_df.shape)
	emails_df = payload_extractor(emails_df)

	print(emails_df.head())
	emails_df.to_csv('emails_payload.csv', index=False)
